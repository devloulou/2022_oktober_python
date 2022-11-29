/*
 * 
 	employee_id	name	salary birth_day
 	department_id	department_name	leader_id (employyee_id)
	job_id	job_name	department_id	
	employee_id	job_id	start_date
	

 * */

create table employee(
	employee_id serial primary key,
	name text,
	salary int,
	birthday date	
);

create sequence seq_jobs
start with 100
increment by 100;

create sequence seq_departments
start with 10
increment by 10;

create table departments (
	department_id int primary key default nextval('seq_departments'),
	department_name text,
	department_leader int references employee(employee_id)
);


create table jobs (
	job_id int primary key default nextval('seq_jobs'),
	job_name text,
	department_id int references departments(department_id)
);

create table hr_workers (
	employee_id int references employee(employee_id),
	job_id int references jobs(job_id),
	start_date date
);

select * from employee;
select * from departments;
select * from jobs;
select * from hr_workers ;

insert into employee (name, salary, birthday)
values
('Gipsz Jakab', 70000, to_date('1980.08.10.', 'YYYY.MM.DD.'));

insert into employee (name, salary, birthday)
values
('Mekk Elek', 50000, to_date('1970.05.15.', 'YYYY.MM.DD.'));

insert into employee (name, salary, birthday)
values
('Lapos Elemér', 67000, to_date('1990.08.10.', 'YYYY.MM.DD.'));

insert into employee (name, salary, birthday)
values
('Kálid Artúr', 170000, to_date('1960.08.10.', 'YYYY.MM.DD.'));

insert into employee (name, salary, birthday)
values
('Hajmási Péter', 48000, to_date('1976.08.10.', 'YYYY.MM.DD.'));
----------------------------------------------------------
select * from departments;

insert into departments (department_name, department_leader)
values ('Development', 4);

insert into departments (department_name, department_leader)
values ('Call Center', 1);

----------------------------------------------------------

select * from jobs;

insert into jobs (job_name, department_id)
values ('Data Engineer', 10);
insert into jobs (job_name, department_id)
values ('Backend Developer', 10);
insert into jobs (job_name, department_id)
values ('Development Team Lead', 10);
insert into jobs (job_name, department_id)
values ('Call Center Operator', 20);
insert into jobs (job_name, department_id)
values ('Call Center Supervisor', 20);

---------------------------------------------
select * from hr_workers;
select * from employee;
select * from jobs;
select * from departments;

insert into hr_workers (employee_id, job_id, start_date)
values (1, 500, to_date('2021.10.01.', 'YYYY.MM.DD.'));

insert into hr_workers (employee_id, job_id, start_date)
values (2, 200, to_date('2021.10.01.', 'YYYY.MM.DD.'));

insert into hr_workers (employee_id, job_id, start_date)
values (3, 100, to_date('2021.10.01.', 'YYYY.MM.DD.'));

insert into hr_workers (employee_id, job_id, start_date)
values (4, 300, to_date('2021.10.01.', 'YYYY.MM.DD.'));

insert into hr_workers (employee_id, job_id, start_date)
values (5, 400, to_date('2021.10.01.', 'YYYY.MM.DD.'));

-----------------------------------------------------------

/*
 * légyszíves készíts nekem egy riportot, 
 * amiben benne van, hogy pl. a developement department, 
 * hány ember dolgozik és havonta pl. mennyi pénzbe kerülnek a cégnek
 * 
 * */


select * from hr_workers;
select * from employee;
select * from jobs;
select * from departments;
----------------------------
-- alias: táblát, mezőket
select employee_id, name as full_name, salary
from employee e1;

-- filterezés - szűrés - where feltétel
-- and - or
-- or - vagy kapcsolat - ha bármelyik feltétel teljesül,
-- akkor visszaadja az ahoz tartozó adatot
select * from employee e
where e.employee_id = 1 or e.name = 'Horváth Feri'
or e.employee_id = 5;

-- and - és kapcsolat
-- minden vizsgálatnak igaznak kell lennie, akkor ad vissza adatot

select * from employee e
where e.employee_id = 1 and e.name = 'Gipsz Jakab'
;

--- tagadás !=

select * from employee e
where e.employee_id != 1
and e.salary > 50000; -- <> egyéb adatbázisokban ezt is megengedik

--------------------------
-- aggregáció -> window function

/*
 * átlag, minimum, maximum, össz érték - summa - , darabszám
 * */

-- avg, count, min, max, sum
select
avg(e.salary) as atlag_fizu,
count(e.employee_id),
min(e.salary),
max(e.salary),
sum(e.salary)
from employee e;

select * from employee ;

/*
 * a departmenteknek kik a vezetői
 * */

select d.department_name, e.name from departments d
inner join employee e on d.department_leader = e.employee_id;

/*
 * kik azok a dolgozók, akik nem vezetők
 * */

select * from departments d right join employee e 
on d.department_leader = e.employee_id
--where d.department_id is null
;

select * from employee e 
left join departments d on d.department_leader = e.employee_id
--where d.department_id is null
;

select * from employee e
full outer join departments d on e.employee_id = d.department_leader