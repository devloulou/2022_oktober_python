-- reguláris kifejezések nem lesz

/*
 * string függvények
 * dátum függvények
 * 
 * */

/*
 * string függvények - stringgel különböző műveletek
 * */
select
-- to_char(dátum, 'formátum')
to_char(e.birthday, 'Mon. DD. YYYY'),
to_date(to_char(e.birthday, 'Mon. DD. YYYY'), 'Mon. DD. YYYY'),
e.birthday 
from employee e;

-- dummy table
-- trim() - a mező elejéről és végéről levágja a megadott karaktert, alap esetben
-- a spaceket
select trim(to_char(9000000, '999,999,999,999,999'));

select to_char(9000000, '9,999,999')

--substring : ki"csomagoljunk" egy adott string részletet a megadott sztringből

select substring('amerika',4,5)

select substring('0630/123-4567',6)

-- strpos - egy megadott karakter első pozícióját adja vissza
select strpos('060/123-4567', '/')

-- az union és union all: ugyan annyi oszlopnak, ugyan olyan adattípussal kell rendelkeznie
-- union - egyesíti a 2 "halmazt", a két select eredményét
-- ha ugyan azt az adatot atartalmazza, akkor distinctálja
-- duplikációt kiszűri -> ez egy költséges művelet
select '0630/123-4567', 1
union
select '063/123-4567', 0
union 
select'06/123-4567', 0
union 
select '0630/123-4567', 0 


-- union all
-- split_part
select
substring(col, strpos(col, '-') + 1),
split_part(col, '-', 2),
col
from
(select '0630-123-4567' as col
union all
select '063-5345-4567' as col
union all
select '06-6858-4567' as col
union all
select '0630-5674573-4567' as col
) base_data;


---- Dátum függvények

select now();

select localtimestamp; 

--- extract

select extract(week from now())


select now() + interval '6 year'


