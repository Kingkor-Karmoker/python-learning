# code for problem 6.12:
# Copied code from 6.11 :
# NOW JUST ADDING SOME NEW KEY AND VALUES:
cities = {
    'Barisal': {
        'Country': 'Bangladesh',
        'population': '9.3 million',
        'fact': "Known as 'Venice of west'",
        'River': 'Kirtonkhola',
        'Tourist spot': 'Kuakata'
    },
    'Dhaka': {
        'Country': 'Bangladesh',
        'population': '36.6 million',
        'fact': "The capital of Bangladesh",
        'River': 'Buriganga',
        'Tourist spot': 'Puran Dhaka'
    },
    'Tokyo': {
        'Country': 'Japan',
        'population': '37.5 million',
        'fact': "Worlds most populous metropolitan",
        'River': 'Sumida',
        'Tourist spot': 'Tokyo tower'
    }
}

for city, info in cities.items():
    print(f"\nCity name: {city.title()}")
    print("City info:")
    for key, val in info.items():
        print(f"\t {key.title()}: {val}")
