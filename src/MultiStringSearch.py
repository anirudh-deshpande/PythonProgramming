# Naive 1
# Time len(smallStrings) * len(bigString) * len(big(smallStrings))
def multiStringSearchN1(bigString, smallStrings):
    contains = []
    big_strig_components = bigString.split()

    for small_str in smallStrings:
        is_present = False
        for big_str in big_strig_components:
            if small_str in big_str:
                is_present = True
                break
        contains.append(is_present)
    return contains


# Naive 2
# Time: len(smallStrings) * len(bigString) * len(big(smallStrings))
def multiStringSearchN2(bigString, smallStrings):
    contains = []

    for smallString in smallStrings:
        small_index = 0
        big_index = 0

        while small_index < len(smallString) and big_index < len(bigString):
            if smallString[small_index] == bigString[big_index]:
                small_index += 1
                big_index += 1
            else:
                small_index = 0
                big_index += 1

        if small_index == len(smallString):
            contains.append(True)
        else:
            contains.append(False)
    return contains




# Approach 3
# Space: O(b^2)
# Time: O(b^2)
# Suffix Trie construction
def addSuffixToTrie(i, root, string, end_char):
    curNode = root
    for j in range(i, len(string)):
        curChar = string[j]
        if curChar not in curNode:
            curNode[curChar] = {}
        curNode = curNode[curChar]
    curNode[end_char] = {}


# Suffix Trie construction
def getSuffixTree(string):
    root = {}
    for i in range(len(string)):
        addSuffixToTrie(i, root, string, "*")
    return root


# Trie search
# Time: O(nS)
# Space: O(nS)
def searchSuffixTree(root, string, end_char):
    curNode = root
    for char in string:
        if char not in curNode:
            return False
        curNode = curNode[char]
    return True


def multiStringSearch(bigString, smallStrings):
    # Construct Trie
    suffix_tree = getSuffixTree(bigString)
    print suffix_tree
    contains = []
    # search Trie
    for string in smallStrings:
        is_present = searchSuffixTree(suffix_tree, string, "*")
        contains.append(is_present)
    return contains


################################################################
# Better implementation                                        #
################################################################


def appendContainedStringsInTrie(trie, i, string, containedStrings):
    node = trie.root
    end_char = trie.end_char

    for j in range(i, len(string)):
        current_char = string[j]
        if current_char not in node:
            return
        node = node[current_char]
        if end_char in node:
            print string
            print node
            containedStrings.append(node[end_char])


def multiStringSearchTrie(bigString, smallStrings):
    trie = Trie()

    # Insert smallStrings into trie
    for string in smallStrings:
        trie.insert_string(string)

    containedStrings = []

    for i in range(len(bigString)):
        appendContainedStringsInTrie(trie, i, bigString, containedStrings)

    output = []
    print containedStrings

    for str in smallStrings:
        if str in containedStrings:
            output.append(True)
        else:
            output.append(False)

    return output

class Trie:
    def __init__(self):
        self.root = {}
        self.end_char = "*"

    def insert_string(self, string):
        node = self.root

        for i in range(len(string)):
            current_char = string[i]
            if current_char not in node:
                node[current_char] = {}
            node = node[current_char]

        node[self.end_char] = string


print multiStringSearchTrie("this is a big string",  ["biggest", "string", "is", "a", "ring"])




