from question_4 import sort_dictionary_by_value
from testing_utils import run_a_test

def test_q4_sort_dictionary_by_value_1():
    run_a_test(sort_dictionary_by_value, {'b': 10, 'c': 11, 'a': 92}, {'a': 92, 'b': 10, 'c': 11})


def test_q4_sort_dictionary_by_value_2():
    run_a_test(sort_dictionary_by_value, {'c': 10, 'b': 11, 'a': 92}, {'a': 92, 'b': 11, 'c': 10})


def test_q4_sort_dictionary_by_value_3():
    run_a_test(sort_dictionary_by_value, {}, {})


def test_q4_sort_dictionary_by_value_4():
    run_a_test(sort_dictionary_by_value, {'longer string': 0, 'short': 1, 'other_short': 1}, {'longer string': 0, 'short': 1, 'other_short': 1})
