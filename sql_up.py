
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
