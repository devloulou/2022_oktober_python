from sqlalchemy import create_engine

# fileból az adatot betöltjük adatbázisba -> adatbázisba való adatintegrálást -> ETL
# ETL - Extract Transform Load - Extract és a Tranfrom része is az adatbázison kívül történik meg
# ETL során az adatot általában már jól strukturált és megfelelő adattípussal ellátott táblába töltjük 
#
# ELT - Extract Load Transform - A Transform már az adatbázisban történik meg
# ELT esetén lesz egy "érkeztetési terület", ahová gyakorlatilag a nyers adatot betöltjük
# változatlan formában
# és ezután az adatbázus oldalon valósítjuk meg az adatok típusosítását, strukturálását és adat tisztítását és 
# egy transzformációs lépéseket


class DBHandler:
    def __init__(self, postgres_url):
        #create_engine("postgresql://scott:tiger@localhost/mydatabase")
        self.engine = create_engine(postgres_url)


    @staticmethod
    def create_table(cols):
        create_statement = "create table if not exists employee_data ("

        for idx, col in enumerate(cols):
            # if idx < len(cols) - 1:
            #     create_statement += f"{col} text, \n"
            # else:
            #     create_statement += f"{col} text )"
            
            # ternary operátor: igaz_ág feltétel hamis ág  - one liner
            create_statement += f"{col} text, \n" if idx < len(cols) - 1 else f"{col} text )"

        return create_statement

    @staticmethod
    def create_insert_statement(cols):
        # insert into employee_data (col1, col2, col3 ... coln) values ('liutya', 'alma'.---)
        # adatbázik komplex rendszerek -> saját működésük van -> "önálló életet élnek"
        # próbálják optimalizálni az utasításokat: insertek esetén a javaslat: használj bind változókat
        # bind változók: placeholder -> insert into tabla (col1, col2) values (:value1, :value2)
        # bind változók: placeholder -> insert into tabla (col1, col2) values (?, ?)
        insert_statement = "insert into employee_data ("
        insert_values = " values ("

        for idx, col in enumerate(cols):
            insert_statement += f"{col}, " if idx < len(cols) - 1 else f"{col} ) "
            insert_values += f"%s, " if idx < len(cols) - 1 else f"%s ) "

        return insert_statement + insert_values

    def execute_sql(self, sql_query):
        with self.engine.connect() as conn:
            try:
                conn.execute(sql_query)
            except Exception as e:
                print(str(e))

    def insert_many(self, insert_statement, data):
        with self.engine.connect() as conn:
            try:
                conn.execute(insert_statement, data)
            except Exception as e:
                print(str(e))    


if __name__ == '__main__':
    from file_handler import FileHandler
    from connection_params import postgres_url

    db = DBHandler(postgres_url)

    test = FileHandler()

    test.file_path = r"C:\WORK\2022_oktober_python\17. alkalom\data\employee.txt"

    data = test.get_data_from_txt()

    ins_data = test.create_data_for_insert(data)

    create_table = db.create_table(ins_data['cols'])
    insert_statement = db.create_insert_statement(ins_data['cols'])

    db.execute_sql(create_table)
    db.insert_many(insert_statement, ins_data['data'])

    # with db.engine.connect() as conn:
    #     test = conn.execute("select 1")

    #     print(test.fetchall())