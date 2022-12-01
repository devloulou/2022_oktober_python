/*
 * departmentenként hány dolgozónk van
 * 
 * */

select * from hr_workers;
select * from employee;
select * from jobs;
select * from departments;

/*
 * group by - csoportosítás
 * 
 * */
select d.department_name,  count(e.employee_id) from departments d
inner join jobs j on d.department_id  = j.department_id
inner join hr_workers hw on j.job_id  = hw.job_id
inner join employee e on hw.employee_id = e.employee_id 
and e.salary  > 50000
group by d.department_id, d.department_name
;

/*
 * departmentenként mennyi a minimum fizetés, a maximum, az átlag,
 * hány emberem van
 * 
 * az sql script adatbázis kiértékelési sorrend:
 * 
 * először lekéri a táblálból az adatokat, a joinoknak megfelelően
 * aztán ha  van where feltétel, akkor elvégzi a szűréseket
 * ha van group by akkor megcsinálja a csoportosítást
 * ha van having, akkor megcsináljja a having kiértékelését
 * aztán a mezőket abban a formában állítja elő, ahogy a select .. from között van megadva
 * ha van order by akkor az ott megadott rendezést kiértékeli
 * ha van limit, akkor annak megfelően adja vissza a rekordszámot
 * */
select d.department_name,
min(e.salary) as min_sal,
max(e.salary) as max_sal,
avg(e.salary) as avg_sal,
sum(e.salary) as sum_sal,
count(e.employee_id) as cnt
from departments d
inner join jobs j on d.department_id  = j.department_id
inner join hr_workers hw on j.job_id  = hw.job_id
inner join employee e on hw.employee_id = e.employee_id
where e.salary > 50000
group by d.department_name
--having count(e.employee_id) > 1
--having min(e.salary) > 68000 and count(e.employee_id) >= 1
order by min_sal desc--- desc - csökkenő, asc- növekvő
limit 1
;


/*
 * 
 * materializálás
 * sub selectek
 * 
 * */

/*
 * count, avg, min, max, sum - aggregáló függvények
 * 
 * window functions - analitikus függvények
 * 
 * departmentenként mennyi a minimum fizetés, a maximum, az átlag,
 * hány emberem van
 * 
 * */

select 
--- fuggveny()over(opcionális: partition by mezo, mezo ... , opcionális: order by mezo, mezo, mezo)
min(e.salary)over(partition by d.department_id order by d.department_id) as min_sal,
e.salary, e."name", d.department_name 
from departments d
inner join jobs j on d.department_id  = j.department_id
inner join hr_workers hw on j.job_id  = hw.job_id
inner join employee e on hw.employee_id = e.employee_id


/*hány db departmentem van*/
select distinct e.department_id from employees_hrschema e;

select count(distinct e.department_id) from employees_hrschema e;

select
distinct
e.department_id,
min(e.salary)over(partition by e.department_id) as min_sal,
max(e.salary)over(partition by e.department_id) as max_sal,
avg(e.salary)over(partition by e.department_id) as avg_sal,
sum(e.salary)over(partition by e.department_id) as sum_sal
--,e.*
from employees_hrschema e;

select e.salary, e.* from employees_hrschema e
where e.department_id = 7;

select * from employees_hrschema;

/*
 * rank, dense_rank, row_number
 * */

select
row_number()over(partition by salary order by salary) as rnk,
salary
from employee e ;

/*subselect*/
select * from
(select
row_number()over(partition by department_id order by salary desc) as rnk,
--max(salary)over(partition by department_id),
--rank()over(partition by salary order by salary) as r_ank,
--dense_rank()over(order by salary) as dens_rnk,
salary, department_id-- concatenacio - python string-eket állítunk elő
from employees_hrschema t) base_data
where rnk = 1
order by department_id, rnk 




