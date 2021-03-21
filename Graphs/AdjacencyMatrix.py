graph = {'A': ['B', 'C'], 'B': ['E', 'A'], 'C': ['A', 'B', 'E', 'F'], 'E': ['B', 'C'], 'F': ['C']}

matrix_elements = sorted(graph.keys())
cols = rows = len(matrix_elements)

adjacency_matrix = [[0 for x in range(rows)] for y in range(cols)]
edges_list = []

for key in matrix_elements:
    for neighbour in graph[key]:
        edges_list.append((key, neighbour))

print(matrix_elements)

for edge in edges_list:
    index_of_first_vertex = matrix_elements.index(edge[0])
    index_of_second_vertex = matrix_elements.index(edge[1])
    print(index_of_first_vertex, index_of_second_vertex)
    adjacency_matrix[index_of_first_vertex][index_of_second_vertex] = 1

print(adjacency_matrix)