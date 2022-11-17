---- Adatbázis ----
/*
 * Mi az adatbázis? Adatokat tárol, logikus, könnyen elérhető, kereshető és megbízható módon */
---- Relációs Adatbázis
/*
 * Relációs adatbázis: az adatok relációkkal vannak megvalósítva, közöttük kapcsolat
 * lehet építeni
 * */
---- Mi az a Reláció
/*
 * A reláció: az adatbázis tábla, táblák
 * 
 * */


----- Táblák

-- létrehozás, "törlés" -> eldobjuk, kiürítés, adattal való feltöltés, adat lekérdezés
-- adat módosítást tudunk, magát a táblát is tudjuk utólag módosítani


--- Adatbázis műveletek csoportosítása:

/*DDL - Data Definition Language
 * 
 * create, drop, alter, truncate
 * */
/*DML - Data Manipulation Language
 * 
 * update, delete, insert
 * 
 * */
/*DCL - Data Control Language
 * 
 * grant, revoke - jogosultság megadás, jogosultság elvétel
 * */
/*DQL - Data Query Language
 * 
 * select
 * 
 * */
/*TCL - Transaction Control Language
 * 
 * commit, rollback 
 * 
 * */



-------------------------------------------------------

CREATE TABLE my_first_table (
my_column int,
my_col2 text,
my_col3 date
);

select * from my_first_table;


/*
 * session, mi az hogy tranzakció
 * insert, update, delete
 * alter 
 * 
 * 
 * 
 * */
