# Solution 1, did not work

class Solution(object):
    def removeAll(self, S1, S2, char):

        for i in range(len(S1)):
            if S1[i] == char:
                S1[i] = None

        for j in range(len(S2)):
            if S2[j] == char:
                S2[j] = None

    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str

        Input:
        "TAUXXTAUXXTAUXXTAUXXTAUXX"
        "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
        Output:
        "TAUX"
        Expected:
        "TAUXX"
        """

        res = ""

        if not str1 or not str2:
            return ""

        S1 = list(str1)
        S2 = list(str2)

        min_str = str1 if len(str1) < len(str2) else str2

        for i in range(len(min_str)):
            char = min_str[i]

            if char not in S1 or char not in S2:
                break

            res += char

            self.removeAll(S1, S2, char)

        remaining_s1 = ''.join(s for s in S1 if s != None)
        remaining_s2 = ''.join(s for s in S2 if s != None)

        if remaining_s1 == "" and remaining_s2 == "":
            return res
        else:
            return ""


    # Solution 3
    class Solution(object):
        def gcdOfStrings(self, str1, str2):
            """
            :type str1: str
            :type str2: str
            :rtype: str
            """

            min = str1 if len(str1) <= len(str2) else str2
            max = str1 if len(str1) > len(str2) else str2

            while len(min) > 0:
                if min not in max:
                    return ""

                tmp = max
                max = min
                min = tmp[len(min):]

                # print len(min), len(max)

                min1 = min # failing here, As min was getting overwritten
                min = min if len(min) < len(max) else max
                max = max if len(max) > len(min1) else min1

                # print min, max

            return max
