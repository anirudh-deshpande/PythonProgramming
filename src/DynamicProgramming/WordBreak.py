class Solution(object):
    def find(self, M, start):

        for i in range(start, len(M)):
            for j in range(i, len(M)):
                if M[i][j] == 1:
                    M[0][j] = 1
                    return self.find(M, j + 1)

    def wordBreak(self, word, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        M = [[0 for x in range(len(word))] for y in range(len(word))]

        for i in range(len(word)):
            for j in range(i, len(word)):
                if word[i:j + 1] in wordDict:
                    M[i][j] = 1

        for arr in M:
            print arr

        print '\n'

        self.find(M, 0)

        for arr in M:
            print arr

        return True if M[0][len(M) - 1] == 1 else False


### Working
class Solution(object):
    def wordBreak(self, word, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        M = [False for i in range(len(word) + 1)]
        M[0] = True

        for i in range(1, len(word) + 1):
            for j in range(i):
                if M[j] and word[j:i] in wordDict:
                    M[i] = True

        return M[len(word)]