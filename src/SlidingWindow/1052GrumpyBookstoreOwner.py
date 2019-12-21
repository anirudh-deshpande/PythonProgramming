from collections import Counter


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        if len(s) == 0:
            return 0

        start = 0
        unique = Counter()
        max_freq = 0

        for end in range(len(s)):
            unique[s[end]] += 1
            max_freq = max(max_freq, unique[s[end]])

            if end - start + 1 - max_freq > k:
                unique[s[start]] -= 1
                start += 1

        return end - start + 1
