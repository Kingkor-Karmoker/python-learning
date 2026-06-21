# code for problem 6.8:
favourite_places = {
    'Wasik': ['cox bazar', 'Shajek valley', 'Bogra'],
    'Shaily': ['Norshingdi', 'australia', 'Rangamati'],
    'deep': ['Barisal']
}

for k, v in favourite_places.items():
    print(f"{k.title()} whats your favourite places?")
    print(f"{k.title()}'s favourite places:")
    for p in v:
        print(f"\t{p}")
    print('\n')
