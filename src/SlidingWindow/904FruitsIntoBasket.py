from collections import defaultdict


class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """

        max_two = 0

        low = 0
        high = 0
        count = 0

        frequency = defaultdict(int)

        while high < len(tree):

            if frequency[tree[low]] == 0:
                count += 1

            frequency[tree[low]] += 1

            if count > 2:
                max_two = max(max_two, high - low)

                while low <= high:

                    frequency[tree[low]] -= 1

                    if frequency[tree[low]] == 0:
                        count -= 1
                        break

                    low += 1

            high += 1

        return max(max_two, high - low)
