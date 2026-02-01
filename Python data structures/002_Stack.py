#Stack
# A block that have a new block on top and so on
#...
#5
#20
#10
# Adding a new block called the Push operations
# Taking the top element and processing it
# The pop operations is take out the top element
# Add it on top or Remove it on top without processing it


# LIFO = Last In First Out
# The element that was added last to the stack will be the first one to processed

# Imagine There's wedding cake of your cousin. It's contains 5 layers
# If you wanna eat it, you must eat from the top layers which is layer#05
# Because if you're eating the bottom or layer#01 or layer#02, the cake will collapse!

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    # O(1) - Constant Time
    def __len__(self):
        return self.size

    # Our node still don't have representation function we have to access the value
    # O(n) - Linear Time
    def __repr__(self):
        items = []
        current_item = self.top

        while current_item is not None:
            items.append(str(current_item.value))
            current_item = current_item.next

        return ','.join(items)

    # When i wanna adding a new element with a certain value
    # O(1) - Constant Time
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

        self.size += 1

    # if my pointer of the stack is now not pointing at the top
    # but the top pointing to as the next element below
    # So it's make my pointer located to 'that' element
    # O(1) - Constant Time
    def pop(self):
        if self.top is None:
            raise ValueError("Stack is empty")

        pop_value = self.top.value
        self.top = self.top.next

        self.size -= 1

        return pop_value

    # Just looking at the value but not popping out yet!
    # O(1) - Constant Time
    def peek(self):
        if self.top is None:
            raise ValueError("Stack is empty")
        return self.top.value

    # O(1) - Constant Time
    def is_empty(self):
        return self.top is None

if __name__ == '__main__':
    stack = Stack()

    stack.push(10) # this is first element, at the bottom, This is the bottomest
    stack.push(14) # Second element, put it at the top of 10
    stack.push(16) # Third element, put it at the top of 14
    stack.push(6) # Forth element, put it at the top of 16
    stack.push(12) # Fifth element, put it at the top of 6, This is The toppest

    # Stack will look exactly like this:
    #12
    #6
    #16
    #14
    #10

    print(stack) # Whole stack
    print()

    print(stack.peek()) # just look at the elements in the stack, it should be I=0, which is 12
    print()

    print(stack.pop()) # Pop1: get 12 out
    print(stack) # remain: 6, 16, 14, 10
    print(stack.pop()) # Pop2: get 6 out
    print(stack) # remain: 16, 14, 10
    print(stack.pop()) # Pop3: get 16 out
    print(stack) # remain: 14, 10
    print(stack.pop()) # Pop4: get 14 out
    print(stack) # remain: 10
    print(stack.pop()) # Pop5: get 10 out
    print(stack) # remain: None

    print()
    print(stack.is_empty()) # Check whether the stack is available

