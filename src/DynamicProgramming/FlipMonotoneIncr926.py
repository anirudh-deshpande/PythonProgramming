# Solution 1
class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """

        cost_0to1 = [0] * (len(S) + 1)
        cost_1to0 = [0] * (len(S) + 1)
        n = len(S)

        cost_1to0[0] = 0
        for i in range(1, n + 1):
            cost_1to0[i] = cost_1to0[i - 1] + 1 if S[i - 1] == '1' else cost_1to0[i - 1]

        cost_0to1[n] = 0
        for j in range(n - 1, -1, -1):
            cost_0to1[j] = cost_0to1[j + 1] + 1 if S[j] == '0' else cost_0to1[j + 1]

        """
        There will come a position where
        (cost of flipping zeros before that position) + (cost of flipping 1s after that position)
        is minimum
        """
        cost = n
        for k in range(0, n + 1):
            cost = min(cost, cost_1to0[k] + cost_0to1[k])

        return cost


# Solution 2
class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """

        """
        After encountering 1st 1, all the 0's coming after should be flipped
        If the count of 0's (flipped) is greater than count of 1's,
        flip 1's instead
        """

        flipCount = 0
        oneCount = 0

        for i in range(len(S)):
            if S[i] == '0':
                if oneCount > 0:
                    flipCount += 1
            else:
                oneCount += 1

            if flipCount > oneCount:
                flipCount = oneCount

        return flipCount

