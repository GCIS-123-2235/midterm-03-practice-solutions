from question_7 import n_primes, filter_words_list, chunk_string, chunk_string_fill
from testing_utils import run_a_test


def test_q7_a_n_primes_test_1():
    run_a_test(n_primes, [2, 3, 5, 7], 10)


def test_q7_a_n_primes_test_2():
    run_a_test(n_primes, [2, 3, 5, 7], 11)


def test_q7_a_n_primes_test_3():
    run_a_test(n_primes, [2, 3, 5, 7, 11], 12)


def test_q7_a_n_primes_test_4():
    run_a_test(n_primes, [], 0)


def test_q7_b_filter_words_list_test_1():
    run_a_test(filter_words_list, ['reader', 'camera'], ['missippi', 'reader', 'camera', 'tips', 'trip', 'zombie'], ['i', 'p'])


def test_q7_b_filter_words_list_test_2():
    run_a_test(filter_words_list, ['missippi', 'reader', 'camera', 'tips', 'trip', 'zombie'], ['missippi', 'reader', 'camera', 'tips', 'trip', 'zombie'], [])


def test_q7_b_filter_words_list_test_3():
    run_a_test(filter_words_list, [], ['missippi', 'reader', 'camera', 'tips', 'trip', 'zombie'], ['a', 'e', 'p'])


def test_q7_b_filter_words_list_test_4():
    run_a_test(filter_words_list, [], [], ['a', 'e', 'i', 'o', 'u', 'y'])


def test_q7_c_chunk_string_test_1():
    run_a_test(chunk_string, [['H', 'e', 'l'], ['l', 'o', ' '], ['W', 'o', 'r'], ['l', 'd']], 'Hello World', 3)


def test_q7_c_chunk_string_test_2():
    run_a_test(chunk_string, [['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']], 'Hello World', 11)


def test_q7_c_chunk_string_test_3():
    run_a_test(chunk_string, [['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l'], ['d']], 'Hello World', 10)


def test_q7_c_chunk_string_test_4():
    run_a_test(chunk_string, [['H'], ['e'], ['l'], ['l'], ['o'], [' '], ['W'], ['o'], ['r'], ['l'], ['d']], 'Hello World', 1)


def test_q7_d_chunk_string_fill_test_1():
    run_a_test(chunk_string_fill, [['H', 'e', 'l'], ['l', 'o', ' '], ['W', 'o', 'r'], ['l', 'd', 'a']], 'Hello World', 3, 'a')


def test_q7_d_chunk_string_fill_test_2():
    run_a_test(chunk_string_fill, [['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']], 'Hello World', 11, 'a')


def test_q7_d_chunk_string_fill_test_3():
    run_a_test(chunk_string_fill, [['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l'], ['d', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']], 'Hello World', 10, 'a')


def test_q7_d_chunk_string_fill_test_4():
    run_a_test(chunk_string_fill, [['H'], ['e'], ['l'], ['l'], ['o'], [' '], ['W'], ['o'], ['r'], ['l'], ['d']], 'Hello World', 1, 'a')


def test_q7_d_chunk_string_fill_test_5():
    run_a_test(chunk_string_fill, [['H', 'e', 'l'], ['l', 'o', ' '], ['W', 'o', 'r'], ['l', 'd', ' ']], 'Hello World', 3, ' ')
