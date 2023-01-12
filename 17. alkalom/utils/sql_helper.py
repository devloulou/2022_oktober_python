insert_employee_final_data = """
insert
	into
	employee_data_final (employee_id,
	first_name,
	last_name,
	email,
	phone_number,
	hire_date,
	job_id,
	salary,
	commission_pct,
	manager_id,
	department_id)
select
	cast(ed.employee_id as integer) as employee_id,
	ed.first_name,
	ed.last_name,
	ed.email,
	ed.phone_number,
	ed.hire_date::date as hire_date,
	-- megegyzik a ::type a cast függvény erredményével
	ed.job_id,
	cast(cast(ed.salary as float)as integer) as salary,
	nullif(trim(ed.commission_pct), '')::double precision as commission_pct,
	nullif(trim(ed.manager_id), '')::float::integer as manager_id,
	nullif(trim(ed.department_id), '')::float::integer as department_id
from
	employee_data ed
"""