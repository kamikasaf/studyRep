"""БАЗА Данных(БД) - это организованная структура, предназначенная для хранения, изменения и обработки взаимосвязанной информации, преимущественно больших объемов"""

"""
1 Иерархическая
2 Оьъектная и объектно ориентированная 
3 Реляционная
4 Объектно-реляционная
5 Сетевая
6 Функциональная 
"""

"""Отличительной чертой реляционных баз данных является возможность построения отношения между таблицами в базе данных"""

"""Нереляционные базы данных не имеют отношений между таблицами и состоят из модели коллекции и модели документа, в которых данные хранятся по типу ключ и значение"""

"""SQL(Structured Query Language) -это язык запросов, который используется в качестве эффективного способа сохранения данных, поиска их частей, обновления, извлечения и удаления из базы"""

"""СУБД(Система управления базами данных) - это комплекс программных средств, необходимых для создания структуры новой базы, ее наполнения, редактирования содержимого и отображения информации"""

"""
SQL запросы
простыми
вложенными
""" 
"""команды SQL"""

"""
# sudo -u postgres psql(psql postgres) - войти в sql
# \l открыть сущ базы данных
# \c name законнектиться к базе данных
# \dt \d увидеть все таблицы
# \du покажет всех userov

# create database name; создать базу данных
# create user name_user with password '12345'; - создать нового не главного юзера с паролем
# create database  name_database with onwer name_user - создать базуданных с другим овнером
# create table table_name(создавать поля имя поля, тип поля, ограничения)    создать таблицу

# alter role nama_user with superuser дать все привелегии другому юзеру 

# grant all privileges on database name_databse to name_user - дать все привелегии на базу данных

# drop database name; удалить таблицу
# drop role name_user -удалить юзера

# \d name_table подробдное инфо о таблице
# \dt name_table инфо о таблице
# \i /home/erlan/Downloads/students.sql найти и загрузить в sql
"""

"""Типы данных"""
# 1. numeric types -числовой тип данных
# 2. character types - как стр
# character varying(n), varchar(n)
# character(n), char(n) - char(n - указывает сколько символов будет занимать поля)
# text
# 3. Boolean Type
# 4. monetary types -для денег тип данных

# Enumerated types -предоставляет выбор из слов
# 5. Date/Time types 
# timestamp -  дата и время
# date - дата
# time - время
# interval

"""Constraints(ограничения)"""
# NOT NULL Constraint - поле не может быть пустым
# UNIQUE Constraint - все значения в этом поле должны быть уникальными
# PRIMARY Key - какое то поле будет идентифицировать какую то запись (тип ID)
# FOREIGN Key - внешний ключ который будет связывать другие таблицы
# CHECK Constraint - значение в поле отвечает каким то условиям
# EXCLUSION Constraint - бла бла бла
 

"""
Select

# select * from table_name увидеть таблицу
# select имя поля from table_name
# select * from table_name limit 5      limit количество 
# select * from offset 5 limit 5        offset с какого начать не включительно
# select * from table_name in название поля (перечисление);        поиск
# select field_name || field_name2 from students; --> || конкатинация строк

        AS
# select field_name || field_name2  as another field_name from students; --> || конкатинация строк

        Order by --> сортирует по какому то полю, по алфовитонму порядку или возрастанию
# select field_name from table_name order by field_name;
# select field_name from table_name order by field_name asc; возрастание
# select field_name from table_name order by field_name desc; убывание
nulls last пустые поля в конце
nulls first пустые поля вначале

        Distinct избавит от повторяющихся элементов
# select distinct field_name from table_name;  
# select distinct on(field_name) field_name, field_name2 from table_name order by field_name, field_name2; 

        Where - условие как if
# select * from table_name where название поля = '';            поиск
# select * from table_name where название поля = ''  and название поля = '' ;       поиск
# select * from table_name where название поля = ''  or название поля = '' ;       поиск
# select * from table_name where field_name > int
# <> не равно!
# and, or, not, in работают так же как в питоне
# 'some' and 'some' 
# 'some' or 'some'
# not some
# in ('some', 'some', 'some')
        beetween - между, между возрастом 20 и 30 и т.д
# select * from table_name where field_name between 20 and 30; 

        Like - чтобы в слове было определенное что то типа буквы вначале, в конце, в середине, заканчивалось на что то и т.д
        Ilike наоборот
# select * from table_name where field_name like 'A%'; где % значит что есть неограниченное продолжение
# like 'a_' значит что после а есть только 1 символ. _ означает один символ __ 2 и т.д

        Is 
# select * from table_name where last_name is null; 

        Limit ставит лимит сколько строк вытащить
        Fetch тот же лимит с другим синтаксисом
        Offset ставит начало 
# select * from table_name limit int;
# select * from table_name fetch first(10) row only;
# select * from table_name offset 4 fetch first(10) row only;
# select * from table_name limit 10 offset 5; вытащит 10 строк и начнет с 6;

        Group by - используется с агригационными функциями вытащит столбец с условием из агригационных функций
        Having - как where только для group by 
# aggregation functions: SUM(), AVG(), COUNT(), MIN(), MAX(), AGE()
# select sum(field_name) from table_name;  --> вытащит сумму какого то поля 
# select count(field_name) from table_name; --> количество
# select avg(field_name) from table_name;   --> среднее значение 
# select sum(field_name), field_name1 from table_name group by field_name1;
# select sum(field_name) from table_name gorup by field_name having sum(field_name) > 6

        Insert -- додавление в таблицу 
# insert into name_table(перечесление имен полей кроме автодекредетируемых) values(передaем название полей)
 
        Update -- изменение записи
# Update table_name Set field_name = value1, field_name2 = value2 where condition; - изменение значений в таблице где condition это условие, (id = 10) где нужно показать какую строку изменить по айди имени или ещ чему нибудь

        Delete --> удаление записи из таблицы
# Delete from table_name where codition 

        Alter Table --> работа с самой таблицей и ее столбцами
# alter table table_name add/rename/drop/alter column ...

        alter column --> изменение характеристики столбца (тип, null not null и т.д)
# alter table alter column field_name (type, set)  

        rename
# alter table table_name rename column field_name to new_field_name
        

        add constrain --> добавление ограничений
# alter table table_name add constrain name_constrain (field_name);

        drop --> удаление
# alter table table_name drop field_name;

"""


