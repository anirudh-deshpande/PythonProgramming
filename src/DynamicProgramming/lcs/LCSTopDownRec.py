import sys
sys.setrecursionlimit(1000000)
import time

class Solution(object):

    def lcsRecWithMemo(self, A, B, i, j, memo):
        if i >= len(A) or j >= len(B):
            return 0

        if (i, j) not in memo:
            if A[i] == B[j]:

                if (i+1, j+1) not in memo:
                    memo[(i+1, j+1)] = self.lcsRecWithMemo(A, B, i + 1, j + 1, memo)

                memo[(i, j)] = 1 + memo[(i+1, j+1)]
            else:

                if (i,j+1) not in memo:
                    memo[(i,j+1)] = self.lcsRecWithMemo(A, B, i, j+1, memo)

                if (i+1,j) not in memo:
                    memo[(i+1,j)] = self.lcsRecWithMemo(A, B, i+1, j, memo)

                memo[(i, j)] = max(memo[(i, j+1)], memo[(i+1, j)])

        return memo[(i, j)]


    def lcsRecWithMemoMatrix(self, A, B, i, j, memo):
        if i >= len(A) or j >= len(B):
            return 0

        if memo[i][j] == 0:
            if A[i] == B[j]:

                if memo[i+1][j+1] == 0:
                    memo[i + 1][j + 1] = self.lcsRecWithMemoMatrix(A, B, i + 1, j + 1, memo)

                memo[i][j] = 1 + memo[i+1][j+1]
            else:

                if memo[i][j+1] == 0:
                    memo[i][j + 1] = self.lcsRecWithMemoMatrix(A, B, i, j+1, memo)

                if memo[i+1][j] == 0:
                    memo[i + 1][j] = self.lcsRecWithMemoMatrix(A, B, i+1, j, memo)

                memo[i][j] = max(memo[i][j + 1], memo[i+1][j])

        return memo[i][j]


    def lcsRec(self, A, B, i, j):
        if i >= len(A) or j >= len(B):
            return 0

        if A[i] == B[j]:
            return 1 + self.lcsRec(A, B, i+1, j+1)

        return max(self.lcsRec(A, B, i+1, j), self.lcsRec(A, B, i, j+1))


    def lcsBottomUp(self, A, B):
        m = len(A)
        n = len(B)

        memo = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    memo[i][j] = 1 + memo[i-1][j-1]
                else:
                    memo[i][j] = max(memo[i][j-1], memo[i-1][j])


        # Reconstruction

        i = m
        j = n
        res = ""

        while i >= 0 and j >= 0:
            if memo[i][j] == memo[i-1][j-1] + 1:
                res += A[i-1]
                i -= 1
                j -= 1
            elif memo[i-1][j] >= memo[i][j-1]:
                i -= 1
            else:
                j -= 1
        return res[::-1]

    def lcsBottomUpString(self, A, B):
        m = len(A)
        n = len(B)

        memo = [["" for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    memo[i][j] = memo[i - 1][j - 1] + A[i - 1]
                else:
                    memo[i][j] = max(memo[i][j - 1], memo[i - 1][j], key=len)

        return memo[m][n]

    # def compute_lcs(s, t):
    #     m, n = len(s), len(t)
    #     dp = [[""] * (n + 1) for _ in range(m + 1)]
    #     for i in range(1, m + 1):
    #         for j in range(1, n + 1):
    #             if s[i - 1] != t[j - 1]:
    #                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)
    #             else:
    #                 dp[i][j] = dp[i - 1][j - 1] + s[i - 1]
    #     return dp[-1][-1]
    # print(compute_lcs(str1, str2))



# memo = {}
#
# start = time.time()
# print Solution().lcsRecWithMemo("abdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdace", "babcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabce", 0, 0, memo)
# end = time.time()
#
# print "Mem map: " + str(end - start)
#
#
# A = "abdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdace"
# B = "babcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabce"
#
# memo = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
#
# start = time.time()
# print Solution().lcsRecWithMemoMatrix(A, B, 0, 0, memo)
# end = time.time()
#
# print "Mem matrix: " + str(end - start)

# start = time.time()
# print Solution().lcsRec("abdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdaceabdace", "babcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabcebabce", 0, 0)
# end = time.time()

# print "Rec: " + str(end - start) # More than 45 mins

start = time.time()
print Solution().lcsBottomUp("abdace", "babce")
end = time.time()

print "BottomUp: " + str(end - start)

# start = time.time()
# print Solution().lcsBottomUpString(A, B)
# end = time.time()
#
# print "BottomUp str: " + str(end - start)
