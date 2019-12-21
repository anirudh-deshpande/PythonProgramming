### DFS O(n)

### Madhur's awesome solution
class Solution(object):
    def height(self, node):

        if node == None:
            return -1

        return 1 + self.height(node.left)

    def nodeExists(self, node, n, height):
        i = 1

        while i <= height and node != None:
            if (n >> height - i) & 1 == 0:
                node = node.left
            else:
                node = node.right

            i += 1

        return node != None

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        height = self.height(root)

        if height == 0:
            return 1

        start = 0
        end = (1 << height) - 1

        while start <= end:
            mid = start + (end - start) / 2

            if self.nodeExists(root, mid, height):
                start = mid + 1
            else:
                end = mid - 1

        return (1 << height) + start - 1







### Most voted

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def height(self, node):
        if node == None:
            return -1
        return 1 + self.height(node.left)

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        height = self.height(root)

        if height == 0:
            return 1

        if (height - 1) == self.height(root.right):
            return (1 << height) + self.countNodes(root.right)
        else:
            return (1 << (height - 1)) + self.countNodes(root.left)
