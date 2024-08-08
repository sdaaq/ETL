# ETL | DATA PIPELINE | AITRFLOW DATA PIPELINE
# АРХИТЕКТУРА
ТУТ БУДЕТ МОДЕЛЬ АРХИТЕКТУРЫ

1)EXTRACT | DOWNLOAD ON LOCAL MACHINE FROM SOURCE (USDA CROPS) WITH AIRFLOW

2)TRANSFORM | TRANSFORM WITH SPARK IN CSV

3)LOAD | LOAD TO CLICKHOUSE

4) JOIN EXTERNAL BI TECHNOLOGIES (GRAFANA)
# OVERVIEW

Данные выгружаются в текстовом формате из сайта Департамента Агрокультуры США.
В ходе дата пайплайна проверяется наличие обновлений файла на сайте.
Данные на сайте обновляются где-то 2-3 раза в неделю.
Данные поступают в парк и там обогащаются.
Спарк складывает данные в формат csv.
Clickhouse читает данные из файла csv.
К кликхаусу подключаются внешние bi инструменты.

# ТУТ БУДЕТ ETL из airflow

# Мб  структура таблиц из кликхауса

# дашборды в графане
