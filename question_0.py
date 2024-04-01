import random

'''
Question 0 (Algorithms) - HARD

Complete the equal_buckets function so that it takes a list of positive numbers and a number of buckets.
equal_buckets should group the numbers in the `numbers` list into `number_of_buckets` buckets.
The sum of each bucket should be about equal.

You can assume that the `numbers` list will always have at least `number_of_buckets` numbers.

For all tests to pass, your function must group numbers into buckets such that, on average,
the ratio of the difference between the largest and smallest sum of the buckets to the difference between 
the largest and smallest number in the list is less than 0.5

For example:
    equal_buckets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) could return [[10, 5, 4], [9, 6, 3], [8, 7, 2, 1]]
    
    That means the buckets have the sums 19, 18, 18 respectively
    The difference between the largest and smallest sum is 19 - 18 = 1
    The difference between the largest and smallest number in the list is 10 - 1 = 9
    Therefore the ratio is 1 / 9 = ~0.11

You may use the sorted function
You man not use the min, max, or sum functions, though you could write your own ;)
Use of imported libraries isnt required, but you may use them if you wish
    
Hint:
    Handle large numbers first
'''
def minimum_bucket_index(buckets: list[list[int]]) -> int:
    min_sum = None
    min_i = 0
    for i in range(len(buckets)):
        sum_bucket = 0
        for number in buckets[i]:
            sum_bucket += number
        if min_sum is None:
            min_sum = sum_bucket
            min_i = i
        if sum_bucket < min_sum:
            min_sum = sum_bucket
            min_i = i
    return min_i


def equal_buckets(numbers: list[int], number_of_buckets: int) -> list:
    '''
    The naive but simplest solution is to sort the numbers in descending order and then add each number to the bucket
    with the smallest sum. This is a greedy algorithm that will not always produce the best results but its average ratio is ~0.1
    '''
    buckets = [[] for _ in range(number_of_buckets)]
    for number in sorted(numbers, reverse=True):
        min_bucket_idx = minimum_bucket_index(buckets)
        buckets[min_bucket_idx].append(number)
    return buckets
