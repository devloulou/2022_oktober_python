create table if not exists country_wise_latest 
(country_region text,
Confirmed integer,
Deaths integer,
Recovered integer,
Active integer,
new_cases integer,
new_deaths integer,
new_recovered integer,
death_100_cases numeric,
recovered_100_cases numeric,
deaths_100_recovered numeric,
confirmed_last_week integer,
week_1_change integer,
week_1_increase numeric,
who_region text);

------------------------
create table if not exists covid_19_clean_complete  (province_state text,
country_region text,
Lat numeric,
Long numeric,
ddate text,
Confirmed integer,
Deaths integer,
Recovered integer,
Active integer,
who_region text);

------------------------
create table if not exists day_wise  (ddate text,
Confirmed integer,
Deaths integer,
Recovered integer,
Active integer,
new_cases integer,
new_deaths integer,
new_recovered integer,
death_100_cases numeric,
recovered_100_cases numeric,
deaths_100_recovered numeric,
no_of_countries integer);

------------------------
create table if not exists full_grouped  (ddate text,
country_region text,
Confirmed integer,
Deaths integer,
Recovered integer,
Active integer,
new_cases integer,
new_deaths integer,
new_recovered integer,
who_region text);

------------------------
create table if not exists  usa_county_wise (UID integer,
iso2 text,
iso3 text,
code3 integer,
FIPS numeric,
Admin2 text,
Province_State text,
Country_Region text,
Lat numeric,
Long_ numeric,
Combined_Key text,
ddate text,
Confirmed integer,
Deaths integer);

------------------------
create table if not exists worldometer_data  (country_region text,
Continent text,
Population numeric,
TotalCases integer,
NewCases numeric,
TotalDeaths numeric,
NewDeaths numeric,
TotalRecovered numeric,
NewRecovered numeric,
ActiveCases numeric,
serious_critical numeric,
tot_cases_1m_pop numeric,
deaths_1m_pop numeric,
TotalTests numeric,
tests_1M_pop numeric,
who_region text);

------------------------
