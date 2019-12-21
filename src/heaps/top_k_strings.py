import heapq

import collections

heap = []
Element = collections.namedtuple("Element", ("length", "string"))

def top_k_strings(s, k):
    for str in s:
        heapq.heappush(heap, Element(len(str), str))
        if len(heap) > k and heap and len(str) > heapq.nsmallest(1, heap)[0].length:
            heapq.heappop(heap)

    return list(reversed([element.string for element in heapq.nsmallest(k, heap)]))


s = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh']
print(top_k_strings(s, 1))
