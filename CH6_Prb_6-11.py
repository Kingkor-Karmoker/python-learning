# code for problem 6.11:
cities = {
    'Barisal': {
        'Country': 'Bangladesh',
        'population': '9.3 million',
        'fact': "Known as 'Venice of west'"
    },
    'dhaka': {
        'Country': 'Bangladesh',
        'population': '36.6 million',
        'fact': "The capital of Bangladesh"
    },
    'Tokyo': {
        'Country': 'Japan',
        'population': '37.5 million',
        'fact': "Worlds most populous metropolitan"
    }
}

for city, info in cities.items():
    print(f"City name: {city.title()}")
    print("City info:")
    for key, val in info.items():
        print(f"\t {key.title()}: {val}")
    print('\n')
