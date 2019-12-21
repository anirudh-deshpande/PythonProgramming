import math


class Solution(object):
    def canKokoFinish(self, num, hours, piles, n):
        total = sum(piles)
        h = total / num
        return h < hours

    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """

        if not piles or H == 0:
            return 0

        start = sum(piles) * 1.0 / H
        end = max(piles)
        n = len(piles)

        if start > end:
            return end

        while start < end:
            mid = start + (end - start) // 2

            if self.canKokoFinish(mid, H, piles, n):
                end = mid
            else:
                start = mid + 1

        return int(math.ceil(mid))


piles = [332484035,524908576,855865114,632922376,222257295,690155293,112677673,679580077,337406589,290818316,877337160,901728858,679284947,688210097,692137887,718203285,62945572,941802184]
H = 823855818
print Solution().minEatingSpeed(piles, H)