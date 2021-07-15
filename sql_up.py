
# Выведите сумму всех стоимостей в одном запросе по датам и по городам и по типам товара из таблицы 2
SELECT city, type, sum(cost), reportdate FROM Table2
GROUP BY city, type, reportdate;

# Покажите все строчки где есть null из таблицы 2
SELECT city, type, cost, reportdate FROM Table2
WHERE city is Null;

# Просуммируйте стоимость в таблицах для города Paris, по типам товара
WITH T2 as (SELECT type, sum(cost) as summa FROM Table2
    GROUP BY city, type
    HAVING city = 'Paris'
    UNION ALL SELECT type, sum(cost) as summa FROM Table1
    GROUP BY city, type
    HAVING city = 'Paris')
SELECT type, sum(summa) from T2
GROUP BY type;

# Объедините данные из двух таблиц, найдите максимальную и минимальную стоимость по каждому типу товаров и в каждом городе на каждую дату. 
# Выведите в виде одной таблицы формата – город, дата, тип товара, макс. стоимость, мин. стоимость

# Первый ваариант
WITH dates as (SELECT city, type, cost, reportdate FROM Table2
UNION ALL SELECT city, type, cost, reportdate FROM Table1)
SELECT city, type, min(cost), max(cost), reportdate
FROM dates
GROUP BY city, type, reportdate;


# Второй ваариант
SELECT city, type, min(cost), max(cost), reportdate
FROM(
    SELECT city, type, cost, reportdate FROM Table2
    UNION ALL SELECT city, type, cost, reportdate FROM Table1) x
GROUP BY city, type, reportdate;


# На основе предыдущего задания, добавьте к таблице ближайшую предыдущую дату и добавьте в 
# вывод предыдущую дату, макс.стоимость и мин.стоимость на эту дату.  
# (можно использовать cte, временные таблицы и любые альтернативные подходы)

WITH four as (SELECT city, type, min(cost) as minimal, max(cost) as maximal, reportdate,
LAG(reportdate) OVER (PARTITION BY type, city ORDER BY reportdate ASC) as Last_Date
FROM(
    SELECT city, type, cost, reportdate FROM Table2
    UNION ALL SELECT city, type, cost, reportdate FROM Table1) x
GROUP BY city, type, reportdate)
SELECT four.city, four.type, four.minimal, four.maximal, four.reportdate, four.Last_Date, x.minimal, x.maximal from four
LEFT JOIN four as x ON four.Last_Date = x.reportdate and four.city = x.city and four.type = x.type;











# Выведите все уникальные даты из таблицы 1, где есть информация по городу Lyon для ананасов (Pinapple)
SELECT DISTINCT reportdate FROM Table1
WHERE city = 'Lyon' and type = 'Pinapple';

# Выведите уникальный список городов и товаров из обеих таблиц
with t1 as (
    SELECT * from Table1
    UNION ALL SELECT * from Table2
)
SELECT DISTINCT city, type from t1;

# Найдите такие типы товаров для Lyon, которые отсутствуют в таблице 2, но которые есть в таблице 1
SELECT Table1.type FROM Table1
LEFT JOIN Table2 ON Table1.type = Table2.type and Table2.city = Table1.city
WHERE Table2.type is NULL and Table1.city = 'Lyon';

# Найдите все даты из таблицы 1, которых нет в таблице 2
SELECT Table1.reportdate FROM Table1
LEFT JOIN Table2 ON Table1.reportdate = Table2.reportdate
WHERE Table2.reportdate is NULL;

# Объедините таблицы и выведите для каждого города самый дорогой товар
With t1 as (SELECT * FROM Table1
UNION ALL SELECT * from Table2),
t2 as (SELECT city, max(cost) as cost from t1
GROUP BY city)
SELECT t1.city, t1.type from t1
LEFT JOIN t2 ON t1.city = t2.city
WHERE t1.cost = t2.cost

# Объедините таблицы и выведите все неуникальные строки
SELECT * FROM (SELECT * FROM Table1
UNION ALL SELECT * from Table2) z
GROUP BY city, type, cost, reportdate
HAVING count(*)>1;
