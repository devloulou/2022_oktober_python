from utils.file_handler import FileHandler
from utils.database_handler import DBHandler
from utils.sql_helper import insert_employee_final_data
from utils.connection_params import postgres_url

def elt_main(file_path):
    db = DBHandler(postgres_url)
    test = FileHandler()

    test.file_path = file_path

    data = test.get_data_from_txt()
    ins_data = test.create_data_for_insert(data)
    create_table = db.create_table(ins_data['cols'])
    insert_statement = db.create_insert_statement(ins_data['cols'])

    db.execute_sql(create_table)
    db.insert_many(insert_statement, ins_data['data'])

    db.execute_sql(insert_employee_final_data)


if __name__ == '__main__':
    elt_main(r"C:\WORK\2022_oktober_python\17. alkalom\data\employee.txt")