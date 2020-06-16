import json

import pygal
import pygal.maps.world as pywm
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

from get_country_code import get_cc

# Get data from json file
filename = 'chap16\\world_map\\world_data\\world_gdp.json'
with open(filename) as f:
    pop_data = json.load(f)


# Puts country code and gdp in dict
country_gdps = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == 2016:
        # Gets country code
        country_name = pop_dict['Country Name'] 
        code = get_cc(country_name)

        # Gets gdp
        gdp = int(float(pop_dict['Value']))

        # Appends code and gdp
        country_gdps[code] = gdp

# Creates map
wm = pywm.World()
wm.title = 'World GDP by Country'
wm.add('2016 GDP', country_gdps)

wm.render_to_file('world_gdp.svg')
