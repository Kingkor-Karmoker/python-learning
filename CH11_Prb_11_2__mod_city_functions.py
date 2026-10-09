# modified code for prob 11.2:
def city(city_name, country_name, population = ''):
    if population:
        name = f"{city_name}, {country_name} - population {population}"
        return name
    else:
        name = f"{city_name}, {country_name}"
        return name
