#!/usr/bin/env python
# -*- coding: utf8 -*-
#
# https://hub.gke2.mybinder.org/user/numpy-numpy-tutorials-yne4ot5m/lab/tree/content/Untitled.ipynb

"""Find Lagrange polynomial for given sets of points"""

import numpy as np
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
import matplotlib.pyplot as plt


def main() -> None:
    """Do the job"""
    # x = np.array([0, 1, 2])
    x = np.array([0, 1, 2, 1.5])
    # y = x ** 3
    # title = "$x^3$"
    y = x ** 4
    title = "$x^4$"

    poly = lagrange(x, y)
    coefficients = Polynomial(poly.coef[::-1]).coef
    txt = f"${coefficients[0]} + " + " + ".join((f"{c} \\cdot x^{e + 1}" for e, c in enumerate(coefficients[1:]))) + "$"
    x_new = np.arange(-0.1, 2.11, 0.1)
    plt.scatter(x, y, label='data')
    plt.plot(x_new, Polynomial(poly.coef[::-1])(x_new), label=txt)
    plt.plot(x_new, 3 * x_new ** 2 - 2 * x_new + 0 * x_new,
             label=r"$3 x^2 - 2 x$", linestyle='-.')
    plt.legend()
    plt.title(f"{title}: {list((xi, yi) for xi, yi in zip(x, y))}.")
    plt.show()


if __name__ == "__main__":
    main()
