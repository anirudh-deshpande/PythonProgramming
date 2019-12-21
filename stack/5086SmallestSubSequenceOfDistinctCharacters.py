from collections import Counter

class Solution(object):
    def smallestSubsequence(self, text):
        """
        :type text: str
        :rtype: str
        """

        stack = []
        counter = Counter(text)
        visited = set()

        for i in range(len(text)):
            char = text[i]

            if char in visited:
                counter[char] -= 1
                continue

            # while stack top is bigger than current_char,
            # stack top is available in the future
            while stack and char < stack[-1] and counter[stack[-1]]:
                top = stack.pop()
                visited.remove(top)

            stack.append(char)
            visited.add(char)
            counter[char] -= 1

        return ''.join(stack)
