import functools


class Solution(object):
    def minimax_max_of_p1_score(self, nums, left, right, cache):

        """
        For Player 1, the maximum score possible is:
            -> If I choose greedily, the other player also chooses greedily.
            -> In this move I choose max, I am assuming that in next move he is choosing max.
            -> The available one to me in the next move is the min of possible next moves

        """

        if left > right:
            return 0

        if cache[left][right] != -1:
            return cache[left][right]

        score = max(
            nums[left] + min(self.minimax_max_of_p1_score(nums, left + 1, right - 1, cache),
                             self.minimax_max_of_p1_score(nums, left + 2, right, cache)),
            nums[right] + min(self.minimax_max_of_p1_score(nums, left, right - 2, cache),
                              self.minimax_max_of_p1_score(nums, left + 1, right - 1, cache))
        )

        cache[left][right] = score
        return score

    def minimax_max_of_p1_score_bottom_up(self, nums):
        """
        1. Going inside-out here.
        2. In the above recursion,
        picking actually happens when there are just 2 numbers available for grab

        Hence, we build the solution this way
          -> (2 side by side numbers in question)
          -> expanding it to 3 numbers, then 4 numbers and so on

        At every step, use the values computed at previous step.
        """

        cache = [[0] * (len(nums)) for _ in range(len(nums))]

        for i in range(len(nums)):
            cache[i][i] = nums[i]

        n = len(nums)
        # Optimize
        for right in range(len(nums)):
            for left in range(right - 1, -1, -1):

                possible_right_left_next = \
                    cache[left + 1][right - 1] if (left + 1) < n and (right - 1) >= 0 else 0

                possible_left_next = \
                    cache[left + 2][right] if (left + 2) < n and right >= 0 else 0

                possible_right_next = \
                    cache[left][right - 2] if left < n and (right - 2) >= 0 else 0

                cache[left][right] = max(
                    nums[left] + min(possible_right_left_next, possible_left_next),
                    nums[right] + min(possible_right_left_next, possible_right_next)
                )

        for row in cache:
            print(row)

        return cache[0][-1]

    def PredictTheWinner(self, nums):

        total = functools.reduce(lambda x, y: x + y, nums, 0)

        cache = [[-1] * len(nums) for _ in range(len(nums))]
        score_top_down = self.minimax_max_of_p1_score(nums, 0, len(nums) - 1, cache)
        score_bottom_up = self.minimax_max_of_p1_score_bottom_up(nums)

        print(score_bottom_up)
        assert score_bottom_up == score_top_down

        # print cache, score
        if score_bottom_up * 2 >= total:
            return True

        return False


if __name__ == "__main__":
    # nums = [1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2]
    nums = [1, 5, 233, 7]
    print("Is player-1 the winner? ", Solution().PredictTheWinner(nums))


