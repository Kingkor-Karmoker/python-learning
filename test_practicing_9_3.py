# code for testing practice:
from CH9_Prb_9_3 import *
def test_greet_user():
    user = User('Kingkor', "Karmoker", '14 apr 2003', 'student')
    assert user.first_name == 'Kingkor'
    assert user.last_name == 'Karmoker'
    assert user.dob == '14 apr 2003'
    assert user.profession == 'student'
