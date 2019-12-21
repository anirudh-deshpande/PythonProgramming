class BinarySearchTree:
    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.right = None
            self.left = None

    def __init__(self):
        self.root = None

    def insertHelper(self, data, parent):
        if parent == None:
            return self.TreeNode(data)

        if data < parent.data:
            parent.left = self.insertHelper(data, parent.left)

        if data > parent.data:
            parent.right = self.insertHelper(data, parent.right)

        return parent

    def insert(self, data):
        self.root = self.insertHelper(data, self.root)


    def preOrder(self, root):
        node = root
        stack = []

        while len(stack) > 0:
            while node is not None:
                print node.data + ' '
                stack.append(node.right)
                node = node.left
            node = stack.pop()






print tree.root.left.data
print tree.root.data
print tree.root.right.data
