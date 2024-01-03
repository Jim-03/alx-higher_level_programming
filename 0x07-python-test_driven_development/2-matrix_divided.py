#!/usr/bin/python3
"""Function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """
    args:
        matrix: the matrix with values
        div: the value to divide from in the matrix
    Returns:
        new_matrix: matrix with the quotients
    Raises:
        TypeError: matrix/div isn't integer or float
        ZeroDivisionError: when div is zero
    Returns:
        new_matrix: contains the quotient values
    """
    if not all(isinstance(row, list) and all(isinstance(element, (int, float))
                                             for element in row)
               for row in matrix):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row]
            for row in matrix]
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
