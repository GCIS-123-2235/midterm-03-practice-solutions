from question_3 import new_list_reference


def test_q3_new_list_reference_1():
    ''' Test Description'''
    a_list = [1, 2, 3]
    b_list = new_list_reference(a_list)
    b_list[2] = 'a'

    assert a_list == [1, 2, 'a']



def test_q3_new_list_reference_2():
    a_list = [1, 2, 3]
    b_list = new_list_reference(a_list)
    a_list[2] = 'a'

    assert b_list == [1, 2, 'a']
