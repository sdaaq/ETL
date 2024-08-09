# ETL | DATA PIPELINE | PET PROJECT
# Архитектура
![image](https://github.com/user-attachments/assets/fba4978f-55d8-45a8-b5bf-13640ee88c39)

# Описание проэкта
В ходе дата пайплайна сенсор каждый час проверяет наличие обновлений файла на сайте USDA.
Данные на сайте обновляют 2-3 раза в неделю.
Формат входных данных txt. При распаковке вес файла 7.5-7.8 Гб

Airflow установлен локально и развернут в виртуальной среде pycharm. Там же установлена СУБД postgreSQL для метаданных airflow.
Аirflow работает на  localexecutor.

Spark(pyspark) развернут в виртуальной среде через pycharm.
Данные поступают в spark и там обогащаются.
Спарк складывает данные в формат csv.

Clickhouse развернут локально.
Clickhouse считывает данные из файла csv в таблицу.

К кликхаусу подключаются внешние bi инструменты.

# Структура DAGа в airflow
![image](https://github.com/user-attachments/assets/7a6c201a-f5bc-45ab-a3a5-1cda1bdf5df4)


# Экскурс о значении полученной информации
Каждый месяц Министерство сельского хозяйства США публикует статистические данные и сопутствующую информацию о
производстве сельскохозяйственных культур в Соединенных Штатах и ​​мире.

Оценки спроса и предложения сельскохозяйственных культур,
подготовленные Министерством сельского хозяйства США,
имеют решающее значение как для политиков в правительстве, так и для людей,
принимающих решения о маркетинге и инвестировании.

Эти оценки используются в качестве ориентиров на рынке из-за
их всеобъемлющего характера, объективности и своевременности. 

Статистические данные, которые публикует USDA, влияют
на решения, принимаемые фермерами, предприятиями и правительствами, определяя
фундаментальные условия на
рынках товаров.

# Структура хранилища в clickhouse.
Все данные хранятся в одной таблице.

На основе этой таблицы собираются запросы.

Если данные обновляются, то таблица полностью перезаписывается.

![image](https://github.com/user-attachments/assets/b8955549-08a2-4287-a5d4-5592059d76ee)


# Дашборд из графаны
Развернутая локально графана, подключенная к clickhouse.

Цифры вычисленные на основе сырых данных сходятся, с отчетами USDA, что может говорить о правильно проведенной обработкe.
![image](https://github.com/user-attachments/assets/3cf782a6-15b1-4584-bc89-df264c9ba657)




