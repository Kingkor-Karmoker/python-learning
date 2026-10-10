# test code for problem 11.3:
from CH11_Prb_11_13_class_employe import Employee

def test_give_default_raise():
    employee = Employee('Kingkor', 'Karmoker', 90000)
    employee.giveRaise()
    assert employee.salary == 95000

def test_give_custom_raise():
    employee = Employee('Kingkor', 'Karmoker', 90000)
    employee.giveRaise(9000)
    assert employee.salary == 99000
