#!/usr/bin/python3
"""
Solving pascal triangle
"""


def pascal_triangle(n):
    """
    pascal_triangle - creating the pascal triangle
    """
    res = []

    for i in range(1, n + 1):
        prev = [] if i == 1 else res[-1]

        def get_comb(prev, x, y):
            # calculating c(x, y) = p(x) / p(x - y) * p(y)
            if x == y or x == 1 or y == 1:
                return 1
            return prev[y - 2] + prev[y - 1]

        res.append([get_comb(prev, i, j) for j in range(1, i + 1)])

    return res
