class MapSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_char = "*"

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        node = self.root
        for char in key:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.end_char] = val

    def find_sum(self, node, total):
        for char in node:
            if char == self.end_char:
                total += node[self.end_char]
            else:
                total = self.find_sum(node[char], total)
        return total

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return 0
            node = node[char]
        return self.find_sum(node, 0)


'''
["MapSum", "insert", "sum", "insert", "sum", "sum", "insert", "sum", "sum", "sum", "insert", "sum", "sum"]
[[], ["aa",3], ["a"], ["aa",2], ["a"], ["aa"], ["aaa", 3], ["aaa"], ["bbb"], ["ccc"], ["aewfwaefjeoawefjwoeajfowajfoewajfoawefjeowajfowaj", 111], ["aa"], ["a"]]
'''
