def combinationSumTopDown(nums, target, cache):
    """
    Complexity: O(target ^ n) times
    """
    if target < 0:
        return 0  # correct?

    if target == 0:
        return 1

    count = 0
    for i in range(len(nums)):
        count += combinationSumTopDown(nums, target - nums[i], cache)

    return count

def combinationSumTopDownWithDP(nums, target, cache):
    """
    DP Complexity: O(target * n) times
    Why O(target * n)?
        - The parameter 'target' takes values from 'target' until '0'.
        - For each of these values, we invoke the same function 'n' times
    """
    if target < 0:
        return 0

    if target == 0:
        return 1

    if cache[target] != -1:
        return cache[target]

    count = 0
    for i in range(len(nums)):
        count += combinationSumTopDownWithDP(nums, target - nums[i], cache)

    cache[target] = count
    return cache[target]


def combinationSumBottomUp(nums, target):
    """
    DP Complexity: O(target * n) times
    """
    cache = [0] * (target + 1)

    #  This helps in the cases where num = target, as there is 1 way to choose here.
    cache[0] = 1

    for t in range(1, target + 1):
        count = 0
        for num in nums:

            # Below condition is implicit
            # if t-num < 0:
            #     continue

            if t - num >= 0:
                count += cache[t - num]

        cache[t] = count

    return cache[target]


if __name__ == "__main__":

    target = 100
    nums = [1,2,3,4,6]
    ans = 34332

    cache = [-1] * (target + 1)
    print(combinationSumTopDownWithDP(nums, target, cache))