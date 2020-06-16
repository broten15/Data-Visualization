from pygal.maps.world import COUNTRIES

def get_cc(country_name):
    """Turns country name into country code for map"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        elif country_name == 'Bolivia':
            return 'bo'
        elif country_name == 'Dominica':
            return 'do'
        elif country_name == 'Egypt, Arab Rep.':
            return 'eg'
        elif country_name == 'Hong Kong SAR, China':
            return 'hk'     
        elif country_name == 'Korea, Dem. People’s Rep.':
            return 'kp' 
        elif country_name == 'Korea, Rep.':
            return 'kr'
        elif country_name == 'Macao SAR, China':
            return 'mo'                          
    return None
