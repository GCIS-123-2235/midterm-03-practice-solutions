from question_6 import employee_to_title
from testing_utils import run_a_test

def test_q6_employee_to_title_1():
    ''' Test Description'''
    title_to_employee_1 = {
        'Sales': ['Jason M.', 'James C.', 'Cannon R.'],
        'CEO': ['Emily A.'],
    }

    result_1 = {
        'Jason M.': {'Sales'},
        'James C.': {'Sales'},
        'Cannon R.': {'Sales'},
        'Emily A.': {'CEO'}
    }
    run_a_test(employee_to_title, result_1, title_to_employee_1)



def test_q6_employee_to_title_2():
    ''' Test Description'''
    title_to_employee_2 = {
        'CEO': ['Emily A.'],
        'Chair Person': ['Arianna P.', 'Emily A.', 'Sam P.']
    }

    result_2 = {
        'Emily A.': {'CEO', 'Chair Person'},
        'Arianna P.': {'Chair Person'},
        'Sam P.': {'Chair Person'}
    }
    run_a_test(employee_to_title, result_2, title_to_employee_2)


def test_q6_employee_to_title_3():
    ''' Test Description'''
    title_to_employee_3 = {
        'Sales': [''],
        'CEO': ['Emily A.'],
    }

    result_3 = {
        '': {'Sales'},
        'Emily A.': {'CEO'}
    }
    run_a_test(employee_to_title, result_3, title_to_employee_3)


def test_q6_employee_to_title_4():
    ''' Test Description'''
    title_to_employee_4 = {
        'CEO': ['Emily A.'],
        '': ['Arianna P.', 'Emily A.', 'Sam P.']
    }

    result_4 = {
        'Emily A.': {'CEO', ''},
        'Arianna P.': {''},
        'Sam P.': {''}
    }
    run_a_test(employee_to_title, result_4, title_to_employee_4)
