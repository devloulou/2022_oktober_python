"""
raw sql  - sql utasításokat, natív

select ....
insert ...

1. kell egy kapcsolat az adatbázishoz

"""

from sqlalchemy import create_engine

# create_engine  - hozza létre a kapcsolatot a python és az adatbázis között
# URL vs URI - az adatbázis kapcsolat leíró stringje

engine = create_engine("sqlite:///test.db")

create_test_table = """create table test_table(id number, name text)"""

insert_data = """
insert into test_table(id, name) values (1, 'Ricsi')
"""

engine.execute(insert_data)

result_set = engine.execute('select * from test_table')

for item in result_set:
    print(item)
