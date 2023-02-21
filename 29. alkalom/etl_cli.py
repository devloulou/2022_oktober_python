import argparse
import os

from utils.database.db_handler import PostgresHandler
from utils.file_operation.file_handler import FileHandler
from utils.database.sql_helper import (day_wise_insert,
                                       full_grouped_insert,
                                       usa_county_wise_insert,
                                       country_wise_latest_insert,
                                       worldometer_data_insert,
                                       covid_19_clean_complete_insert)

from utils.database.connection_params import postgres_url
from utils.file_operation.config import data_folder_path

def load_all_csv():
    file = FileHandler()
    sql = PostgresHandler(postgres_url)

    mapping = {
        "country_wise_latest.csv": country_wise_latest_insert,
        "covid_19_clean_complete.csv": covid_19_clean_complete_insert,
        "day_wise.csv": day_wise_insert,
        "full_grouped.csv": full_grouped_insert,
        "usa_county_wise.csv": usa_county_wise_insert,
        "worldometer_data.csv": worldometer_data_insert
    }

    file.data_folder_path = data_folder_path
    for item in file.get_files_list():
        file_name = os.path.basename(item)

        data = file.get_data_from_csv(item)

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

        data.columns = data.columns.str.lower()

        sql.run_query(mapping.get(file_name), data.to_dict(orient="records"))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="Load every csv from Data folder")
    parser.add_argument("-f", "--file", type=str, help="Load given CSV to related db table")

    args = parser.parse_args()

    if args.all:
        load_all_csv()

    if args.f or args.file:
        ...