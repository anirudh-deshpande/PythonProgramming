### Does not work because of the identified reason
class Solution(object):
    def updateLeftHeight(self, lrtb_height, heightMap):
        for i in range(0, len(heightMap)):
            max_left = 0
            for j in range(0, len(heightMap[0])):
                if max_left < heightMap[i][j]:
                    max_left = heightMap[i][j]
                lrtb_height[i][j].append(max_left)

    def updateRightHeight(self, lrtb_height, heightMap):
        for i in range(0, len(heightMap)):
            max_right = 0
            for j in range(len(heightMap[0]) - 1, -1, -1):
                if max_right < heightMap[i][j]:
                    max_right = heightMap[i][j]
                lrtb_height[i][j].append(max_right)

    def updateTopHeight(self, lrtb_height, heightMap):
        for i in range(0, len(heightMap[0])):
            max_top = 0
            for j in range(len(heightMap)):
                if max_top < heightMap[j][i]:
                    max_top = heightMap[j][i]
                lrtb_height[j][i].append(max_top)

    def updateBottomHeight(self, lrtb_height, heightMap):
        for i in range(0, len(heightMap[0])):
            max_bottom = 0
            for j in range(len(heightMap) - 1, -1, -1):
                if max_bottom < heightMap[j][i]:
                    max_bottom = heightMap[j][i]
                lrtb_height[j][i].append(max_bottom)

    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]:
            return 0

        lrtb_height = [[[] for j in range(len(heightMap[0]))] for i in range(len(heightMap))]

        self.updateLeftHeight(lrtb_height, heightMap)
        self.updateRightHeight(lrtb_height, heightMap)
        self.updateTopHeight(lrtb_height, heightMap)
        self.updateBottomHeight(lrtb_height, heightMap)

        total_water = 0

        for i in range(1, len(heightMap) - 1):
            for j in range(1, len(heightMap[0]) - 1):
                cur_height = heightMap[i][j]
                capacity = min(lrtb_height[i][j])

                if (i - 1) != 0:
                    capacity = min(capacity, min(lrtb_height[i - 1][j]))

                if (i + 1) != len(heightMap):
                    capacity = min(capacity, min(lrtb_height[i + 1][j]))

                if (j - 1) != 0:
                    capacity = min(capacity, min(lrtb_height[i][j - 1]))

                if (j + 1) != len(heightMap[0]):
                    capacity = min(capacity, min(lrtb_height[i][j + 1]))

                if cur_height < capacity:
                    total_water += (capacity - cur_height)

        return total_water



## Did not produce output
import heapq


class Solution(object):
    def insertBorder(self, heap, heightMap, visited):
        m = len(heightMap)
        n = len(heightMap[0])
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    visited[i][j] = True
                    heapq.heappush(heap, (heightMap[i][j], i, j))

    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """

        heap = []
        water = 0
        maximum = -1
        visited = [[False for i in range(len(heightMap[0]))] for j in range(len(heightMap))]
        self.insertBorder(heap, heightMap, visited)

        while not heap:
            cur = heapq.heappop(heap)
            maximum = max(maximum, cur[0])
            i, j = cur[1], cur[2]

            # visit [i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]

            for k in range(i - 1, i + 2):
                if not k < 0 or not k > len(heightMap):
                    if not visited[k][j]:
                        visited[k][j] = True
                        heapq.heappush(heap, (heightMap[k][j], k, j))
                        if heightMap[k][j] < maximum:
                            water += maximum - heightMap[k][j]

            for k in range(j - 1, j + 2):
                if not k < 0 or not k > len(heightMap[0]):
                    if not visited[i][k]:
                        visited[i][k] = True
                        heapq.heappush(heap, (heightMap[i][k], i, k))
                        if heightMap[i][k] < maximum:
                            water += maximum - heightMap[i][k]

        return water







