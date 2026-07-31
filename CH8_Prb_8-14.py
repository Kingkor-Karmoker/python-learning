# code for problem 8.14:
def make_car(manufacturer, model_name, **kwargs):
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model_name
    return kwargs

info = make_car(manufacturer='BMW', model_name='BMW 1998', color= 'Black',)
info2 = make_car('Subaru', 'Outback', color= 'Blue', tow_package= True)

print(info)
print(info2)
