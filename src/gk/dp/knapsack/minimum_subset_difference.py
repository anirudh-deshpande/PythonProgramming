import math

def minimum_subset_difference_backtrack(nums, target, result, i):

    if i >= len(nums) or result >= target:
        return result

    with_cur_num = 0
    if target - nums[i] >= 0:
        with_cur_num = minimum_subset_difference_backtrack(nums, target - nums[i], result + nums[i], i+1)

    without_cur_num = minimum_subset_difference_backtrack(nums, target, result, i+1)

    return max(with_cur_num, without_cur_num)


def minimum_subset_difference_top_down(nums, target, result, i, cache):

    if i >= len(nums) or result >= target:
        return result

    if cache[i][target] != -1:
        return cache[i][target]

    with_cur_num = 0
    if target - nums[i] >= 0:
        with_cur_num = minimum_subset_difference_top_down(nums, target - nums[i], result + nums[i], i + 1, cache)

    without_cur_num = minimum_subset_difference_top_down(nums, target, result, i + 1, cache)

    cache[i][target] = max(with_cur_num, without_cur_num)
    return max(with_cur_num, without_cur_num)


def minimum_subset_difference_bottom_up_dp(nums, target):

    cache = [[0] * (target+1) for _ in range(-1, len(nums))]

    for i in range(1, len(nums)+1):
        for t in range(1, target+1):

            with_cur_num = 0
            if t - nums[i-1] >= 0:
                with_cur_num = nums[i-1] + cache[i - 1][t - nums[i - 1]]

            without_cur_num = cache[i-1][t]

            cache[i][t] = max(with_cur_num, without_cur_num)

    print(cache)
    return cache[-1][-1]


if __name__ == "__main__":
    nums = [1, 3, 100, 4, 1, 3, 100, 4, 1, 3, 100, 4, 1, 3, 100, 4, 1, 3, 100, 4, 1, 3, 100, 4, 1, 3, 100, 4, 1, 3, 100, 4, 1, 3, 100, 4, 1, 3, 100, 4, 1, 3, 100, 4, 1, 3, 100, 4, 1, 3, 100, 4, 1, 3, 100, 4, 1, 3, 100, 4, 1, 3, 100, 4, 1, 3, 100, 4, 1, 3, 100, 4, 1, 3, 100, 4, 1, 3, 100, 4, 1, 3, 100, 4, 1, 3, 100, 4]
    # nums = [1, 3, 100, 4]
    addition = sum(nums)
    target = int(math.ceil(addition / 2))

    # set_1_sum = minimum_subset_difference_backtrack(nums, target, 0, 0)
    # set_2_sum = addition - set_1_sum
    # print(abs(set_2_sum - set_1_sum))

    cache = [[-1] * (target+1) for _ in range(len(nums))]
    set_1_sum_top_down_dp = minimum_subset_difference_top_down(nums, target, 0, 0, cache)
    print(addition, 2 * set_1_sum_top_down_dp)
    print(abs(addition - 2 * set_1_sum_top_down_dp))

    set_1_sum_bottom_up_dp = minimum_subset_difference_bottom_up_dp(nums, target)

    print(addition, 2 * set_1_sum_bottom_up_dp)
    print(abs(addition - 2 * set_1_sum_bottom_up_dp))
