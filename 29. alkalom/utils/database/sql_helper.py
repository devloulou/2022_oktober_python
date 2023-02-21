country_wise_latest_insert = """INSERT INTO public.country_wise_latest
(country_region, confirmed, deaths, recovered, active, new_cases, new_deaths, new_recovered, death_100_cases, recovered_100_cases, deaths_100_recovered, confirmed_last_week, week_1_change, week_1_increase, who_region)
VALUES(:country_region, :confirmed, :deaths, :recovered, :active, :new_cases, :new_deaths, :new_recovered, :death_100_cases, :recovered_100_cases, :deaths_100_recovered, :confirmed_last_week, :week_1_change, :week_1_increase, :who_region);"""


covid_19_clean_complete_insert = """
INSERT INTO public.covid_19_clean_complete
(province_state, country_region, lat, long, ddate, confirmed, deaths, recovered, active, who_region)
VALUES(:province_state, :country_region, :lat, :long, :ddate, :confirmed, :deaths, :recovered, :active, :who_regionprovince_state, :country_region, :lat, :long, :ddate, :confirmed, :deaths, :recovered, :active, :who_region);
"""

day_wise_insert = """
INSERT INTO public.day_wise
(ddate, confirmed, deaths, recovered, active, new_cases, new_deaths, new_recovered, death_100_cases, recovered_100_cases, deaths_100_recovered, no_of_countries)
VALUES(:ddate, :confirmed, :deaths, :recovered, :active, :new_cases, :new_deaths, :new_recovered, :death_100_cases, :recovered_100_cases, :deaths_100_recovered, :no_of_countries);
"""

full_grouped_insert = """
INSERT INTO public.full_grouped
(ddate, country_region, confirmed, deaths, recovered, active, new_cases, new_deaths, new_recovered, who_region)
VALUES(:ddate, :country_region, :confirmed, :deaths, :recovered, :active, :new_cases, :new_deaths, :new_recovered, :who_region);

"""

usa_county_wise_insert = """
INSERT INTO public.usa_county_wise
(uid, iso2, iso3, code3, fips, admin2, province_state, country_region, lat, long_, combined_key, ddate, confirmed, deaths)
VALUES(:uid, :iso2, :iso3, :code3, :fips, :admin2, :province_state, :country_region, :lat, :long_, :combined_key, :ddate, :confirmed, :deaths);

"""

worldometer_data_insert = """
INSERT INTO public.worldometer_data
(country_region, continent, population, totalcases, newcases, totaldeaths, newdeaths, totalrecovered, newrecovered, activecases, serious_critical, tot_cases_1m_pop, deaths_1m_pop, totaltests, tests_1m_pop, who_region)
VALUES(:country_region, :continent, :population, :totalcases, :newcases, :totaldeaths, :newdeaths, :totalrecovered, :newrecovered, :activecases, :serious_critical, :tot_cases_1m_pop, :deaths_1m_pop, :totaltests, :tests_1m_pop, :who_region);
"""