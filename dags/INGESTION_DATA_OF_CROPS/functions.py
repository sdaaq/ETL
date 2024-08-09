from datetime import datetime, date
import requests
import gzip
import wget
import shutil

from pyspark.sql import SparkSession
import os
from pyspark.sql.types import IntegerType, FloatType, TimestampNTZType
from pyspark.sql.functions import regexp_replace

def check():

    """Check actual date and availability of updated files on the site"""
    with open("/home/vitalii/PycharmProjects/ETL/files/download_date.txt", 'r') as f:
        url = "https://www.nass.usda.gov/datasets/qs.crops_" + date.today().strftime("%Y%m%d") + ".txt.gz"
        old_date = datetime.strptime(f.read(), "%Y%m%d")

        if date.today() > old_date.date() and requests.head(url).status_code == 200:
            return True


def download_data():
    date_now = date.today().strftime("%Y%m%d")
    file_url = "https://www.nass.usda.gov/datasets/qs.crops_" + date_now + ".txt.gz"

    """Download data from site"""
    file_name = wget.download(file_url, out='testing_data' + '.txt.gz')

    """Unzip data"""
    with gzip.open(file_name, 'rb') as f_in:
        with open('/home/vitalii/PycharmProjects/ETL/files/our_data.txt', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    """Update download_date"""
    with open("/home/vitalii/PycharmProjects/ETL/files/download_date.txt", "w") as file_date:
        file_date.write(date_now)

    os.remove(file_name)    # Remove temp. file
    return


def transform_data():
    spark = SparkSession.builder.getOrCreate()
    spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")
    df = spark.read.csv('/home/vitalii/PycharmProjects/ETL/files/our_data.txt', header=True, sep="\t", inferSchema=True)

    """Transform data"""
    df = df.withColumn('VALUE', regexp_replace('VALUE', ',', ''))
    df = df.withColumn('VALUE', df['VALUE'].cast(FloatType()))
    df = df.withColumn('LOAD_TIME', df['LOAD_TIME'].cast(TimestampNTZType()))

    """Drop empty columns"""
    df = df.drop('REGION_DESC', 'ZIP_5', 'WATERSHED_DESC', 'CONGR_DISTRICT_CODE', 'WEEK_ENDING', 'CV_%', 'WATERSHED_CODE', 'COUNTRY_CODE')

    """Save data in CSV"""
    df.repartition(1).write.csv("/var/lib/clickhouse/user_files", sep='|', mode='overwrite', nullValue='NULL', header='true')  # 1-2 minutes
    return

def list_queries():

    """My sql queries in list"""
    ls = ["""DROP TABLE IF EXISTS clickhouse.test""",
          """SET format_csv_delimiter = '|'""",
          """CREATE TABLE clickhouse.test (
    `SOURCE_DESC` String,
    `SECTOR_DESC` String,
    `GROUP_DESC` String,
    `COMMODITY_DESC` String,
    `CLASS_DESC` String,
    `PRODN_PRACTICE_DESC` String,
    `UTIL_PRACTICE_DESC` String,
    `STATISTICCAT_DESC` String,
    `UNIT_DESC` String,
    `SHORT_DESC` String,
    `DOMAIN_DESC` String,
    `DOMAINCAT_DESC` String,
    `AGG_LEVEL_DESC` String,
    `STATE_ANSI` UInt8,
    `STATE_FIPS_CODE` UInt8,
    `STATE_ALPHA` String,
    `STATE_NAME` String,
    `ASD_CODE` Nullable(UInt16),
    `ASD_DESC` Nullable(String),
    `COUNTY_ANSI` Nullable(UInt16),
    `COUNTY_CODE` Nullable(UInt16),
    `COUNTY_NAME` Nullable(String),
    `COUNTRY_NAME` String,
    `LOCATION_DESC` UInt32,
    `YEAR` UInt16,
    `FREQ_DESC` String,
    `BEGIN_CODE` UInt32,
    `END_CODE` UInt32,
    `REFERENCE_PERIOD_DESC` String,
    `LOAD_TIME` Datetime64,
    `VALUE` Float64
) 
ENGINE = MergeTree()
ORDER BY tuple(SOURCE_DESC, SECTOR_DESC) AS SELECT * FROM file("*.csv", CSV);"""]
    return ls
