# Binary Search Tree

# it a tree it looks similar to a family tree
# but the key difference is each node follows a specific ordering rule
# left-child has to contain values smaller than the parent
# right-child has to contain values greater than the parent
# this makes searching insertion and deletion extremely efficient

# Imagine This!
# Top: 30 (root)
# Left: 20, 10 (smaller)
# Right: 40, 50 (Greater)

# The rules of the left parent and right needing to be less than one another
# Every time we look to access an element insert an element or delete an element
# You can eliminate half the tree as we're going through it
# Looks like it find that word because you're just splitting up your search space by half every layer

# Worst Case Scenario: Those operations access insertion and deletion that looks like a Linked-List
# Ex. My root is 5, then 6 -> 10 -> 30 always goes right because it's greater values than 5

# Leaf nodes = Those notes that don't have any children
# Designed Layers = O(h) = runtime complexity. H is the height of the tree.

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key
        self.value = None

    def __repr__(self):
        return f"({self.key}, {self.value})"

class BinarySearchTree:

    def __init__(self):
        self.root = None

    # O(n) worst case, O(log n) average case, O(n) always
    def __contains__(self, key):
        current_node = self.root

        while current_node is not None:
            if key < current_node.key:
                current_node = current_node.left
            elif key > current_node.key:
                current_node = current_node.right
            else:
                return True

        return False

    # O(n) - linear
    def __iter__(self): # allows me to iterate
        yield from self._in_order_traversal(self.root)

    # O(n) - linear
    def __repr__(self):
        return str(list(self._in_order_traversal(self.root)))
    # return the string version of the list version of whatever we get from the generator
    # call the in order traversal -> onto root -> return it into a list -> turn a generator into a list
    # Get all the value and store it in a list, and then we can turn that into a string

    # O(n) worst case, O(log n) average case, O(n) always
    def insert(self, key, value):

        # Looks like we're playing some game
        # add the concept on it
        # And if I keep looking for it, can still update its value

        if self.root is None:
            self.root = Node(key)
            self.root.value = value
        else:
            current_node = self.root
            while True:
                if key < current_node.key:
                    if current_node.left is None:
                        current_node.left = Node(key)
                        current_node.left.value = value
                        current_node.left.parent = current_node
                        break
                    else:
                        current_node = current_node.left

                elif key > current_node.key:
                    if current_node.right is None:
                        current_node.right = Node(key)
                        current_node.right.value = value
                        current_node.right.parent = current_node
                        break
                    else:
                        current_node = current_node.right

                else:
                    current_node.value = value
                    break

    # O(n) worst case, O(log n) average case, O(n) always
    def search(self, key):
        current_node = self.root

        # The idea is I have a tree and looking for a value
        # Just go left-right depending on if the key is larger than or less than the current key.
        # And then I found what I want, then return that note.
        # Then I keep looking, but It's no value left. So, return none.

        while True:
            if current_node is None or current_node.key == key:
                return current_node
            elif key < current_node.key:
                if current_node.left is None:
                    return None
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    return None
                else:
                    current_node = current_node.right

    # O(n) worst case, O(log n) average case, O(n) always
    def delete(self, key):

        # First Case: When I'm deleting a leaf note. So, I can do it right now.
        # Super Easy: just cut the connection or remove the reference

        # Second Case: When I delete a note with 1 child
        # When delete it, I have to redirect the connection
        # I need to replace the note I'm deleting with the only child note.

        # Third Case: When I delete a note with 2 child
        # I need to replace the note I'm deleting with its successor
        # ** I'm replacing it with the smallest key that is still larger than the key I'm replacing **

        node = self.search(key)
        if node is None:
            raise KeyError('Node with this key does not exist')

        self._delete(node) # Calls _delete

    # O(n) - linear
    def traverse(self, order): #traverse the tree in different orders.
        if order == 'inorder':
            yield from self._in_order_traversal(self.root)
        elif order == 'preorder':
            yield from self._pre_order_traversal(self.root)
        elif order == 'postorder':
            yield from self._post_order_traversal(self.root)
        else:
            raise ValueError("Unknow order")

# =============== The helper methods ===============

    def _delete(self, node):
        # Node is leaf node.
        if node.left is None and node.right is None:
            if node.parent is None:
                self.root = None
            else:
                if node.parent.right == node:
                    node.parent.right = None
                else:
                    node.parent.left = None
                node.parent = None

        # Node has 1 child node.
        # 10 -> 20 -> 30, Let say cut 20!
        # I need to redirect it to this child node.
        # Then set the child nodes parents reference to the parent that it was before
        # Then cut both directions.
        elif node.left is None or node.right is None:
            child_node = node.left if node.left is not None else node.right

            if node.parent is None:
                child_node.parent = None
                self.root = child_node
            else:
                if node.parent.right == node:
                    node.parent.right = child_node
                else:
                    node.parent.left = child_node
                child_node.parent = node.parent
            node.parent = node.left = node.right = None

        # Node has 2 child nodes.
        else:
            successor = self._successor(node)

            # Delete the key and the value
            # So whatever is in here, I'm going to wipe it clean
            # Copy the value of successor, and then just delete

            node.key = successor.key
            node.value = successor.value

            self._delete(successor)

    def _successor(self, node):
        if node is None:
            raise ValueError("Cannot find successor of None")

        if node.right is None:
            return None
        else:
            current_node = node.right
            while current_node.left is not None:
                current_node = current_node.left
            return current_node

    def _predecessor(self, node):
        # Predecessor: The largest note that's smaller than the note
        # the predecessor of 10 would be 9, it's the largest note but still less than 10

        if node is None:
            raise ValueError("Cannot find predecessor of None")

        if node.left is None:
            return None
        else:
            current_node = node.left
            while current_node.right is not None:
                current_node = current_node.right
            return current_node

    # We can make it grouping and then sorting it = Recursively ordering
    # Calls it from traverse method

    def _in_order_traversal(self, node):
        # We're going to yield.
        # We're going to ascending order

        if node is not None:
            yield from self._in_order_traversal(node.left)
            yield (node.key, node.value)
            yield from self._in_order_traversal(node.right)

    def _pre_order_traversal(self, node):
        # Root note first then left -> right

        if node is not None:
            yield (node.key, node.value)
            yield from self._pre_order_traversal(node.left)
            yield from self._pre_order_traversal(node.right)

    def _post_order_traversal(self, node):
        # left -> right -> root

        if node is not None:
            yield from self._post_order_traversal(node.left)
            yield from self._post_order_traversal(node.right)
            yield (node.key, node.value)

if __name__ == '__main__':
    bst = BinarySearchTree()

    bst.insert(10, 'Hello')
    bst.insert(5, 'Hello')
    bst.insert(22, 'Hello')
    bst.insert(2, 'Hello')
    bst.insert(9, 'Hello')
    bst.insert(12, 'Hello')
    bst.insert(30, 'Hello')
    bst.insert(11, 'Hello')
    bst.insert(15, 'Hello')
    bst.insert(30, 'Hello')
    bst.insert(23, 'Hello')
    bst.insert(35, 'Hello')
    bst.insert(1, 'Hello')

    print(bst)
    print()

    bst.delete(9)
    bst.delete(2) # check the case, 1 should replace 2
    bst.delete(22) # delete another, is it still running and replacing

    for i in bst.traverse('inorder'):
        print(i)
    print()

    for i in bst.traverse('preorder'):
        print(i)
    print()

    for i in bst.traverse('postorder'):
        print(i)
    print()

    print(bst.search(30)) # Lookup for key value of X
    print()

# ==============================   ==============================   ==============================
# When you delete a node with two children, you look for its Successor (the next biggest number).
# Rule: To find the successor, you go Right once, then Left as far as you can go.
# The "No Left Child" Fact: Because you went as far left as possible,
# the successor cannot have a left child. If it did, you would have moved to that child instead!
# The "Right Child" Possibility: The successor can still have a right child.

# Imagine a company hierarchy (a tree). The Manager (Node 10) leaves.
# We need to promote someone to take their desk. We pick the most junior person from the "Senior" department—this is the Successor.
# That person (Successor) definitely doesn't have anyone reporting to them on their "Junior" side (no left child)
# because then that person would have been the most junior instead.
# But they might have an assistant (a right child) who is slightly more senior than them but still part of that department.
# When the Successor moves up to the Manager's desk,
# they don't leave their assistant behind; the assistant just moves up to fill the Successor's old spot.
# ==============================   ==============================   ==============================

# >> Create a fresh tree <<
new_bst = BinarySearchTree()

# >> Insert nodes to create a specific shape <<

# We want 20 to be the target for deletion.
# 30 will be its right child.
# 25 will be the successor (leftmost of 30).
# 27 will be the successor's right child.
for val in [20, 10, 30, 25, 35, 27]:
    new_bst.insert(val, 'Data')

print("Before deleting 20 (Root):")
print(list(new_bst.traverse('inorder')))

# >> The Big Test <<
new_bst.delete(20)

print("\nAfter deleting 20:")
print(list(new_bst.traverse('inorder')))
# The value 25 (Successor) should take the place of 20.
# The value 27 (Successor's child) should now be attached to the left of 30.
# The inorder traversal should still be perfectly sorted: [10, 25, 27, 30, 35].