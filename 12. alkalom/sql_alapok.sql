/*
 * Adatmodellezés alapjai:
 * 
 * 3NF
 * 
 * OLTP - OnLine Transactional Processing  
 * netbank, webshop, fizetési rendszer, 
 * 
 * OLAP (Adattárház - DWH(Data Warehouse)) - Online Analitical Processing * 
 * historikusan, idősorosan tárolod az adattal kapcsolatos változást
 * 
 * Data modelling: ER modell - Entity - Relationship modell
 * 
 * Conceptual: az elképzelt kapcsolatot felvázolod  a táblák között
 * felvázolod a táblákról való elképzelést
 * 
 * Logical: a felvázolt tábláknál megjelöli, hogy milyen mezők vannak, milyen adattípussal
 * Physical: adatbázisra specifikált adatmodellnek a megfeleltetése
 * 
 * 
 * */

-- hogyan alakítunk ki kapcsolatot táblák között
-- primary key  - elsődleges kulcs: egyedinek kell lennie, nem lehet null az értéke
-- foreign key

-- szülő
create table test_relation (
	relation_id int primary key,
	relation_desc text
);

-- gyermek tábla
drop table temp_table;
create table temp_table (
	temp_id int primary key,
	relation_id int references test_relation(relation_id) on delete cascade
);

select * from test_relation;
select * from temp_table;

insert into test_relation(relation_id, relation_desc) values (2, 'test');

/*SQL Error [23503]: ERROR: insert or update on table "temp_table" violates foreign key constraint "fk_rel_id"
  Detail: Key (relation_id)=(1) is not present in table "test_relation".*/

insert into temp_table (temp_id, relation_id) values (1, 2);

/*
 * SQL Error [23503]: ERROR: update or delete on table "test_relation" violates foreign key constraint "fk_rel_id" on table "temp_table"
  Detail: Key (relation_id)=(2) is still referenced from table "temp_table".
 * 
 * ezen hiba feloldása:
 * 1. a gyermek táblából törlöd azt / azokat a rekordokat, amelyeket a szülő táblából is törölni akarsz
 * 2. "force" olva törölöd a szülő táblából
 * 
 * */


delete from test_relation where relation_id = 2;

-- milyen kapcsolatok léteznek a táblák között






--------------------------------------------------------------------------------
-- sequence: adatbázis objektum típus, generáljon nekem egy értéket, valamilyen
-- megadott logika alapján

/*
 * sequence:
 * 1. insert során lekérem a sequence következő értékét: nextval('seq_department')
 * */

create sequence seq_department
start with 10
increment by 10;


create table departments (
	department_id int primary key DEFAULT nextval('seq_department'),
	name text
);

ALTER SEQUENCE seq_department
OWNED BY departments.department_id;

--------------------------------------------------
create sequence seq_jobs
start with 100
increment by 100;

create table jobs (
	
	job_id int primary key default nextval('seq_jobs'),
	name text,
	salary int,
	department_id int references departments(department_id) on delete cascade
);

ALTER SEQUENCE seq_jobs
OWNED BY jobs.job_id;
--------------------------------------------------

create table employee(
	employee_id serial primary key,
	name text,
	birth_date date,
	start_date date,
	job_id int references jobs(job_id)
);

create table leaders (
	leader_id serial primary key,
	employee_id int references employee(employee_id)
);



