import itertools
class Solution(object):
    def dfs(self, n, i, str, arr, ans, visited):

        if i == n:
            ans.append(str)
            return

        for j in range(i, n):
            if not visited[j]:
                visited[j] = True
                cur_arr = arr[j]
                for val in cur_arr:
                    self.dfs(n, i + 1, str + val, arr, ans, visited)
                visited[j] = False

    def expand(self, S):
        """
        :type S: str
        :rtype: List[str]
        """

        A = S.replace("{", " ").replace("}", " ").split(' ')

        B = [b.split(',') for b in A if b]
        visited = [False] * len(B)

        ans = []
        self.dfs(len(B), 0, "", B, ans, visited)

        return sorted(''.join(str) for str in ans)


    def expand2(self, S):
        """
        :type S: str
        :rtype: List[str]
        """

        A = S.replace("{", " ").replace("}", " ").split(' ')

        B = [b.split(',') for b in A]

        ans = []
        for a in itertools.product(*B):
            ans.append(a)

        return sorted(''.join(str) for str in ans)


print Solution().expand("{a,b}{a,b}{a,b}{a,b}{a,b}{a,b}{a,b}{a,b}{a,b}{a,b}")