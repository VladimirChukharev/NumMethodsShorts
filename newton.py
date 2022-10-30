#!/usr/bin/env python
# -*- coding: utf8 -*-
#
# https://mybinder.org/v2/gh/VladimirChukharev/NumMethodsShorts/HEAD
# https://mybinder.org/v2/gh/VladimirChukharev/NumMethodsShorts/
# 01db198cd4ad842db03cc5fe174f3d7d92770897?urlpath=lab%2Ftree%2Flagrange.ipynb

"""
Find Lagrange polynomial for given sets of points in Newton's form.
Main part of implementation by Khalil Al Hooti:
https://stackoverflow.com/questions/14823891/newton-s-interpolating-polynomial-python
"""

import numpy as np
import matplotlib.pyplot as plt


def _poly_newton_coefficient(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """
    x: list or np array containing x data points
    y: list or np array containing y data points
    """
    m: int = len(x)
    # x = np.copy(x)
    a: np.ndarray = np.copy(y)
    for k in range(1, m):
        print(a)
        a[k:m] = (a[k:m] - a[k - 1]) / (x[k:m] - x[k - 1])
    print(a)
    return a


def newton_polynomial(x_data: np.ndarray, y_data: np.ndarray, x: np.ndarray) -> np.ndarray:
    """
    x_data: data points at x
    y_data: data points at y
    x: evaluation point(s)
    """
    a: np.ndarray = _poly_newton_coefficient(x_data, y_data)
    print(f">>> {a}")
    n: int = len(x_data) - 1  # Degree of polynomial
    p: np.ndarray = a[n]
    for k in range(1, n + 1):
        p = a[n - k] + (x - x_data[n - k]) * p
    return p


def main() -> None:
    """Do the job"""
    # x = np.array([-1,])
    # x = np.array([-1, 0])
    x = np.array([-1, 0, 1])
    # x = np.array([-1, 0, 1, 2])
    # x = np.array([0, 1, 2])
    # x = np.array([0, 1, 2, 1.5])
    # x = np.array([-1, 0, 1, 2, 1.5])

    y, title = x ** 3, "$x^3$"
    # y, title = x ** 4, "$x^4$"

    coefficients = _poly_newton_coefficient(x, y)
    txt = (f"${coefficients[0]:g} + " +
           " + ".join((f"{c:g} \\cdot x^{e + 1}" for e, c in enumerate(coefficients[1:]))) + "$")
    x_new = np.arange(-1.1, 2.11, 0.1)
    plt.scatter(x, y, label='data')
    plt.plot(x_new, newton_polynomial(x, y, x_new), label=txt, linestyle=":")
    plt.legend()
    plt.title(f"{title}: {list((xi, yi) for xi, yi in zip(x, y))}.")
    plt.show()


if __name__ == "__main__":
    main()
