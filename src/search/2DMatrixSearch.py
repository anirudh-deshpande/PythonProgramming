class Solution(object):

    def searchHelper(self, matrix, i, j, target):

        if matrix[i][j] == target:
            return True

        ans = False

        if i+1 < len(matrix) and matrix[i+1][j] <= target:
            ans = self.searchHelper(matrix, i+1, j, target)

        if ans:
            return ans

        if j+1 < len(matrix[0]) and matrix[i][j+1] <= target:
            ans = self.searchHelper(matrix, i, j+1, target)

        if ans:
            return ans

        return False



    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        # return self.searchHelper(matrix, 0, 0, target)

        row, m, col, n = 0, 0, len(matrix), len(matrix[0])

        while row+1 < m and col+1 < n:

            if matrix[row][col] == target:
                return True

            if matrix[row+1][col] <= target:
                row += 1

            if matrix[row][col+1] <= target:
                col += 1

        return False







matrix = [[48,1024,70,113,133,163,170,216,298,389],[89,169,215,222,250,348,379,426,469,554],[178,202,253,294,367,392,428,434,499,651],[257,276,284,332,380,470,516,561,657,698],[275,331,391,432,500,595,602,673,758,783],[357,365,412,450,556,642,690,752,801,887],[359,451,534,609,654,662,693,766,803,964],[390,484,614,669,684,711,767,804,857,1055],[400,515,683,732,812,834,880,930,1024,1130],[480,538,695,751,864,939,966,1024,1089,1224]]
target = 1024

soln = Solution()

print soln.searchMatrix(matrix, target)
