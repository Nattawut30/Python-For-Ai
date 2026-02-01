#Graph
from collections import deque


# basically consists of a bunch of nodes and a bunch of edges
# these notes can be connected by edges
# looks like a tree but have a specific limitation = No cycle.

# undirected graph = The connection go both ways. one connected two. two connected one.
# directed graph = Every connection needs to have a direction. one goes to two, but two doesn't need to go to one.
# weighted graph = Each connection has a certain weight to it. A cost. A speed. what's the fastest road 1-5?
# Every single connection have a direction

# Imagine a spider webs that have a complex designed and connected together
# Each points called "notes" connected to another notes and so on.

# BFS = Breadth First Search
# DFS = Depth First Search

# adjacency listed (normal connected)
# 1: 2, 4, 5
# 2: 1, 3
# 3: 2, 4, 5, 6

# adjacency matrix (connected 1, disconnected: 0)
# 1, 2, 3, 4
# 1 [1] [0]
# 2
# 3
# 4

class Graph:

    def __init__(self, directed=False):
        self.directed = directed
        self.adjacency_list = dict()

    def __repr__(self):
        graph_str = ""
        for node, neighbors in self.adjacency_list.items():
            graph_str += f"{node} -> {neighbors}\n"
        return graph_str

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = set()
        else:
            raise ValueError("Node Exists Already")

    def remove_node(self, node):
        if node not in self.adjacency_list:
            raise ValueError("Node Does Not Exist")

        del self.adjacency_list[node]

        for start_node in self.adjacency_list:
            self.adjacency_list[start_node] = {
                n for n in self.adjacency_list[start_node]
                if (n[0] if isinstance(n, tuple) else n) != node
            }

    def add_edge(self, from_node, to_node, weight=None):
        if from_node not in self.adjacency_list:
            self.add_node(from_node) # add the connection from 1 to 2

        if to_node not in self.adjacency_list:
            self.add_node(to_node)

        if weight is None:
            self.adjacency_list[from_node].add(to_node)
            if not self.directed:
                self.adjacency_list[to_node].add(from_node) # then it goes both ways
        else:
            self.adjacency_list[from_node].add((to_node, weight))
            if not self.directed:
                self.adjacency_list[to_node].add((from_node, weight))

    def remove_edge(self, from_node, to_node):
        if from_node not in self.adjacency_list:
            raise ValueError(f"Node {from_node} does not exist")

            # List Comprehension
        self.adjacency_list[from_node] = {
            neighbor for neighbor in self.adjacency_list[from_node]
            if (neighbor[0] if isinstance(neighbor, tuple) else neighbor) != to_node
            }

            # Undirected = Deleted ways back too
        if not self.directed and to_node in self.adjacency_list:
            self.adjacency_list[to_node] = {
                neighbor for neighbor in self.adjacency_list[to_node]
                if (neighbor[0] if isinstance(neighbor, tuple) else neighbor) != from_node
            }

    def get_neighbors(self, node):
        return self.adjacency_list.get(node, set()) # get all the neighbors and empty set by default.

    def has_node(self, node):
        return node in self.adjacency_list

    def has_edge(self, from_node, to_node):
        if from_node in self.adjacency_list:
            return to_node in self.adjacency_list[from_node]
        return False

    def get_nodes(self): # return a lists of self, adjacency list
        return list(self.adjacency_list.keys())

    def get_edges(self):
        edges = []
        for from_node, neighbors in self.adjacency_list.items():
            for to_node in neighbors:
                edges.append((from_node, to_node))

        return edges

    def bfs(self, start): #Queue, FIFO
        visited = set()
        queue = [start]
        order = []

        while queue: # we wanna get elements to be processed
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbors = sorted(self.get_neighbors(node))
                for neighbor in neighbors:
                    if isinstance(neighbor, tuple):
                        neighbor = neighbor[0]
                    if neighbor not in visited:
                        queue.append(neighbor)

        return order


    def dfs(self, start): #Stacks, LILO
        visited = set()
        stack = [start]
        order = []

        while stack:  # we wanna get elements to be processed
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbors = self.get_neighbors(node)
                for neighbor in sorted(neighbors, reverse=True):
                    if isinstance(neighbor, tuple):
                        neighbor = neighbor[0]
                    if neighbor not in visited:
                        stack.append(neighbor)

        return order

    def dijkstra(self, start):
        import heapq
        distances = {node: float("inf") for node in self.adjacency_list}
        distances[start] = 0
        heap = [(0, start)]

        while heap:
            current_distance, current_node = heapq.heappop(heap)
            if current_distance > distances[current_node]:
                continue
            neighbors = self.adjacency_list.get(current_node, set())
            for neighbor in neighbors:
                if isinstance(neighbor, tuple):
                    to, weight = neighbor
                else:
                    to, weight = neighbor, 1
                distance = current_distance + weight
                if distance < distances[to]:
                    distances[to] = distance
                    heapq.heappush(heap, (distance, to))

        return distances

    def shortest_path(self, start, end):
        import heapq
        distances = {node: float("inf") for node in self.adjacency_list}
        previous = {node: None for node in self.adjacency_list}
        distances[start] = 0
        heap = [(0, start)]

        while heap:
            current_distance, current_node = heapq.heappop(heap)
            if current_node == end:
                break
            if current_distance > distances[current_node]:
                continue
            neighbors = self.adjacency_list.get(current_node, set())
            for neighbor in neighbors:
                if isinstance(neighbor, tuple):
                    to, weight = neighbor
                else:
                    to, weight = neighbor, 1
                distance = current_distance + weight
                if distance < distances[to]:
                    distances[to] = distance
                    previous[to] = current_node
                    heapq.heappush(heap, (distance, to))
        path = []
        node = end
        while node is not None:
            path.append(node)
            node = previous[node]
        path.reverse()
        if path[0] == start:
            return path
        return []

    def to_adjacency_matrix(self):
        nodes = self.get_nodes()
        index = {node: i for i, node in enumerate(nodes)}
        size = len(nodes)
        matrix = [[0 for _ in range(size)] for _ in range(size)]
        for from_node, neighbors in self.adjacency_list.items():
            for to_node in neighbors:
                if isinstance(to_node, tuple):
                    to, weight = to_node
                    matrix[index[from_node]][index[to]] = weight
                else:
                    matrix[index[from_node]][index[to_node]] = 1
        return matrix

if __name__ == "__main__":
    g = Graph(directed=True)

    # g.add_node('A')
    # g.add_node('B')
    # g.add_node('C')
    # g.add_node('D')
    # g.add_node('E')
    # g.add_node('F')
    # g.add_node('G')
    # g.add_node('H')
    # g.add_node('I')

    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 10)
    g.add_edge('B', 'C', 1)
    g.add_edge('B', 'D', 1)
    g.add_edge('D', 'C', 1)
    g.add_edge('A', 'E', 1)
    g.add_edge('E', 'F', 1)
    g.add_edge('G', 'F', 1)
    g.add_edge('F', 'H', 1)
    g.add_edge('H', 'I', 1)
    g.add_edge('I', 'G', 100)

    print(g)

    import numpy as np
    print(np.array(g.to_adjacency_matrix()))
    print()

    print("BFS from A:", g.bfs('A'))
    print("DFS from A:", g.dfs('A'))
    print("Dijkstra from A:", g.dijkstra('A'))
    print("shortest_path from A to C:", g.shortest_path('A', 'C'))
