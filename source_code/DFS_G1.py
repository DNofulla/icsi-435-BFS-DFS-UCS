from Graphs_and_Helpers import map_of_vertex, getAdjacentLetterToExplore, getIndex, getVertex, graph1_vertex, graph1_matrix


def DFS_Vertex_Stack_G1():
    stack = []
    stack.append('S')
    visited_letters = []
    expanded_steps = []

    while len(stack) != 0:
        path = stack[-1]
        letter_to_be_explored = path[-1]

        expanded_steps.append(letter_to_be_explored)

        if letter_to_be_explored not in visited_letters:
            visited_letters.append(letter_to_be_explored)

        if letter_to_be_explored == 'G':
            return (path, expanded_steps)

        for adjacent_letter_to_explore in graph1_vertex[letter_to_be_explored][::-1]:
            stack.append(
                path + adjacent_letter_to_explore) if adjacent_letter_to_explore not in visited_letters else None


def DFS_Vertex_Recursion_G1_Run():
    return DFS_Vertex_Recursion_G1('S', [])


def DFS_Vertex_Recursion_G1(letter_to_explore, path, expanded_steps=[]):

    if letter_to_explore not in expanded_steps:
        expanded_steps.append(letter_to_explore)

    if letter_to_explore not in path:
        path.append(letter_to_explore)

    if letter_to_explore == 'G':
        return (path, expanded_steps)

    for adjacent_letter_to_explore in graph1_vertex[letter_to_explore]:
        if adjacent_letter_to_explore not in expanded_steps:
            expanded_steps.append(adjacent_letter_to_explore)

        if adjacent_letter_to_explore not in path:
            return DFS_Vertex_Recursion_G1(adjacent_letter_to_explore, path, expanded_steps)


def DFS_Matrix_Stack_G1():
    stack = []
    stack.append('S')
    visited_letters = []
    expanded_steps = []

    while len(stack) != 0:
        path = stack[-1]
        letter_to_be_explored = path[-1]

        expanded_steps.append(letter_to_be_explored)

        if letter_to_be_explored not in visited_letters:
            visited_letters.append(letter_to_be_explored)

        if letter_to_be_explored == 'G':
            return (path, expanded_steps)

        for adjacent_letter_index in range(len(graph1_matrix[getIndex(letter_to_be_explored)])):
            reverseIndex = len(graph1_matrix[getIndex(
                letter_to_be_explored)]) - 1 - adjacent_letter_index
            if len(graph1_matrix[getIndex(
                letter_to_be_explored)]) - adjacent_letter_index - 1 not in visited_letters and graph1_matrix[getIndex(letter_to_be_explored)][len(graph1_matrix[getIndex(
                    letter_to_be_explored)]) - adjacent_letter_index - 1] == 1:

                adjacent_letter_to_explore = getAdjacentLetterToExplore(
                    reverseIndex)
                if adjacent_letter_to_explore not in visited_letters:
                    stack.append(path + adjacent_letter_to_explore)


def DFS_Matrix_Recursion_G1_Run():
    return DFS_Matrix_Recursion_G1('S', [])


def DFS_Matrix_Recursion_G1(letter_to_explore, path, expanded_steps=[]):
    index_to_explore = getIndex(letter_to_explore)

    if index_to_explore not in path:
        path = path + [index_to_explore]

    if index_to_explore not in expanded_steps:
        expanded_steps.append(index_to_explore)

    if index_to_explore == getIndex('G'):
        path = [map_of_vertex[letter] for letter in path]
        expanded_steps = [map_of_vertex[letter] for letter in expanded_steps]
        return (path, expanded_steps)

    for adjacent_index_to_explore in range(len(graph1_matrix[index_to_explore])):
        if adjacent_index_to_explore not in expanded_steps and graph1_matrix[index_to_explore][adjacent_index_to_explore] == 1:
            return DFS_Matrix_Recursion_G1(map_of_vertex[adjacent_index_to_explore], path, expanded_steps)


def run_dfs_g1_tests():

    print("PRINTING DFS FOR G1 - All Correct")

    (path, expanded_steps) = DFS_Vertex_Stack_G1()
    print("DFS Expanded Steps Vertex w/ Stack G1:")
    print("[" + " -> ".join(expanded_steps) + "]")
    print("DFS Path Vertex w/ Stack G1:")
    print("[" + " -> ".join(path) + "]")

    print()
    print()

    (path, expanded_steps) = DFS_Vertex_Recursion_G1_Run()
    print("DFS Expanded Steps Vertex w/ Recursion G1:")
    print("[" + " -> ".join(expanded_steps) + "]")
    print("DFS Path Vertex w/ Recursion G1:")
    print("[" + " -> ".join(path) + "]")

    print()
    print()

    (path, expanded_steps) = DFS_Matrix_Stack_G1()
    print("DFS Expanded Steps Matrix w/ Stack G1:")
    print("[" + " -> ".join(expanded_steps) + "]")
    print("DFS Path Matrix w/ Stack G1:")
    print("[" + " -> ".join(path) + "]")

    print()
    print()

    (path, expanded_steps) = DFS_Matrix_Recursion_G1_Run()
    print("DFS Expanded Steps Matrix w/ Recursion G1:")
    print("[" + " -> ".join(expanded_steps) + "]")
    print("DFS Path Matrix w/ Recursion G1:")
    print("[" + " -> ".join(path) + "]")

    print()
    print()
    return
