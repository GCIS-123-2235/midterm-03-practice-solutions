from random import randint

from question_0 import equal_buckets

def random_lists(num_lists: int):
    result = []
    for _ in range(num_lists):
        size = randint(10, 150)
        result.append([randint(1, size) for _ in range(size)])
    return result


def test_q0_equal_buckets_ratio():
    rand_lists = random_lists(752)
    ratio = 0
    for numbers_list in rand_lists:
        n_buckets = randint(2, len(numbers_list) - 1)
        res = equal_buckets(numbers_list, n_buckets)
        bucket_sums = [sum(bucket) for bucket in res]
        sum_diff = max(bucket_sums) - min(bucket_sums)
        num_diff = max(numbers_list) - min(numbers_list)
        ratio += (sum_diff / num_diff)
    avg_ratio = ratio / len(rand_lists)
    assert avg_ratio < 0.5, f"Ratio: {avg_ratio}"
