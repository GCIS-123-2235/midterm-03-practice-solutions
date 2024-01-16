'''
Question 2 (Sets)

Complete the function one_but_not_both so that it finds and returns the xor of set_a and set_b.

An XOR of two sets returns a set of values that are in either set but excludes values that are in both.
The XOR of two booleans results in True if one of the values is True but not both.

You are not allowed to use python's built in XOR function or the operator (^)

Example:
    one_but_not_both({1, 2, 3, 4, 5}, {4, 5, 6, 7, 8}) -> {1, 2, 3, 6, 7, 8}
'''
def one_but_not_both(set_a: set[int], set_b: set[int]) -> set[int]:
    result_set = set()
    for element in set_a:
        if element not in set_b:
            result_set.add(element)
    for element in set_b:
        if element not in set_a:
            result_set.add(element)
    return result_set
