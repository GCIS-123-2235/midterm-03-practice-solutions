import random

'''
Question 1 (Tuples)

Given a tuple with 5 values of unknown types, complete the shuffle_tuple function so that it returns a copy of a_tuple
with its elements randomly shuffled

Example:
    shuffle_tuple_5((1, 2, 3, 4, 5)) -> (2, 5, 1, 3, 4)

***************** MUST USE TUPLES *****************
***************** CANNOT USE TUPLE CASTING *****************
'''
def shuffle_tuple_5(a_tuple: tuple) -> tuple:
    random_indexes = []
    while len(random_indexes) < len(a_tuple):
        rand_number = random.randint(0, len(a_tuple) - 1)
        if rand_number not in random_indexes:
            random_indexes.append(rand_number)

    return (a_tuple[random_indexes[0]], a_tuple[random_indexes[1]], a_tuple[random_indexes[2]], a_tuple[random_indexes[3]], a_tuple[random_indexes[4]])
