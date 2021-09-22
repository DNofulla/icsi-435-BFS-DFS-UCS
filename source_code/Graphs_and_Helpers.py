map_of_vertex = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H',
    8: 'P',
    9: 'Q',
    10: 'R',
    11: 'S',
}

graph1_vertex = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D', 'F'],
    'D': ['B', 'C', 'E', 'S'],
    'E': ['D', 'H', 'R', 'S'],
    'F': ['C', 'G', 'R'],
    'G': ['F'],
    'H': ['E', 'P', 'Q'],
    'P': ['H', 'Q', 'S'],
    'Q': ['H', 'P'],
    'R': ['E', 'F'],
    'S': ['D', 'E', 'P'],
}

graph1_matrix = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
                 [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0]]


graph2_vertex = {
    'A': [],
    'B': ['A'],
    'C': ['A'],
    'D': ['B', 'C', 'E'],
    'E': ['H', 'R'],
    'F': ['C', 'G'],
    'G': [],
    'H': ['P', 'Q'],
    'P': ['Q'],
    'Q': [],
    'R': ['F'],
    'S': ['D', 'E', 'P'],
}

graph2_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                 [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0]]

graph3_vertex = {
    'A': {'B': 2, 'C': 2},
    'B': {'A': 2, 'D': 1},
    'C': {'A': 2, 'D': 8, 'F': 3},
    'D': {'B': 1, 'C': 8, 'E': 2, 'S': 3},
    'E': {'D': 2, 'H': 8, 'R': 2, 'S': 9},
    'F': {'C': 3, 'G': 2, 'R': 2},
    'G': {'F': 2},
    'H': {'E': 8, 'P': 4, 'Q': 4},
    'P': {'H': 4, 'Q': 15, 'S': 1},
    'Q': {'H': 4, 'P': 15},
    'R': {'E': 2, 'F': 2},
    'S': {'D': 3, 'E': 9, 'P': 1},
}


graph3_matrix = [[0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [2, 0, 0, 8, 0, 3, 0, 0, 0, 0, 0, 0],
                 [0, 1, 8, 0, 2, 0, 0, 0, 0, 0, 0, 3],
                 [0, 0, 0, 2, 0, 0, 0, 8, 0, 0, 2, 9],
                 [0, 0, 3, 0, 0, 0, 2, 0, 0, 0, 2, 0],
                 [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 8, 0, 0, 0, 4, 4, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 4, 0, 15, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0, 4, 15, 0, 0, 0],
                 [0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 3, 9, 0, 0, 0, 1, 0, 0, 0]]

graph4_vertex = {
    'A': {},
    'B': {'A': 2},
    'C': {'A': 2},
    'D': {'B': 1, 'C': 8, 'E': 2},
    'E': {'H': 8, 'R': 2},
    'F': {'C': 3, 'G': 2},
    'G': {},
    'H': {'P': 4, 'Q': 4},
    'P': {'Q': 15},
    'Q': {},
    'R': {'F': 2},
    'S': {'D': 3, 'E': 9, 'P': 1},
}

graph4_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 8, 0, 2, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 2, 0],
                 [0, 0, 3, 0, 0, 0, 2, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 8, 0, 0, 0, 4, 4, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 3, 9, 0, 0, 0, 1, 0, 0, 0]]


def getIndex(char: str):
    for i in range(len(map_of_vertex)):
        if map_of_vertex[i] == char:
            return i
    return -1


def getVertex(index: int):
    if index < len(map_of_vertex):
        return map_of_vertex[index]
    return -1


def getAdjacentLetterToExplore(some_reverse_index):
    return [letter_value for key_value, letter_value in map_of_vertex.items() if key_value == some_reverse_index][0]
