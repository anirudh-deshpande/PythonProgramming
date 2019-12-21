class Solution(object):
    def allSubStrings(self, res, cur_sub, i, p):

        if i > len(p):
            return

        if cur_sub not in res:
            res.append(cur_sub)

        for j in range(i, len(p)):
            cur_sub += p[j]
            self.allSubStrings(res, cur_sub, i + 1, p)
            cur_sub = cur_sub[0:len(cur_sub) - 1]

    def subString(self, s, n):
        # Pick starting point in outer loop
        # and lengths of different strings for
        # a given starting point

        res = set()
        for i in range(n):
            for len in range(i + 1, n + 1):
                res.add(s[i: len])

        return res

    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        if not p:
            return 0

        # all_sub_str = []
        # self.allSubStrings(all_sub_str, '', 0, p)
        # all_sub_str = all_sub_str[1:]
        # print all_sub_str

        sub_strs = self.subString(p, len(p))

        len_p = len(p)
        append_num = int(len_p / 26) + 2

        s = s_app = "abcdefghijklmnopqrstuvwxyz"

        for i in range(0, append_num):
            s_app += s

        count = 0

        for sub_str in sub_strs:
            if sub_str in s_app:
                # print sub_str, "Appending count"
                count += 1

        return count


# p = "uvwxyzabcdefg"
p = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
print Solution().findSubstringInWraproundString(p)

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
#