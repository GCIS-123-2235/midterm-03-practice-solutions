from question_2 import one_but_not_both
from testing_utils import run_a_test

def test_q2_one_but_not_both_1():
    ''' Test Description'''
    run_a_test(one_but_not_both, {1, 2, 3, 6, 7, 8}, {1, 2, 3, 4, 5}, {4, 5, 6, 7, 8})


def test_q2_one_but_not_both_2():
    ''' Test Description'''
    run_a_test(one_but_not_both, {'a', 'b', 'c', 'f', 'g', 'h'}, {'a', 'b', 'c', 'd', 'e'}, {'d', 'e', 'f', 'g', 'h'})


def test_q2_one_but_not_both_3():
    ''' Test Description'''
    run_a_test(one_but_not_both, {1, 2, 3, 4, 5}, {1, 2, 3, 4, 5}, {})


def test_q2_one_but_not_both_4():
    ''' Test Description'''
    run_a_test(one_but_not_both, {4, 5, 6, 7, 8}, {}, {4, 5, 6, 7, 8})


def test_q2_one_but_not_both_5():
    ''' Test Description'''
    run_a_test(one_but_not_both, {2, 3, 4, 5}, {1, 2, 3, 4, 5}, {1})


def test_q2_one_but_not_both_6():
    ''' Test Description'''
    run_a_test(one_but_not_both, {5, 6, 7, 8}, {4}, {4, 5, 6, 7, 8})


def test_q2_one_but_not_both_7():
    ''' Test Description'''
    run_a_test(one_but_not_both, {2, '3', 4, 5}, {1, 2, '3', 4, 5}, {1})


def test_q2_one_but_not_both_8():
    ''' Test Description'''
    run_a_test(one_but_not_both, {5, 6, 7, 8}, {'4'}, {'4', 5, 6, 7, 8})
