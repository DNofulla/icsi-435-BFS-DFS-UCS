from Graphs_and_Helpers import map_of_vertex, getAdjacentLetterToExplore, getIndex, getVertex, graph1_vertex, graph1_matrix


def BFS_Vertex_Stack_G1():
    stack = []
    stack.append('S')
    visited_letters = set()
    expanded_steps = []

    while len(stack) != 0:
        path = stack.pop(0)
        letter_to_be_explored = path[-1]

        if letter_to_be_explored not in expanded_steps:
            expanded_steps.append(letter_to_be_explored)

        if letter_to_be_explored not in visited_letters:
            visited_letters.add(letter_to_be_explored)

        if letter_to_be_explored == 'G':
            return (path, expanded_steps)

        for adjacent_letter_to_be_explored in graph1_vertex[letter_to_be_explored]:
            if adjacent_letter_to_be_explored not in visited_letters:
                stack.append(path + adjacent_letter_to_be_explored)


def BFS_Vertex_Recursion_G1_Run():
    return BFS_Vertex_Recursion_G1('S', [])


def BFS_Vertex_Recursion_G1(letter_to_explore, path, expanded_steps=[]):

    if letter_to_explore not in expanded_steps:
        expanded_steps.append(letter_to_explore)

    if letter_to_explore not in path:
        path.append(letter_to_explore)

    if letter_to_explore == 'G':
        return (path, expanded_steps)

    for adjacent_letter_to_explore in graph1_vertex[letter_to_explore][::-1]:
        if adjacent_letter_to_explore not in expanded_steps:
            expanded_steps.append(adjacent_letter_to_explore)

        if adjacent_letter_to_explore not in path:
            return BFS_Vertex_Recursion_G1(adjacent_letter_to_explore, path, expanded_steps)


def BFS_Matrix_Stack_G1():
    stack = []
    stack.append('S')
    visited_letters = set()
    expanded_steps = []

    while len(stack) != 0:
        path = stack.pop(0)
        letter_to_be_explored = path[-1]

        if letter_to_be_explored not in expanded_steps:
            expanded_steps.append(path[-1])

        if letter_to_be_explored not in visited_letters:
            visited_letters.add(letter_to_be_explored)

        if letter_to_be_explored == 'G':
            return (path, expanded_steps)

        for adjacent_letter_index in range(len(graph1_matrix[getIndex(letter_to_be_explored)])):
            if adjacent_letter_index not in visited_letters and graph1_matrix[getIndex(letter_to_be_explored)][adjacent_letter_index] == 1:
                adjacent_letter_to_explore = getAdjacentLetterToExplore(
                    adjacent_letter_index)
                if adjacent_letter_to_explore not in visited_letters:
                    stack.append(path + adjacent_letter_to_explore)


def BFS_Matrix_Recursion_G1_Run():
    return BFS_Matrix_Recursion_G1('S', [])


def BFS_Matrix_Recursion_G1(letter_to_explore, path, expanded_steps=[]):
    index_to_explore = getIndex(letter_to_explore)

    if index_to_explore not in path:
        path = path + [index_to_explore]

    if index_to_explore not in expanded_steps:
        expanded_steps.append(index_to_explore)

    if index_to_explore == getIndex('G'):
        path = [map_of_vertex[letter] for letter in path]
        expanded_steps = [map_of_vertex[letter]
                          for letter in expanded_steps]
        return (path, expanded_steps)

    for adjacent_index_to_explore in range(len(graph1_matrix[index_to_explore])):
        if adjacent_index_to_explore not in expanded_steps and graph1_matrix[index_to_explore][adjacent_index_to_explore] == 1:
            return BFS_Matrix_Recursion_G1(map_of_vertex[adjacent_index_to_explore], path, expanded_steps)


def run_bfs_g1_tests():
    print("PRINTING BFS FOR G1 - All Correct except Recursive for both Vertex and Matrix")

    (path, expanded_steps) = BFS_Vertex_Stack_G1()
    print("BFS Expanded Steps Vertex w/ Stack G1:")
    print("[" + " -> ".join(expanded_steps) + "]")
    print("BFS Path Vertex w/ Stack G1:")
    print("[" + " -> ".join(path) + "]")

    print()
    print()

    (path, expanded_steps) = BFS_Vertex_Recursion_G1_Run()
    print("BFS Expanded Steps Vertex w/ Recursion G1:")
    print("[" + " -> ".join(expanded_steps) + "]")
    print("BFS Path Vertex w/ Recursion G1:")
    print("[" + " -> ".join(path) + "]")

    print()
    print()

    (path, expanded_steps) = BFS_Matrix_Stack_G1()
    print("BFS Expanded Steps Matrix w/ Stack G1:")
    print("[" + " -> ".join(expanded_steps) + "]")
    print("BFS Path Matrix w/ Stack G1:")
    print("[" + " -> ".join(path) + "]")

    print()
    print()

    (path, expanded_steps) = BFS_Matrix_Recursion_G1_Run()
    print("BFS Expanded Steps Matrix w/ Recursion G1:")
    print("[" + " -> ".join(expanded_steps) + "]")
    print("BFS Path Matrix w/ Recursion G1:")
    print("[" + " -> ".join(path) + "]")

    print()
    print()
    return
