#!/usr/bin/python3
"""Module to multiply 2 matrices."""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        list: The resulting matrix.
    """
    if not isinstance(m_a, list):
        raise TypeError(m_a must be a list)

    if not isinstance(m_b, list):
        raise TypeError(m_b must be a list)

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError('m_a must be a list of lists')

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError('m_b must be a list of lists')

    if m_a == []:
        raise ValueError('m_a can\'t be empty')
    for row in m_a:
        if row == []:
            raise ValueError('m_a can\'t be empty')
    if m_b == []:
        raise ValueError('m_a can\'t be empty')
    for row in m_b:
        if row == []:
            raise ValueError('m_b can\'t be empty')

    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError('m_a should contain only integers or floats')
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError('m_b should contain only integers or floats')
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError('Each row of m_a must be of the same size')

    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError('Each row of m_b must be of the same size')

    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')
