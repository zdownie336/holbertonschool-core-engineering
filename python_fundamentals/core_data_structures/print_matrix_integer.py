#!/usr/bin/env python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for element in range(len(matrix[row])):
            if element == len(matrix[row]) - 1:
                print("{num:d}".format(num=matrix[row][element]))
            else:
                print("{num:d}".format(num=matrix[row][element]), end=" ")

    if matrix == [[]]:
        print(f"")
