class vertex:
    def __init__(self, key: int, neighbors=None):
        self.key: int = key
        self.neighbors: edges_list = neighbors


class edge:
    def __init__(self, this_vertex=None, next_vertex=None):
        self.this_vertex: vertex = this_vertex
        self.next_vertex: vertex = next_vertex


class edges_list:
    def __init__(self, root_node, first_neighbor=None):
        self.root_node: vertex = root_node
        self.first_neighbor: edge = first_neighbor
        self.num_neighbors: int = 0

    def add_edge(self, node: vertex):
        new_edge = edge(node)
        if self.num_neighbors == 0:
            self.first_neighbor = new_edge
        else:
            this_neighbor = self.first_neighbor
            while this_neighbor.next_vertex is not None:
                this_neighbor = this_neighbor.next_vertex
            this_neighbor.next_vertex = new_edge
        self.num_neighbors += 1


class graph:
    def __init__(self):
        self.num_vertecies: int = 0
        self.first_vertex: vertex = None

    def add_vertex(self, key: int):
        new_vertex = vertex(key)
        if self.num_vertecies == 0:
            self.first_vertex = new_vertex

