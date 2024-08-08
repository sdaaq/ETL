# ETL | DATA PIPELINE | AITRFLOW DATA PIPELINE
# АРХИТЕКТУРА
![image](https://github.com/user-attachments/assets/fba4978f-55d8-45a8-b5bf-13640ee88c39)

# Overview

В ходе дата пайплайна сенсор каждый час проверяет наличие обновлений файла на сайте.
Данные на сайте обновляют 2-3 раза в неделю.
Формат входных данных txt. При распаковке вес файла 7.5-7.8 Гб

Данные поступают в спарк и там обогащаются.
Спарк складывает данные в формат csv.

Clickhouse читает данные из файла csv.
К кликхаусу подключаются внешние bi инструменты.

# Airflow
![image](https://github.com/user-attachments/assets/7a6c201a-f5bc-45ab-a3a5-1cda1bdf5df4)


# Мб  структура таблиц из кликхауса

# ДАШБОРДЫ В ГРАФАНЕ С ПРИМЕРАМИ СТАТИСТИКИ ПРОИЗВОДСТВА ПО ГОДАМ VEGETABLES которые хочется
![image](https://github.com/user-attachments/assets/82f50fcc-6f90-4328-b7e7-10b72eb7ef6d)


