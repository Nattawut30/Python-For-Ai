#Queue
# look a lot like stacks but stacks pop whoever on top out and also push to added more

# Stacks = LIFO = Last in, First Out
# Queue = FIFO = First In, First Out

# Imagine you are queuing to paying your grocery store.
# you can't jump out of queue but wait in line before reaching your queue
# She#01 came first get checking out first, He#02 came after She#01 get paying later

# If cashier is the "front" then the queue is the "rear"
# Queue1 get checking and paying first then Queue2, Queue3, .... so on
# Hence, we need to "peak" the Queue1 first because she came first!

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    # All I have to do is I have to look at the value
    # O(1) -- Constant
    def __len__(self):
        return self.size

    # I have to go through all the note in the queue to get all the elements
    # O(n) -- Linear Time
    def __repr__(self):
        items = []
        current_item = self.front

        while current_item is not None:
            items.append(str(current_item.value))
            current_item = current_item.next

        return ', '.join(items)

    # I have to look at the rear and I have to append an elements
    # O(1) -- Constant
    def enqueue(self, value):
        new_node = Node(value)

        if self.rear is None:
            self.front = self.rear = new_node # The front and the rear are the same object new note.
        else:
            self.rear.next = new_node # if I got 1 element left my pointers both will point at them
            self.rear = new_node # but if I add another 1 element in it, I want to reset the pointers

        self.size += 1

    # No matters how elements I have, I just wanna take the first elements from the front of the queue
    # And also adjust my pointer!
    # O(1) -- Constant
    def dequeue(self):
        if self.front is None:
            raise IndexError('Queue is empty')

        dequeue_value = self.front.value # So I get the value of the first note of the que
        self.front = self.front.next # my front element should now be pointing to the next element

        if self.front is None:
            self.rear = None

        self.size -= 1 # makes both pointers of front and rear point to "None"

        return dequeue_value

    # I just wanna look at the first element and ref. and look at the value
    # O(1) -- Constant
    def peek(self):
        if self.front is None:
            raise IndexError('Queue is empty')

        return self.front.value # Storing it and return immediately

    # O(1) -- Constant
    def is_empty(self):
        return self.front is None

if __name__ == '__main__':
    queue = Queue()

    queue.enqueue(10) #Q1
    queue.enqueue(20) #Q2
    queue.enqueue(30) #Q3
    queue.enqueue(40) #Q4
    queue.enqueue(50) #Q5
    queue.enqueue(60) #Q6

    print(queue) # Total elements
    print(len(queue)) # Total Q
    print()

    print(queue.dequeue()) # Q1 came to cashier first, pay fist!
    print(queue.dequeue()) # Q2 came later next to Q1, following the Q1 but need Q1 to pay first!
    print(queue.dequeue()) # Q3 came later next to Q2, get paying too but need to wait Q1 and Q2!
    print()

    print(queue) # What elements left?
    print(len(queue)) # How many Q left?
