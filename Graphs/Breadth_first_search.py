from collections import deque

graph = dict()
graph['A'] = ['B', 'G', 'D']
graph['B'] = ['A', 'F', 'E']
graph['C'] = ['F', 'H']
graph['D'] = ['F', 'A']
graph['E'] = ['B', 'G']
graph['F'] = ['B', 'D', 'C']
graph['G'] = ['A', 'E']
graph['H'] = ['C']


def breadth_first_search(graph, root):
    visited_vertices = []
    graph_queue = deque([root])
    visited_vertices.append(root)
    node = root

    while len(graph_queue) > 0:
        print("graph_queue: ", graph_queue)

        node = graph_queue.popleft()
        adj_nodes = graph[node]
        remaining_elements = set(adj_nodes).difference(set(visited_vertices))

        print("node: ", node)
        print("adj_nodes: ", sorted(adj_nodes))
        print("remaining_elements: ", sorted(remaining_elements))
        print("visited_vertices: ", visited_vertices)
        print()

        if len(remaining_elements) > 0:
            for element in sorted(remaining_elements):
                visited_vertices.append(element)
                graph_queue.append(element)

    return visited_vertices


if __name__ == "__main__":
    path = breadth_first_search(graph, 'B')
    print(path)
