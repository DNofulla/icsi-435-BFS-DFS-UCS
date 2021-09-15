import numpy as np


class G1_Matrix:
    __matrix = None

    # Default adjacency matrix size for this Graph will be 10 x 10
    def __init__(self, matrix_size: int = 10):
        self.__matrix = np.zeros([matrix_size, matrix_size], dtype=int)

    def add_edge(self, x: int, y: int, weight: int = 1):
        if weight < 0:
            raise Exception("Weight cannot be less than 0!")
        else:
            self.__matrix[x][y] = weight
            self.__matrix[y][x] = weight

    def remove_edge(self, x: int, y: int):
        self.__matrix[x][y] = 0
        self.__matrix[y][x] = 0

    def find_edge(self, x: int, y: int):
        return str(self.__matrix[x][y])

    def dfs_recursion(self):
        return "DFS Recursion!"

    def dfs_stack(self):
        return "DFS Stack!"

    def bfs_recursion(self):
        return "BFS Recursion!"

    def bfs_stack(self):
        return "BFS Stack!"
