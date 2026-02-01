# Hashmap

# Hashmap stores data using "Key-Value Pairs"
# Each key run through a hash function that determines,
# where the value should be stored

# It's like keys -> Hash function to find -> index -> value
# Keys have to check up by the Hash functions rules first,
# To identify the index, then get the value
# Hash functions act like a "center filter"

# Collision Handling: approached in different ways.
# When a collision happens (two keys land on index 3), you just keep adding them to that same list at index 3.
# if the index is full, I still can jump from the elements to find my element

# Imagine a mail room in the mailbox for every employee
# Instead of sorting through all the mail one by one
# My mailbox is #01, her mailbox is #02, his mailbox is #03
# I know exactly where to put it. Her/His knows too

class Hashmap:
    def __init__(self, capacity):
        self. capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    # O(1) - constant
    def __len__(self):
        return self.size # we need to keep track of that

    # Average: O(1) - constant
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function
    def __contains__(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for k, v in bucket: #just looking for the correct key
            if k == key:
                return True

        return False

    # Average: O(1) - constant
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function
    def put(self, key, value):
        index = self._hash_function(key)
        bucket = self.buckets[index] # must defined 'bucket' fist

        for i, (k, v) in enumerate(bucket): # We are appending elements.
            if k == key:
                bucket[i] = (key, value) #update existing key
                return #exit the function since we are done

        # if the loop finishes without finding the key, add a new one
        bucket.append((key, value)) # go through each branch and leave the for loop without breaking it.
        self.size += 1

    # Average: O(1) - constant
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function
    def get(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for k, v in bucket: # I return the value that belongs to the key value pair
            if k == key:
                return v
        raise KeyError('Key not found')

    # Average: O(1) - constant
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function
    def remove(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                break
        else:
            raise KeyError('Key not found')

    # O(n) - linear time
    # We need to go through all the buckets
    def keys(self):
        return [k for bucket in self.buckets for k, _ in bucket] # go to all the buckets, and get all the key value pairs

    # O(n) - linear time
    def values(self):
        return [v for bucket in self.buckets for _, v in bucket]

    # O(n) - linear time
    def items(self):
        return [(k, v) for bucket in self.buckets for k, v in bucket]

    # O(k) - linear in key length
    # The longer your key is, the larger the effort or the more effort this function will have
    def _hash_function(self, key):
        key_string = str(key) # we are going to allow string as keys
        hash_result = 0

        for c in key_string: # ord = ordinal
            hash_result = (hash_result * 31 + ord(c)) % self.capacity # we will always have a number that is between 0 and capacity minus one

        return hash_result

if __name__ == '__main__':
    import uuid
    import matplotlib.pyplot as plt

    # You are putting 100,000 items into only 100 buckets.
    # $$Load Factor (\alpha) = n/k

    # n = number of entries (100,000)
    # k = number of buckets (100)

    # "Average O(1)" time complexity is currently behaving like O(n)
    # because Python has to search through a list of 1,000 items every time you call

    hash_map = Hashmap(100)

    for _ in range(100000):
        hash_map.put(uuid.uuid4(), 'some_value')

    x = []
    y = []

    for i, bucket in enumerate(hash_map.buckets):
        x.append(i)
        y.append(len(bucket))

    plt.bar(x, y)
    plt.show()