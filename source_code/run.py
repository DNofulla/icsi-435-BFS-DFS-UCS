import numpy as np

map_of_vertex = {
    0: 'S',
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D',
    5: 'E',
    6: 'F',
    7: 'H',
    8: 'P',
    9: 'Q',
    10: 'R',
    11: 'G',
}


def getIndex(char: str):
    for i in range(len(map_of_vertex)):
        if map_of_vertex[i] == char:
            return i
    return -1


def getVertex(index: int):
    if index < len(map_of_vertex):
        return map_of_vertex[index]
    return -1


# graph_1_vertex_list = {
#     'S': ['D', 'E', 'P'],
#     'A': ['B', 'C'],
#     'B': ['A', 'D'],
#     'C': ['A', 'D', 'F'],
#     'D': ['S', 'B', 'C', 'E'],
#     'E': ['S', 'D', 'H', 'R'],
#     'F': ['C', 'G', 'R'],
#     'H': ['E', 'P', 'Q'],
#     'P': ['S', 'H', 'Q'],
#     'Q': ['H', 'P'],
#     'R': ['E', 'F'],
#     'G': ['F']
# }

# graph_2_vertex_list = {
#     'S': ['D', 'E', 'P'],
#     'A': [],
#     'B': ['A'],
#     'C': ['A'],
#     'D': ['B', 'C', 'E'],
#     'E': ['H', 'R'],
#     'F': ['C', 'G'],
#     'H': ['P', 'Q'],
#     'P': ['Q'],
#     'Q': [],
#     'R': ['F'],
#     'G': []
# }

# graph_3_vertex_list = {
#     'S': {'D': 3, 'E': 9, 'P': 1},
#     'A': {'B': 2, 'C': 2},
#     'B': {'A': 2, 'D': 1},
#     'C': {'A': 2, 'D': 8, 'F': 3},
#     'D': {'S': 3, 'B': 1, 'C': 8, 'E': 2},
#     'E': {'S': 9, 'D': 2, 'H': 8, 'R': 2},
#     'F': {'C': 3, 'G': 2, 'R': 2},
#     'H': {'E': 8, 'P': 4, 'Q': 4},
#     'P': {'S': 1, 'H': 4, 'Q': 15},
#     'Q': {'H': 4, 'P': 15},
#     'R': {'E': 2, 'F': 2},
#     'G': {'F': 2}
# }

# graph_4_vertex_list = {
#     'S': [('D', 3), ('E', 9), ('P', 1)],
#     'A': [],
#     'B': [('A', 2)],
#     'C': [('A', 2)],
#     'D': [('B', 1), ('C', 8), ('E', 2)],
#     'E': [('H', 8), ('R', 2)],
#     'F': [('C', 3), ('G', 2)],
#     'H': [('P', 4), ('Q', 4)],
#     'P': [('Q', 15)],
#     'Q': [],
#     'R': [('F', 2)],
#     'G': []
# }


g1_vertex = {}
g2_vertex = {}
g3_vertex = {}
g4_vertex = {}

g1_matrix = [[]]
g2_matrix = [[]]
g3_matrix = [[]]
g4_matrix = [[]]


with open('edges.txt', 'r') as file:
    number_of_vertices = int(file.readline())
    number_of_edges = int(file.readline())

    # Initializing Vertices and Arrays
    g1_matrix = np.zeros((number_of_vertices, number_of_vertices), dtype=int)
    g2_matrix = np.zeros((number_of_vertices, number_of_vertices), dtype=int)
    g3_matrix = np.zeros((number_of_vertices, number_of_vertices), dtype=int)
    g4_matrix = np.zeros((number_of_vertices, number_of_vertices), dtype=int)

    for i in range(len(map_of_vertex)):
        g1_vertex[getVertex(i)] = []
        g2_vertex[getVertex(i)] = []
        g3_vertex[getVertex(i)] = {}
        g4_vertex[getVertex(i)] = {}

    for i in range(number_of_edges):
        line = file.readline().split(",")

        # Update G1 - Just Letters in Array
        g1_matrix[getIndex(line[0])][getIndex(line[1])] = 1
        g1_matrix[getIndex(line[1])][getIndex(line[0])] = 1
        prev_array_1 = g1_vertex[line[0]]
        prev_array_2 = g1_vertex[line[1]]
        g1_vertex[line[0]] = [*prev_array_1, line[1]]
        g1_vertex[line[1]] = [*prev_array_2, line[0]]

        # Update G2 - Just Letters in Array
        g2_matrix[getIndex(line[0])][getIndex(line[1])] = 1
        prev_array_1 = g2_vertex[line[0]]
        g2_vertex[line[0]] = [*prev_array_1, line[1]]

        # Update G3 - Letters in Dictionary with Number
        g3_matrix[getIndex(line[0])][getIndex(line[1])] = int(line[2])
        g3_matrix[getIndex(line[1])][getIndex(line[0])] = int(line[2])
        prev_array_1 = g3_vertex[line[0]]
        prev_array_2 = g3_vertex[line[1]]
        g3_vertex[line[0]] = {**prev_array_1, line[1]: int(line[2])}
        g3_vertex[line[1]] = {**prev_array_2, line[0]: int(line[2])}

        # Update G4
        g4_matrix[getIndex(line[0])][getIndex(line[1])] = int(line[2])
        prev_array_1 = g4_vertex[line[0]]
        g4_vertex[line[0]] = {**prev_array_1, line[1]: int(line[2])}


print("VERTEX GRAPH 1")
print(g1_vertex)
print()
print("VERTEX GRAPH 2")
print(g2_vertex)
print()
print("VERTEX GRAPH 3")
print(g3_vertex)
print()
print("VERTEX GRAPH 4")
print(g4_vertex)


print()
print()


print("ADJACENCY MATRIX GRAPH 1")
print(g1_matrix)
print()
print("ADJACENCY MATRIX GRAPH 2")
print(g2_matrix)
print()
print("ADJACENCY MATRIX GRAPH 3")
print(g3_matrix)
print()
print("ADJACENCY MATRIX GRAPH 4")
print(g4_matrix)


def DFS_Vertex_G1():
    return
