class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """

        low = 0
        high = 0
        cur_sum = 0
        count = 0

        while high < N + 1:

            if 2 * high > N:
                break

            cur_sum += high

            while cur_sum >= N:
                cur_sum -= low
                low += 1

                if cur_sum == N:
                    count += 1
                    print count, high

            high += 1

        return count


print Solution().consecutiveNumbersSum(1000000000)
