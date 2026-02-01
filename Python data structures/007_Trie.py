# Trie
# The original is "Retrieved"
# The concept is similar to the tree
# Sometimes called it prefix-tree

# Imagine you're climbing a mango tree cause you want to eat it.
# You're slowly climbing each branch to reach your goal or the mango. It's called it the "End"
# Every branch contains tiny sticks it's called the "dictionary" that could lead to your end,
# but you still can't skip or jump over. you gonna falls!
# So, you mission is to reach the target and pick the best routes. Even the separate ways!
# Also, can get the mango that is closet along the way as well.

# [Left]
# Sort through the string by letter-by-letter ex. "Hello"
# the H points to a note and the note now has again its own dictionary
# Next, E is not part of the note, so added E to it and E gonna points to the note.
# Which again, gonna have a dictionary. There's L keep points to the next note.
# and another L, which have 2 dictionary, and add O and point to the empty dictionary!
# (root)_"Hello" = H-E-L-L-O_(end of the word)


# [Right]
# if I insert the word "minimum"
# The child note gonna points to the next dictionary letter-by-letter. (root)_m-i-n-i-m-u-m_(end)
# BUT what if I insert the word "minimal",
# It's still try the dictionary letter-by-letter but gonna stop it,
# They gonna decide m-i-n-i-m-? < is it gonna u = minimum or a = minimal right?
# So, there's new branch here on 'm' before decide to pick a or u.
# and A note points to the next dictionary which is 'l'
# on 'm' is you go right note which is 'u' you gonna get the word "minimum"
# if you're go left note which is 'a' you gonna get the word "minimal".

class Node:

    def __init__(self):
        self.children = dict()
        self.is_end_of_word = False

class Trie:

    def __init__(self):
        self.root = Node()

    # O(m) - linear runtime complexity
    # m is the length of the word
    def insert(self, word):
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = Node()

            current_node = current_node.children[char]

        current_node.is_end_of_word = True
        # follows the path until we get there
        # Or we have to create new nodes until get there
        # keep processing... until the end at the note then we're set it "End"

    # O(m) - linear runtime complexity
    # m is the length of the word
    def search(self, word):
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False
                # the word that not part of the children dictionary of my current node
                # It's means the word does not exist!

            current_node = current_node.children[char]

        return current_node.is_end_of_word

    # O(m) - linear runtime complexity
    # m is the length of the word
    def delete(self, word):
        self._delete(self.root, word, index=0) # Lets calls the function

    # O(m) - linear runtime complexity
    # m is the length of the word
    def has_prefix(self, prefix): # is it part of the tree or not?
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return False

            current_node = current_node.children[char]

        return True

    # O(m + k)
    # m is the prefix length
    # k is the total number of characters in all suffixes
    def starts_with(self, prefix):
    # We need to explore all the child notes to find words and collect them in the lists
        words = []
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return words

            current_node = current_node.children[char]

        def _dfs(current_node, path):
            if current_node.is_end_of_word:
                words.append(''.join(path))

            for char, child_node in current_node.children.items():
                _dfs(child_node, path + [char])


        _dfs(current_node, list(prefix)) #Never start it with empty list

        return words

    # O(n)
    # n is the number of nodes in the Trie
    def list_words(self):
        words = []

        def _dfs(current_node, path):
            if current_node.is_end_of_word:
                words.append(''.join(path))

            for char, child_node in current_node.children.items():
                _dfs(child_node, path + [char])

        _dfs(self.root, path=[])

        return words


    def _delete(self, current_node, word, index):
        if index == len(word):
            if not current_node.is_end_of_word:
                return False # No need anything, No need to delete anything

            current_node.is_end_of_word = False

            return len(current_node.children) == 0

        char = word[index]
        node = current_node.children.get(char)

        if node is None:
            return False

        delete_current_node = self._delete(node, word, index + 1)
        if delete_current_node:
            del current_node.children[char]
            return len(current_node.children) == 0 and not current_node.is_end_of_word

        return False

        # Go 1 node forward, and increase the index by 1
        # So we can continue the same process down the line
        # this is recursively return T/F.
        # True = delete the current node. False = not gonna delete the current node.
        # empty dic = can still delete all the notes that are no longer necessary.

if __name__ == '__main__':
    trie = Trie()

    trie.insert('hello')
    trie.insert('world')
    trie.insert('mike')
    trie.insert('minimal')
    trie.insert('minimum')

    print(trie.list_words())

    print()

    print(trie.has_prefix('mi'))
    print(trie.starts_with('mi'))

    print()

    trie.delete('minimal')
    print(trie.starts_with('mi'))

    print()

    print(trie.search('minimum'))
    print(trie.search('minimal'))
    print(trie.search('mini'))

    print()

    trie.insert('mini')
    print(trie.starts_with('mi'))