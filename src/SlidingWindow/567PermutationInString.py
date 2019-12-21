class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        A = [ord(a) - ord('a') for a in s1]
        B = [ord(b) - ord('a') for b in s2]

        target = [0] * 26
        for a in A:
            target[a] += 1

        window = [0] * 26
        for i, b in enumerate(B):
            window[b] += 1

            if i >= len(A):
                window[B[i - len(A)]] -= 1

            if window == target:
                return True

        return False


class Solution(object):
    def allZeros(self, frequency):
        for i in range(len(frequency)):
            if frequency[i] != 0:
                return False

        return True

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        len1 = len(s1)
        len2 = len(s2)

        if not (len1 <= len2):
            return False

        frequency = [0] * 26
        chars1 = [ord(a) - ord('a') for a in s1]
        chars2 = [ord(b) - ord('a') for b in s2]

        for i in range(len1):
            frequency[chars1[i]] -= 1
            frequency[chars2[i]] += 1

        if self.allZeros(frequency):
            return True

        for i in range(len1, len2):
            frequency[chars2[i - len1]] -= 1
            frequency[chars2[i]] += 1

            if self.allZeros(frequency):
                return True

        return False