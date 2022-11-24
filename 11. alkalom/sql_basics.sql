/*
 * session, mi az hogy tranzakció
 * insert, update, delete
 * alter 
 * 
 * session: user által nyitott kapcsolat az adatbázis felé
 * 
 * postgresben MINDEN ADATBÁZIS MŰVELET "COMMIT KÖTELES"
 * 
 * tranzakció: az adatbázis művelet: select, insert, update, delete, create,
 * drop, alter, truncate ... explain.... grant, revoke, explain plan,
 * comment
 * 
 * 2 állapota lehet: vagy lezárt, vagy lezáratlan tranzakció
 * 
 * lezárt tranzakció:
 * 					- jóváhagyva: commit utasítás
 * 					- visszavonva: rollback utasítás
 * 
 * lezáratlan tranzakció
 * 
 * rollback: amennyi ideig tart a tranzakció, megközeleítőleg annyi ideig fog tartani
 * a rollback utasítás
 * 
 * execute - kiadod az adatbázisnak azadatbázis műveletet, hogy végezze el
 * 
 * */
drop table test_ricsi;

alter table test_ricsi add age int;

create table test_ricsi (name text);

drop table test_table;
create table test_table (id int);


select * from test_ricsi;

insert into test_ricsi(name) values ('Misi');
update test_ricsi set name = 'Ricsi';
delete from test_ricsi;
select * from test_ricsi;

/*
 * 
 * 
 * */


/*
 * insert , 
 * 
 * update, delete
 * select
 * */

create table users (
	id int,
	user_name text,
	age int,
	mother_name text,
	date_of_birth date
);

select to_char(t.date_of_birth,  'YYYY.MM.DD.'), t.date_of_birth from users t;
-- 1 adat insertje
insert into users (id, user_name, age, mother_name)
values (1, 'John Wick', 45, 'ismeretlen');

---
insert into users (user_name, id, mother_name, age, date_of_birth)
values('John Ramnbo', 2, 'undefined', 36, to_date('1967/07/12', 'YYYY/MM/DD'));

-------------------------------------------------------------------------
select *from users;

-- módosítás: update

update users set user_name = 'John Rambo', age = 73, mother_name= 'Ilona'
where id = 2
--user_name = 'John Ramnbo'
;

-- delete utasítás: sor / sorok törlése

delete from users where id = 2;
--delete users where id = 2;

/*
Normalizált vs Denormalizált
OLTP - normál formák: 3NF
Adattárház: dimenzionális modellezés: Kimball
            Inmoni: 3NF
            Data Vault: hibrid: 3NF és dimenzionális




adatmodellezés alapjai: OLTP, 3NF adatmadollezés
kapcsolat táblák között
kulcsok
indexek
megszorítások

select és hozzátartozó utasítások

*/

