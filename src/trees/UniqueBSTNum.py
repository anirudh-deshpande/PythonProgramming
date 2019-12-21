def numTrees(self, n):
    """
    :type n: int
    :rtype: int
    """
    return self.numTreesHelper(1, n + 1,
                               [[None for x in range(n + 2)] for y in range(n + 2)])


def numTreesHelper(self, start, end, Matrix):
    if start >= end:
        return 1

    if Matrix[start][end] is not None:
        return Matrix[start][end]

    result = 0

    for i in range(start, end):
        numLeft = self.numTreesHelper(start, i, Matrix)
        Matrix[start][i] = numLeft

        numRight = self.numTreesHelper(i + 1, end, Matrix)
        Matrix[i + 1][end] = numRight

        result += numLeft * numRight

    return result


def numTreesSolution2(self, n):
    """
    :type n: int
    :rtype: int
    """
    T = [0 for i in range(n + 1)]
    T[0] = 1
    T[1] = 1

    for i in range(2, n + 1):
        for j in range(0, i):
            T[i] += T[j] * T[i - j - 1]

    return T[n]