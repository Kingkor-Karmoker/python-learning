# testing code for problem CH11_Prb_11_1_city_functions:
from CH11_Prb_11_1_city_functions import city

def test_city_function():
    name = city('Dhaka', 'Bangladesh')
    assert name == "Dhaka, Bangladesh"
