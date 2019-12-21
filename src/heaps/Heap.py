class MinHeap:

    def heapify(self, n, i, array):
        """
        Whenever parent is greater than children,
        Swap parent with smallest child E.g. [3, 2, 1] =>(3 <-> 1) => [1, 2, 3]
        This implies parent satisfies heap property

        Keep percolating largest element downwards, to make largest element satisfy heap property.
        """

        left = 2 * i + 1
        right = 2 * i + 2

        smallest = i

        if left < n and array[left] < array[smallest]:
            smallest = left
        if right < n and array[right] < array[smallest]:
            smallest = right

        if smallest != i:
            array[i], array[smallest] = array[smallest], array[i]

            self.heapify(n, smallest, array)

    def buildheap(self, array):
        i = (len(array) - 1) / 2

        while i >= 0:
            heap.heapify(len(array), i, array)
            i -= 1

    def heap_sort(self, array):
        n = len(array)

        # Build heap
        i = (n - 1) / 2

        while i >= 0:
            self.heapify(n, i, array)
            i -= 1

        for j in range(n - 1, 0, -1):
            array[j], array[0] = array[0], array[j]
            self.heapify(j, 0, array)


if __name__ == "__main__":

    array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print array

    heap = MinHeap()

    i = (len(array) - 1) / 2

    while i >= 0:
        heap.heapify(len(array), i, array)
        i -= 1

    print array

    heap.heap_sort(array)
    print array
