"""
Question 3 (Reference Types)

Description:
    Implement new_list_reference so that given some list, it returns a_list as a reference type (not a new list)

Example:
    a_list = [1, 2, 3]
    b_list = new_list_reference(a_list)
    b_list[2] = 'a'
    print(a_list) -> [1, 2, 'a']

"""

def new_list_reference(a_list: list):
    return a_list
