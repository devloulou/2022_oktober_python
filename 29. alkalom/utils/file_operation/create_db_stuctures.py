import os
from config import data_folder_path
from file_handler import FileHandler

test = FileHandler()

test.data_folder_path = data_folder_path

files = test.get_files_list()

for item in files[:]:
    data = test.get_data_from_csv(item)
    file_name = os.path.basename(item)[:-4]

    data.rename(columns={'Country/Region' : 'country_region',
        'New cases' : 'new_cases',
        'New deaths' : 'new_deaths',
        'New recovered' : 'new_recovered',
        'Deaths / 100 Cases' : 'death_100_cases',
        'Recovered / 100 Cases' : 'recovered_100_cases',
        'Deaths / 100 Recovered' : 'deaths_100_recovered',
        'Confirmed last week' : 'confirmed_last_week',
        '1 week change' : 'week_1_change',
        '1 week % increase' : 'week_1_increase',
        'WHO Region' : 'who_region',
        'Province/State': 'province_state',
        'No. of countries': 'no_of_countries',
        'Date': 'ddate',
        'Serious,Critical': 'serious_critical',
        'Tot Cases/1M pop': 'tot_cases_1m_pop',
        'Deaths/1M pop': 'deaths_1m_pop',
        'Tests/1M pop': 'tests_1M_pop'

        }, inplace=True)


    cols = {}
    # ide kellene a create table

    for key, val in data.dtypes.to_dict().items():
        if val == 'object':
            cols[key] = "text"
        elif 'int' in str(val):
            cols[key] = "integer"
        elif 'float' in str(val):
            cols[key] = "numeric"
        else:
            cols[key] = "text"

    create_tab = f"create table {file_name} if not exists ("

    for k, v in cols.items():
        create_tab += f"{k} {v},"

    print(create_tab)
    print("------------------------")
    # ide kellene az insert into 