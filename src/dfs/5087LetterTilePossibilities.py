# My solution

class Solution(object):
    def allPermutations(self, tiles, visited, used, path):

        if len(path) > 0:
            if path not in visited:
                visited.add(path)

        for j in range(len(tiles)):
            if not used[j]:
                used[j] = True
                self.allPermutations(tiles, visited, used, path + tiles[j])
                used[j] = False

    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        visited = set()
        used = [False] * len(tiles)
        self.allPermutations(tiles, visited, used, "")

        return len(visited)


soln = Solution()
print soln.numTilePossibilities("TBAKNLM")
