# ETL | DATA PIPELINE | AITRFLOW DATA PIPELINE
# Архитектура
![image](https://github.com/user-attachments/assets/fba4978f-55d8-45a8-b5bf-13640ee88c39)

# Overview
Airflow установлен локально и развернут в виртуальной среде pycharm. Там же установлена СУБД postgreSQL для метаданных airflow.
Аirflow работает на  localexecutor.

В ходе дата пайплайна сенсор каждый час проверяет наличие обновлений файла на сайте.
Данные на сайте обновляют 2-3 раза в неделю.
Формат входных данных txt. При распаковке вес файла 7.5-7.8 Гб

Spark(pyspark) развернут в виртуальной среде через pycharm.
Данные поступают в spark и там обогащаются.
Спарк складывает данные в формат csv.

Clickhouse развернут локально.
Clickhouse считывает данные из файла csv в таблицу.

К кликхаусу подключаются внешние bi инструменты.

# Airflow
![image](https://github.com/user-attachments/assets/7a6c201a-f5bc-45ab-a3a5-1cda1bdf5df4)


# Структура таблицы в хранилище clickhouse

# Дашборд из графаны
Развернутая локально графана, подключенная к clickhouse
Цифры вычисленные из необработанных данных сходятся, с отчетами USDA, что может говорить о правильно проведенной обработки.
![image](https://github.com/user-attachments/assets/bcc484f2-9a31-4484-ae6e-871991d1f5f5)



