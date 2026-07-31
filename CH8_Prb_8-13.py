# code for problem 8.13:
def build_profile (first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

info = build_profile('Kingkor', 'Karmoker', location ='Dhaka', field='Student')
print(info)
