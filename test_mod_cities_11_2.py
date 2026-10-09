# testing code for problem 11.2:
from CH11_Prb_11_2__mod_city_functions import city
def test_city_function():
    name = city('Dhaka', 'Bangladesh')
    assert name == "Dhaka, Bangladesh"

def test_city_function_population():
    name = city('Dhaka', 'Bangladesh',  36000000)
    assert name == "Dhaka, Bangladesh - population 36000000"
