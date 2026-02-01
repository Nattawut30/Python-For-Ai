# 25 -> None -> 10 -> 5 -> 30 -> 40 -> None | all of them run in orders
# like a deterministic thinking, a train tracks that fixed but still flexible
# Change, insert, delete, pop, the elements as we wants

# Imagine you are on a train and at the head of the train
# you want to check the Car5
# So you need to walk yourself through Car1, Car2, Car3, Car4, and then you arrive at the Car5
# Because you cannot teleport from the head to Car5.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(n) - linear time (even for the best case)
    def __repr__(self): # scan the whole list and print the elements
        if self.head is None:
            return "[]"
        else:
            last = self.head

            return_string = f"[{last.value}"

            while last.next:
                last = last.next
                return_string += f", {last.value}"
            return_string += "]"

            return return_string

    # O(n) - linear time
    def __contains__(self, value):
        last = self.head
        while last is not None:
            if last.value == value:
                return True
            last = last.next
        return False
    # Look at this. No. Next. Look at this. No. Next. No. End of the list.

    # O(n) - linear time
    def __len__(self): # depends on how you implement!
        last = self.head
        counter = 0
        while last is not None:
            counter += 1
            last = last.next
        return counter

    # Go all the elements to get to the end until we can
    # then append a new element.

    # O(n) - constant time
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head # elements at the tail and the head of the list is the same
        else:
            last_node = Node(value)
            last_node.previous = self.tail
            self.tail.next = last_node
            self.tail = last_node
            # go for both direction now
            # Also have a null pointer
            # The next element can be a new element

    # O(1) - constant time
    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            first_node = Node(value)
            first_node.next = self.head
            self.head.previous = first_node
            self.head = first_node

    # O(n) - linear time
    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
        else:
            if self.head is None:
                raise ValueError("Index out of bounds")
            else:
                last = self.head

                for i in range(index - 1): # we wanna go before that element
                    if last.next is None:
                        raise ValueError("Index out of bounds")
                    last = last.next

                new_node = Node(value)
                new_node.next = last.next #the currently pointing to as next
                new_node.previous = last
                if last.next is not None:
                    last.next.previous = new_node  # set up again when insert the elements, but we can pick one
                last.next = new_node

    # tried to find an elements
    # if it finds it, it updates the pointers
    # in C you have to free the memory, but Python you just ignore it

    # O(n) - linear time
    def delete(self, value):
        last = self.head

        if last is not None:
            if last.value == value:
                self.head = last.next
            else:
                while last.next:
                    if last.next.value == value:
                        if last.next.next is not None:
                            last.next.next.previous = last
                        last.next = last.next.next
                        break
                    last = last.next
        # imagine i wanna delete 5 now 10 gonna pointing at five
        # but we gonna make it cuts here
        # the connection theoretically still exists
        # So we cut the connection and skip 5 and runs on

    # O(n) - linear time
    def pop(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last = self.head

            for i in range(index - 1):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next

            if last.next is None:
                raise ValueError("Index out of bounds")
            else:
                if last.next.next is not None:
                    last.next.next.previous = last
                last.next = last.next.next

    # basically, the edge case that it's the last element that is none
    # I still raise a value error

    # O(n) - linear time
    def get(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last = self.head

    # Do not try to change any element or any connection now
            for i in range(index):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next

            return last.value

if __name__ == '__main__':
    ll = DoublyLinkedList()

    # 100, 200, 10, 97, 88, 22, 18, 20, 5
    # I delete 18, 22, 5

    # 100, 200, 10, 97, 88, 20
    # I pop index 1, which is 200

    # 100, 10, 97, 88, 20
    # I should get this exact list left

    ll.append(10)
    ll.insert(5, 1)
    ll.insert(20, 1)
    ll.insert(18, 1)
    ll.insert(22, 1)
    ll.insert(88, 1)
    ll.insert(97, 1)


    ll.prepend(100)

    ll.insert(value=200, index=1) # try to insert the value wherever I want them to be in the elements

    ll.delete(18)
    ll.delete(22)
    ll.delete(5)

    ll.pop(index=1) # try to pop up the index 1, 200 out of game

    print(ll)
    print(ll.get(index=1)) # Ask what index 1 is after customized the list, should be 10 not 200
    print(88 in ll) # 8 is in the list, Should get "True"
    print(888 in ll) # 888 is NOT in the list, Should get "False"