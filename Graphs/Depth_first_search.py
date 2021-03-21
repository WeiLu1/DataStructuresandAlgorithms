graph = dict()
graph['A'] = ['B', 'G', 'D']
graph['B'] = ['A', 'F', 'E']
graph['C'] = ['F', 'H']
graph['D'] = ['F', 'A']
graph['E'] = ['B', 'G']
graph['F'] = ['B', 'D', 'C']
graph['G'] = ['A', 'E']
graph['H'] = ['C']


def depth_first_search(graph, root):
    visited_vertices = []
    graph_stack = [root]
    node = root

    while len(graph_stack) > 0:
        if node not in visited_vertices:
            visited_vertices.append(node)

        adj_nodes = graph[node]

        if set(adj_nodes).issubset(set(visited_vertices)):
            graph_stack.pop()
        if len(graph_stack) > 0:
            node = graph_stack[-1]
            continue
        else:
            remaining_elements = set(adj_nodes).difference(set(visited_vertices))

        first_adj_node = sorted(remaining_elements)[0]
        graph_stack.append(first_adj_node)
        node = first_adj_node

    return visited_vertices
