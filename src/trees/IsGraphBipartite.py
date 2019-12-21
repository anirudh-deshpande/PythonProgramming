from collections import defaultdict


class Node(object):
    def __init__(self, num):
        self.num = num
        self.color = None
        self.visited = False


class Solution(object):
    def getNode(self, num, graph):
        for node in graph:
            if node.num == num:
                return node
        return Node(num)

    def assignColors(self, node, color, graphDict):
        if node.color:
            return

        node.color = color
        next_color = "white" if node.color == "black" else "black"

        for neighbour in graphDict[node]:
            self.assignColors(neighbour, next_color, graphDict)

    def checkColors(self, root, graphDict):
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)

            if node.visited:
                continue

            node.visited = True
            color = node.color

            for neighbour in graphDict[node]:
                if neighbour.color == color:
                    return False
                queue.append(neighbour)
        return True

    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        graphDict = defaultdict(set)

        for i in range(len(graph)):

            for j in range(len(graph[i])):
                src = self.getNode(i, graphDict)
                dst = self.getNode(graph[i][j], graphDict)

                graphDict[src].append(dst)
                graphDict[dst].append(src)

        for node in graphDict:
            self.assignColors(node, "white", graphDict)

        for node in graphDict:
            truth = self.checkColors(node, graphDict)
            if not truth:
                return False
        return True
