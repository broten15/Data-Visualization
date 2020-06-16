import json

import pygal
import pygal.maps.world as pywm
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

from get_country_code import get_cc


# Gets data from json file
filename = 'chap16\\world_map\\world_data\\population.json'
with open(filename) as f:
    pop_data = json.load(f)

# Puts country code and population in dict
country_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == 2010:
        # Gets code
        country_name = pop_dict['Country Name']
        code = get_cc(country_name)
        if not code:
            print(country_name)
        
        # Gets population
        population = int(float(pop_dict['Value']))

        # Appends code and population
        country_populations[code] = population

# Adds coutntry to 1 of 3 dicts based on their population
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in country_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# Creates map
wm_style = RS('#336699', base_style=LCS)
wm = pywm.World(style=wm_style)
wm.title = 'World Population in 2010 by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1b', cc_pops_2)
wm.add('>1b', cc_pops_3)

wm.render_to_file('world_population.svg')

