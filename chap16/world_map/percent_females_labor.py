import csv

import pygal
import pygal.maps.world as pywm

from get_country_code import get_cc

# Gets data from csv file
filename = 'chap16\\world_map\\world_data\\female_labor.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    percent_row = header_row.index('2019')
    country_row = header_row.index('ï»¿"Country Name"')

    # Gets country code and percent in a dict
    labor_percents = {}
    for row in reader: 
        if row[percent_row]:
            # Gets labor percent
            percent = int(float(row[percent_row]))
            
            # Gets country code
            country_name = row[country_row] 
            code = get_cc(country_name)
            if code == None:
                continue

            # appends code and percent to dict
            labor_percents[code] = percent
    
    # Puts the countries percentages in categories
    less_20, upto_30, upto_40, upto_50, above_50 = {}, {}, {}, {}, {}
    for code, percent in labor_percents.items():
        if percent < 20:
            less_20[code] = percent
        elif percent < 30:
            upto_30[code] = percent
        elif percent < 40:
            upto_40[code] = percent
        elif percent < 50:
            upto_50[code] = percent
        elif percent >= 50:
            above_50[code] = percent            
            
# Builds world map
wm = pywm.World()
wm.title = "Percentage of women in the labor force in 2019"
wm.add('< 20%', less_20)
wm.add('< 30%', upto_30)
wm.add('< 40%', upto_40)
wm.add('< 50%', upto_50)
wm.add('>= 50%', above_50)

wm.render_to_file('women_labor_percentage.svg')