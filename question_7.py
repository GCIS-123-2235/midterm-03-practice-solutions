def is_prime(n: int) -> bool:
    """
    Provided helper function that returns True if a number is prime (only factors are 1 and itself)
    And returns False if the number is a composite
    """
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


"""
Question 7.a (List Comprehension) EASY
complete n_primes to use list comprehension to make a list of prime numbers up to
n (but not including n)

you must use list comprehension and n_primes.
must be one line of code (excluding "def" line)

is_prime has been provided that returns true if a number is prime and false if a number is not prime

Examples:
    n_primes(10) -> [2, 3, 5, 7]
    n_primes(11) -> [2, 3, 5, 7]
    n_primes(12) -> [2, 3, 5, 7, 11]
"""
def n_primes(n: int) -> list:
    return [i for i in range(n) if is_prime(i)]


'''
Question 7.b (List Comprehension) HARD

Complete the function filter_words_list given a list of words and a list of letters you want to exclude
so that it returns a new list of words where each word does not contain the letters in excluded.

Examples:
    filter_words_list(['missippi', 'reader', 'camera', 'tips', 'trip', 'zombie'], ['i', 'p']) -> ['reader', 'camera']

***************** MUST USE LIST COMPREHENSION *****************
If you make a helper function, this must also use list comprehension.
'''
def filter_words_list(words: list[str], excluded: list[str]) -> list[str]:
    return [word for word in words if not [letter for letter in excluded if letter in word]]


"""
Question 7.c (List Comprehension) HARD

Write a function that chunks a strings into equal sized portions.
It should return a 2D list with each row being a list of characters.
You must use a list comprehension and slicing to do this. Your function should be 1 line of code.

Note: the last row may not be the same size as the others because a word length may not be evenly divisible by the chunk size.

Hint: It may be easier to write the function using a for loop and then convert it to list comprehension.

Example:
    chunk_string('Hello World', 3) -> [['H', 'e', 'l'], ['l', 'o', ' '], ['W', 'o', 'r'], ['l', 'd']]
"""
def chunk_string(string: str, chunk_size: int) -> list:
    return [list(string[i:i + chunk_size]) for i in range(0, len(string), chunk_size)]


"""
Question 7.d (List Comprehension) EXTRA HARD

Improve chunk_string so that it can handle a string that is not evenly divisible by the chunk size.
It should fill the last row with the a fill_character until it is the same size as the other rows.

chunk_string_fill should remain one line of code

Example:
    chunk_string_fill('Hello World', 3, 'a') -> [['H', 'e', 'l'], ['l', 'o', ' '], ['W', 'o', 'r'], ['l', 'd', 'a']]
"""
def chunk_string_fill(string: str, chunk_size: int, fill_character: str = '') -> list:
    return [list(string[i:i + chunk_size]) + ([fill_character] * (chunk_size - len(string[i:i + chunk_size]))) for i in range(0, len(string), chunk_size)]
