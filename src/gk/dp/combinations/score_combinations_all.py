import time
import sys

def score_combinations_backtracking(nums, i, target):

    if target < 0:
        return 0

    if target == 0:
        return 1

    count = 0
    for j in range(i, len(nums)):
        count += score_combinations_backtracking(nums, j, target - nums[j])

    return count


def score_combinations_top_down_memoization(nums, i, target, cache):

    if target < 0:
        return 0

    if target == 0:
        return 1

    if cache[i][target] != 0:
        return cache[i][target]

    count = 0
    for j in range(i, len(nums)):
        count += score_combinations_top_down_memoization(nums, j, target-nums[j], cache)

    cache[i][target] = count
    return cache[i][target]




def score_combinations_bottom_up_iterative(nums, target):
    """
    If we observe above, the cache is being built as follows:
        - for every 'num' in nums, we build cache until target
    """

    cache = [0] * (target+1)

    # Required when cur_target == nums[i]
    cache[0] = 1

    for i in range(len(nums)):
        for cur_target in range(1, target+1):

            if cur_target >= nums[i]:
                cache[cur_target] += cache[cur_target - nums[i]]

    print('\n', cache)
    return cache[-1]


if __name__ == "__main__":
    nums = [1,2,3,4,6]
    target = 100

    start = time.time_ns()
    print(score_combinations_backtracking(nums, 0, target))
    print("Time backtracking: ", (time.time_ns()-start)/1000000000)

    start = time.time_ns()
    cache = [[0] * (target+1) for _ in range(len(nums))]
    print('\n', score_combinations_top_down_memoization(nums, 0, target, cache))
    print("Time memoization: ", (time.time_ns() - start) / 1000000000)

    for row in cache:
        print(row)

    start = time.time_ns()
    print('\n', score_combinations_bottom_up_iterative(nums, target))
    print("Time memoization: ", (time.time_ns() - start) / 1000000000)
