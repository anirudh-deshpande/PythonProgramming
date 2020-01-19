def subset_sum_wrong(nums, target):

    for i in range(len(nums)):

        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]

            if sum == target:
                return True

    return False


def subset_sum_backtracking(nums, i, target):

    if target == 0:
        return True

    if i >= len(nums):
        return False

    with_this_item = False
    if target - nums[i] >= 0:
        with_this_item = subset_sum_backtracking(nums, i + 1, target - nums[i])

    without_this_item = subset_sum_backtracking(nums, i + 1, target)

    return with_this_item or without_this_item



def subset_sum_top_down_dp(nums, i, target, cache):

    if target == 0:
        return True

    if i >= len(nums):
        return False

    if cache[i][target] != -1:
        return cache[i][target]

    with_this_item = False

    if target - nums[i] >= 0:
        with_this_item = subset_sum_top_down_dp(nums, i+1, target - nums[i], cache)

    without_this_item = subset_sum_top_down_dp(nums, i+1, target, cache)

    cache[i][target] = with_this_item or without_this_item
    return cache[i][target]


def subset_sum_bottom_up_iterative(nums, target):

    cache = [[False] * (target+1) for _ in range(len(nums)+1)]
    cache[0][0] = True

    for i in range(1, len(nums)+1):
        for t in range(1, target+1):

            with_cur_num = False
            if t - nums[i-1] >= 0:
                with_cur_num = cache[i - 1][t - nums[i-1]]

            without_cur_num = cache[i - 1][t - 1]

            cache[i][t] = with_cur_num or without_cur_num

    return cache[-1][-1]


if __name__ == "__main__":
    nums = [1, 3, -4, 8]
    target = -1

    print(subset_sum_backtracking(nums, 0, target))

    cache = [[-1] * (target+1) for _ in range(len(nums))]
    print(subset_sum_top_down_dp(nums, 0, target, cache))

    print(subset_sum_bottom_up_iterative(nums, target))




