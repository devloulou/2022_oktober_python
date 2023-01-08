from sqlalchemy import create_engine, inspect
from sqlalchemy import MetaData, Table, Column, String, Integer

engine = create_engine("sqlite:///test.db")

meta = MetaData(engine)

test_table = Table("my_table", meta,
                Column('id', Integer, primary_key=True),
                Column('name', String(100))
            )

insp = inspect(engine)

if not insp.has_table("my_table"):
    test_table.create()

######
# insert

# insert_statement = test_table.insert().values(id=1, name='Alma')
insert_statement = test_table.insert()

# contextusmanager
with engine.connect() as conn:
    if 1 == 2:
        for item in range(1, 11):
            conn.execute(insert_statement.values(id=item, name=f"Alma_{str(item)}"))

############################################

# update

    update_statement = test_table.update().where(test_table.c.id==2).values(name="jóska")

    conn.execute(update_statement)

# delete

    delete_statement = test_table.delete().where(test_table.c.id > 5)
    conn.execute(delete_statement)


    select_statement = test_table.select().where(test_table.c.id == 2)
    select_statement = test_table.select()#.where(test_table.c.id == 2)
    select_statement = test_table.select().with_only_columns([test_table.c.name, test_table.c.id])#.where(test_table.c.id == 2)

    result_set = conn.execute(select_statement)

    for item in result_set:
        print(item)