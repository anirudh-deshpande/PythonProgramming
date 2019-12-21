import collections

TupleType = collections.namedtuple("TypeName", ("element1", "element2"))

tuples = []

tuples.append(TupleType("element1", 1))
tuples.append(TupleType("siri", "iphone"))

# print(tuples)
# print(tuples[0].element1)
# print(tuples[0].element2)


Element = collections.namedtuple("Element", ("node", "low", "high"))
element = Element("node", float('-inf'), float('inf'))
#print(element)

queue = collections.deque([element])
print(queue.pop())
