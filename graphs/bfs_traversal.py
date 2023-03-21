from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict()
        for vertex in range(1, vertices + 1):
            self.graph[vertex] = []

    def add_edge(self, edges):
        self.graph[edges[0]].append(edges[1])


def bfs(start_node, graph, weight):
    queue = []
    visited_nodes = []
    queue.append(start_node)
    visited_nodes.append(start_node)
    result = defaultdict()
    for vertex in range(1, len(graph.graph) + 1):
        result[vertex] = 0

    while queue:
        node = queue.pop(0)
        neighbours = graph.graph[node]
        for neighbour in neighbours:
            if neighbour not in visited_nodes:
                queue.append(neighbour)
                visited_nodes.append(neighbour)
                result[neighbour] += result[node] + weight

    for node in graph.graph.keys():
        if node == start_node:
            del result[node]
        elif node in visited_nodes:
            continue
        else:
            result[node] = -1
    return result.values()


if __name__ == '__main__':
    weight = 6
    edges = [[2, 1], [2, 2], [1, 3], [3, 4]]
    start_node = 2
    graph = Graph(5)

    for edge in edges:
        graph.add_edge(edge)

    print(bfs(start_node, graph, weight))
