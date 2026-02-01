# Heap
# Priority Queue

# Imagine a pyramid of stacked boxes
# where the smallest box is always at the very top
# You don't randomly grab a box from the middle
# You mostly take it from the top, but specifically...
# They always need a box to be at the top
# if any boxes are removed within the pyramid, they need to re-adjust
# So... There's a box still at the top

# Min-Heap: every parent is SMALLER than its children, Top elements is the smallest
# Max-Heap: evert parent is LARGER than its children, Top elements is the largest

# Extract-Min: remove the top node then take the last node put it at the top (now it's invalid heap)
# Sift-down ops: look at the 2 child nodes and which one is the smallest. Swap the positions. (repeat the steps)
# Sift-up ops: comparing with the parent node which one larger-smaller, then swim up positions.

# Left-Child: 2 * index of the node + 1
# Right-Child: 2 * index of the node + 2
# Parent = (index - 1) // 2, If index !=0

# O(h) = O(log n)

class MinHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return str(self.heap) # show the list/heap

    # O(log n)
    def insert(self, key, value):
        self.heap.append((key, value))
        self._sift_up(len(self.heap) - 1)

    # O(1) - constant
    def peek_min(self):
        if not self.heap:
            raise IndexError("Empty heap")
        return self.heap[0]

    # O(log n)
    def extract_min(self):
        if not self.heap:
            raise IndexError("Empty heap")

        # If I pop it out, it could be an empty list
        # Make me restore the heap which is the last element, and check sift it down
        min_element = self.heap[0]
        last_element = self.heap.pop()

        if self.heap:
            self.heap[0] = last_element
            self._sift_down(0)

        return min_element

    # O(n) - linear, go through all the elements and perform
    def heapify(self, elements):
        # Get a collection of values, structure as a heap
        # Re-order them so they fit the heap property.

        self.heap = list(elements)

        for i in reversed(range(self._parent(len(self.heap) - 1) + 1)):
            self._sift_down(i)

    # O(n) - linear, adding 2 lists together and then heapify
    def meld(self, other_heap):
        combined_heap = self.heap + other_heap.heap
        self.heapify(combined_heap)

        # keep the heap that existing, but now they are an empty list
        # absorb the elements from the other heap

        other_heap.heap = []

    # O(1) - constant
    def _parent(self, index):
        return (index - 1) // 2 if index !=0 else None

    # O(1) - constant
    # If doing Max, just change < to > and implementing largest and smallest
    def _left_child(self, index):
        left = 2 * index + 1
        return left if left < len(self.heap) else None

    # O(1) - constant
    def _right_child(self, index):
        right = 2 * index + 2
        return right if right < len(self.heap) else None

    # O(log n)
    def _sift_up(self, index):
        # Swim operations

        parent_index = self._parent(index)

        while parent_index is not None and self.heap[index][0] < self.heap[parent_index][0]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = self._parent(index)

    # O(log n)
    def _sift_down(self, index):
        # Sync Operations

        # Smallest variable pointing to the index or having the index of the smallest note
        # will keep the note with the smallest key value.

        while True:
            smallest = index

            left = self._left_child(index)
            right = self._right_child(index)

            if left is not None and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left

            if right is not None and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest
            # We just swap the positions with the small smallest element, and we need to progress the index

if __name__ == "__main__":
    min_heap = MinHeap()
    min_heap.heapify([[10, '10'], [9, '9'], [8, '8'], [7, '7'], [6, '6'], [5, '5'], [4, '4'], [3, '3'], [2, '2'], [1, '1']])
    print(min_heap.heap)
    print()

    import heapq
    mylist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    heapq.heapify(mylist)
    print(mylist)
    print()

    print(min_heap.extract_min())
    print(min_heap.extract_min())
    print(min_heap.extract_min())

    print()

    print(heapq.heappop(mylist))
    print(heapq.heappop(mylist))
    print(heapq.heappop(mylist))

    print()

    min_heap.insert(2, '2')
    print(min_heap)

    print()

    heapq.heappush(mylist, 2)
    print(mylist)

    print()

    min_heap2 = MinHeap()
    min_heap2.heapify([[5, '5'], [7, '7'], [2, '2']])
    min_heap.meld(min_heap2)
    print(min_heap)