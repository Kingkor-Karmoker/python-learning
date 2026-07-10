# code for problem 8.6:
def city_country(city_name, country_name):
    """ returning city and country name """
    city_country = f"{city_name}, {country_name}"
    return city_country

name = city_country('Dhaka', 'Bangladesh')
print(name)
name = city_country('Mumbai', 'India')
print(name)
name = city_country(city_name= 'Delhi', country_name= 'India')
print(name)
