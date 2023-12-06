#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nmatrix = []
    for i in range(len(matrix)):
        nmatrix.append([])

        for k in range(len(matrix[i])):
            nmatrix[i].append(matrix[i][k] ** 2)

    return nmatrix
