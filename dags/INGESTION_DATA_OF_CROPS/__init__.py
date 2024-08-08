from datetime import datetime
from .functions import list_queries, download_data, transform_data, check

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.python import PythonSensor
from airflow_clickhouse_plugin.operators.clickhouse import ClickHouseOperator


with DAG(
        dag_id='our_testing_DAG',
        start_date=datetime(2024, 8, 6),
        schedule='@hourly',
        tags=['pet_dag'],
        catchup=False,
) as dag:

    check_file = PythonSensor(
        task_id='check_update_file_on_site',
        timeout=10,
        mode="reschedule",
        python_callable=check,
        soft_fail=True,
    )

    downloading = PythonOperator(
        task_id='get_data_from_source',
        python_callable=download_data,
    )

    transformation = PythonOperator(
        task_id='transform_data_with_spark',
        python_callable=transform_data,
    )


    create_data = ClickHouseOperator(
        task_id='insert_data_to_clickhouse',
        sql=list_queries(),
        clickhouse_conn_id='clickhouse_connect',
        do_xcom_push=False,
    )

    check_file >> downloading >> transformation >> create_data

