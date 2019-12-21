class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        start = 0
        zeros = 0
        max_window = 0

        for end in range(len(A)):
            if A[end] == 0:
                zeros += 1

            if zeros > K:
                while A[start] != 0:
                    start += 1

                start += 1
                zeros -= 1

            max_window = max(max_window, end - start + 1)

        return max_window
