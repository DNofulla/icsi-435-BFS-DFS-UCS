from Graphs_and_Helpers import map_of_vertex, getIndex, getVertex, graph1_vertex, graph1_matrix, graph2_vertex, graph2_matrix

# VERTEX


def DFS_Vertex_Stack_G1(ch: str, visited=[], progress=[]):
    stack = []
    stack.append(ch)

    while(len(stack) != 0):
        ch = stack.pop()
        if ch not in visited:
            progress.append(ch)
            print(f"Exploring Node {ch}")
            for letter in graph1_vertex[ch][::-1]:
                stack.append(letter)
            visited.append(ch)
            print(f"Finished Exploring Node {ch}")
    return [visited, progress]


def DFS_Vertex_Recursion_G1(ch: str, visited=[], progress=[]):
    if ch == 'G':
        progress.append(ch)
        print(f"Exploring Node {ch}")
        visited.append(ch)
        print(f"Finished Exploring Node {ch}")
        return [visited, progress]
    else:
        print(f"Exploring Node {ch}")
        progress.append(ch)
        for letter in graph1_vertex[ch]:
            if letter not in progress and letter not in visited:
                DFS_Vertex_Recursion_G1(letter, visited, progress)
        progress.pop()
        visited.append(ch)
        print(f"Finished Exploring Node {ch}")
    return [visited, progress]


# MATRIX
def DFS_Matrix_Stack_G1(ch: str, visited=[], progress=[]):
    stack = []
    stack.append(ch)

    while(len(stack) != 0):
        ch = stack.pop()
        index = getIndex(ch)

        if ch not in visited:
            progress.append(ch)
            print(f"Exploring Node {ch}")
            for i in range(12):
                if graph1_matrix[index][i] > 0 and graph1_matrix[i][index] > 0:
                    stack.append(getVertex(i))
            print(f"Finished Exploring Node {ch}")
    return [visited, progress]


def DFS_Matrix_Recursion_G1(ch: str, visited=[], progress=[]):

    index = getIndex(ch)

    if ch == 'G':
        progress.append(ch)
        print(f"Exploring Node {ch}")
        visited.append(ch)
        print(f"Finished Exploring Node {ch}")
        return [visited, progress]
    else:
        print(f"Exploring Node {ch}")
        progress.append(ch)
        for i in range(12):
            if getVertex(i) not in progress and getVertex(i) not in visited:
                if graph1_matrix[index][i] > 0 and graph1_matrix[i][index] > 0:
                    DFS_Matrix_Recursion_G1(getVertex(i), visited, progress)
        visited.append(ch)
        print(f"Finished Exploring Node {ch}")
    return [visited, progress]


# DFS G2
def DFS_Vertex_Stack_G2(ch: str, visited=[], progress=[]):
    stack = []
    stack.append(ch)

    while(len(stack)):
        ch = stack.pop()
        print(f"Exploring Node {ch}")
        if ch not in visited:
            visited.append(ch)
        for letter in graph2_vertex[ch][::-1]:
            if letter not in visited:
                stack.append(letter)
        print(f"Finished Exploring Node {ch}")
    return [visited, progress]


def DFS_Vertex_Recursion_G2(ch: str, visited=[], progress=[]):
    if (ch == 'G'):
        progress.append(ch)
        print(f"Exploring Node {ch}")
        progress.pop()
        visited.append(ch)
        print(f"Finished Exploring Node {ch}")
        return [visited, progress]
    else:
        progress.append(ch)
        print(f"Exploring Node {ch}")
        for letter in graph2_vertex[ch]:
            if letter not in progress and letter not in visited:
                DFS_Vertex_Recursion_G2(letter, visited, progress)
        visited.append(ch)
        progress.pop()
        print(f"Finished Exploring Node {ch}")
    return [visited, progress]


def DFS_Matrix_Stack_G2(ch: str, visited=[], progress=[]):
    stack = []
    stack.append(ch)

    while(len(stack) != 0):
        ch = stack.pop()
        if ch not in visited:
            progress.append(ch)
            index = getIndex(ch)

            print(f"Exploring Node {ch}")
            for i in range(12):
                if graph1_matrix[i][index] > 0:
                    stack.append(getVertex(i))
            print(f"Finished Exploring Node {ch}")
    return [visited, progress]


def DFS_Matrix_Recursion_G2(ch: str, visited=[], progress=[]):

    index = getIndex(ch)
    visited.append(ch)
    print(f"Exploring Node {ch}")

    if ch == 'G':
        return [visited, progress]
    else:
        i = 0
        for i in range(12):
            if getVertex(i) not in visited:
                if graph2_matrix[index][i] > 0:
                    DFS_Matrix_Recursion_G1(getVertex(i), visited, progress)
        print(f"Finished Exploring Node {ch}")

    return [visited, progress]


def run_dfs_tests(visited=[], progress=[]):
    # Correct
    print("G1 Vertex Stack Visit Order:")
    [visited, progress] = DFS_Vertex_Stack_G1('S', visited, progress)
    print("Path: ", visited[0:visited.index('G')+1])

    visited = progress = []
    print()
    print()

    # Correct
    print("G1 Vertex Recursion Visit Order:")
    [visited, progress] = DFS_Vertex_Recursion_G1('S', visited, progress)
    print("Path: ", progress[0:progress.index('G')+1])

    visited = progress = []
    print()
    print()

    # Error
    print("G1 Matrix Stack Visit Order:")
    [visited, progress] = DFS_Matrix_Stack_G1('S', visited, progress)
    print("Path: ", visited[0:visited.index('G')+1])

    visited = progress = []
    print()
    print()

    # Correct
    print("G1 Matrix Recursion Visit Order:")
    [visited, progress] = DFS_Matrix_Recursion_G1('S', visited, progress)
    print("Path: ", progress[0:progress.index('G')+1])

    visited = progress = []
    print()
    print()

    # Error
    print("G2 Vertex Stack Visit Order:")
    [visited, progress] = DFS_Vertex_Stack_G2('S', visited, progress)
    print("One Direction Path: ", visited[0:visited.index('G')+1])

    visited = progress = []
    print()
    print()

    # Correct
    print("G2 Vertex Recursion Visit Order:")
    [visited, progress] = DFS_Vertex_Recursion_G2('S')
    print("One Direction Path: ", visited[::-1][0:visited.index('G')])

    visited = progress = []
    print()
    print()

    # Error
    print("G2 Matrix Stack Visit Order:")
    [visited, progress] = DFS_Matrix_Stack_G2('S', visited, progress)
    print("One Direction Path: ", visited[0:visited.index('G') + 1])

    visited = progress = []
    print()
    print()

    # Error
    print("G2 Matrix Recursion Visit Order:")
    [visited, progress] = DFS_Matrix_Recursion_G2('S', visited, progress)
    print("One Direction Path: ", visited[0:visited.index('G') + 1])
    return
