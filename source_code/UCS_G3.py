from Graphs_and_Helpers import getAdjacentLetterToExplore, getIndex, graph3_vertex, graph3_matrix
from queue import PriorityQueue


def UCS_Vertex_PQ_G3():
    priority_queue = PriorityQueue()
    priority_queue.put((0, 'S'))
    visited_letters = set()
    expanded_steps = []

    while not priority_queue.empty():
        temp = priority_queue.get()
        (path_cost, path) = temp
        letter_to_be_explored = path[-1]
        if letter_to_be_explored not in visited_letters:
            visited_letters.add(letter_to_be_explored)
            expanded_steps.append(letter_to_be_explored)

            if letter_to_be_explored == 'G':
                return (path, expanded_steps)

            for adjacent_letter_to_explore in graph3_vertex[letter_to_be_explored]:
                if adjacent_letter_to_explore not in visited_letters:
                    priority_queue.put((path_cost + graph3_vertex[letter_to_be_explored]
                                        [adjacent_letter_to_explore], path + adjacent_letter_to_explore))


def UCS_Matrix_PQ_G3():
    priority_queue = PriorityQueue()
    priority_queue.put((0, 'S'))
    visited_letters = set()
    expanded_steps = []

    while not priority_queue.empty():
        temp = priority_queue.get()
        (path_cost, path) = temp
        letter_to_be_explored = path[-1]
        if letter_to_be_explored not in visited_letters:
            visited_letters.add(letter_to_be_explored)
            expanded_steps.append(letter_to_be_explored)

            if letter_to_be_explored == 'G':
                return (path, expanded_steps)

        for adjacent_letter_index in range(len(graph3_matrix[getIndex(letter_to_be_explored)])):
            if adjacent_letter_index not in visited_letters and graph3_matrix[getIndex(letter_to_be_explored)][adjacent_letter_index] > 0:
                adjacent_letter_to_explore = getAdjacentLetterToExplore(
                    adjacent_letter_index)
                if adjacent_letter_to_explore not in visited_letters:
                    priority_queue.put((path_cost + graph3_matrix[getIndex(
                        letter_to_be_explored)][adjacent_letter_index], path + adjacent_letter_to_explore))


def run_ucs_g3_tests():

    print("PRINTING UCS FOR G3 - All Correct")

    (path, expanded_steps) = UCS_Vertex_PQ_G3()
    print("UCS Expanded Steps Vertex w/ Priority Queue G3:")
    print("[" + " -> ".join(expanded_steps) + "]")
    print("UCS Path Vertex w/ Recursion G3:")
    print("[" + " -> ".join(path) + "]")

    print()
    print()

    (path, expanded_steps) = UCS_Matrix_PQ_G3()
    print("UCS Expanded Steps Matrix w/ Priority Queue G3:")
    print("[" + " -> ".join(expanded_steps) + "]")
    print("UCS Path Matrix w/ Priority Queue G3:")
    print("[" + " -> ".join(path) + "]")

    print()
    print()
    return
