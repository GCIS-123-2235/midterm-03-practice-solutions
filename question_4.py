"""
Question 4 (Sort Keys):

Description:
    While Sets may not have an order to them, Dictionaries do. Key-value pairs in a dictionary appear in the order that
    the keys were added to the dictionary. That said, given a dictionary that has string/integer key/value pairs,
    sort it in ascending order based on the integer value for each key.

Example:
    sort_dictionary_by_value({'a': 92, 'b': 10, 'c': 11}) -> {'b': 10, 'c': 11, 'a': 92}
    sort_dictionary_by_value({'longer string': 0, 'short': 1, 'other_short': 1}) -> {'longer string': 0, 'short': 1, 'other_short': 1}
"""
def value_sort_key(pairs: list) -> int:
    return pairs[1]


def sort_dictionary_by_value(letter_to_int_dict: dict[str, int]):
    pairs = []
    for key in letter_to_int_dict:
        pairs.append([key, letter_to_int_dict[key]])
    pairs = sorted(pairs, key=value_sort_key)

    res_dict = dict()
    for pair in pairs:
        res_dict[pair[0]] = pair[1]
    return res_dict
