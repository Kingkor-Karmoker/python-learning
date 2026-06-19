# code for problem 6.6:
favourite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}
f_l_poll = ['jen', 'kingkor', 'shaily', 'wasik', 'edward', 'deep']

for people in f_l_poll:
    if people in favourite_language.keys():
        print(f"{people.title()}, thanks for taking the poll already")
    else:
        print(f"{people.title()}, kindly give your response of the poll")
