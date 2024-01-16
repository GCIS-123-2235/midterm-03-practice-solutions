from random import seed
from question_1 import shuffle_tuple_5
from testing_utils import run_a_test

def test_q1_shuffle_tuple_5_1():
    ''' Test Description'''
    seed(1)
    run_a_test(shuffle_tuple_5, (2, 5, 1, 3, 4), (1, 2, 3, 4, 5))


def test_q1_shuffle_tuple_5_2():
    ''' Test Description'''
    seed(1)
    run_a_test(shuffle_tuple_5, (4, 1, 5, 3, 2), (5, 4, 3, 2, 1))


def test_q1_shuffle_tuple_5_3():
    ''' Test Description'''
    seed(1)
    run_a_test(shuffle_tuple_5, ('4', {1}, 5.1, 3, [1, 2]), (5.1, '4', 3, [1, 2], {1}))


def test_q1_shuffle_tuple_5_4():
    ''' Test Description'''
    seed(101)
    run_a_test(shuffle_tuple_5, (1, 4, 3, 2, 5), (5, 4, 3, 2, 1))


def test_q1_shuffle_tuple_5_5():
    ''' Test Description'''
    seed(101)
    run_a_test(shuffle_tuple_5, (1, 4, 3, 2, 5), (5, 4, 3, 2, 1))
