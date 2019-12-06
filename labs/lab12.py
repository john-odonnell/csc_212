def build_adjacency_matrix() -> list:
    """ Create the adjacency matrix for a graph.
    Return the matrix as a two dimensional list.
    """
    matrix = [[0, 1, 1, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 0, 1],
              [0, 0, 0, 1, 1, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 1, 0]]
    return matrix


def dfs(graph, initial) -> list:
    """ Traverse the graph using depth-first search.
    You should use the adjacency matrix you created,
    where the source node is the same as the one as seen
    in the slides
    """
    checked = []
    return _dfs(graph, initial, checked)


def _dfs(graph, current, checked) -> list:
    if len(checked) == len(graph):
        return checked
    elif current not in checked:
        checked.append(current)
        for i in range(len(graph[current - 1])):
            if graph[current - 1][i] == 1 and (i + 1) not in checked:
                checked = _dfs(graph, i + 1, checked)
        return checked


def build_weighted_adjacency_matrix() -> list:
    """ Creates and returns a weighted adjacency matrix.
    """
    matrix = [[0, 5, 1, 0, 3, 0, 0, 0, 0],
              [0, 0, 0, 8, 3, 0, 0, 0, 0],
              [0, 0, 0, 0, 4, 10, 0, 0, 0],
              [0, 0, 0, 0, 5, 0, 0, 9, 0],
              [0, 0, 0, 0, 0, 4, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 0, 11],
              [0, 0, 0, 6, 3, 0, 0, 2, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 14, 1, 0]]
    return matrix


def mst(graph, initial) -> int:
    """ Using Kruskal's algorithm, build a minimal spanning tree.
    Returns the sum of the edges of the built tree.
    """
    trees = [[1], [2], [3], [4], [5], [6], [7], [8], [9]]
    min_queue = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if len(min_queue) == 0:
                min_queue.append([i, graph[i - 1][j - 1], j])
            else:
                k = 0


def main():
    matrix = build_adjacency_matrix()
    checked = dfs(matrix, 1)
    print(checked)


if __name__ == "__main__":
    main()
