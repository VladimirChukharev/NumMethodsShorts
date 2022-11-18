#!/usr/bin/env python
# -*- coding: utf8 -*-
#
# https://mybinder.org/v2/gh/VladimirChukharev/NumMethodsShorts/HEAD
# https://mybinder.org/v2/gh/VladimirChukharev/NumMethodsShorts/
# 01db198cd4ad842db03cc5fe174f3d7d92770897?urlpath=lab%2Ftree%2Flagrange.ipynb

"""Find Lagrange polynomial for given sets of points"""

import numpy as np
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
import matplotlib.pyplot as plt


def main() -> None:
    """Do the job"""
    # x = np.array([-1,])
    # x = np.array([-1, 0])
    # x = np.array([-1, 0, 1])
    # x = np.array([-1, 0, 1, 2])
    # x = np.array([0, 1, 2])
    # x = np.array([0, 1, 2, 1.5])
    x = np.array([-1, 0, 1, 2, 1.5])

    y, title = x ** 3, "$x^3$"
    # y, title = x ** 4, "$x^4$"

    poly = lagrange(x, y)
    coefficients = Polynomial(poly.coef[::-1]).coef
    txt: str = (f"${coefficients[0]:g} + " +
                " + ".join((f"{c:g} \\cdot x^{e + 1}" for e, c in enumerate(coefficients[1:]))) + "$")
    x_new = np.arange(-1.1, 2.11, 0.1)
    plt.scatter(x, y, label='data')
    plt.plot(x_new, Polynomial(poly.coef[::-1])(x_new), label=txt, linestyle="-.")
    plt.legend()
    plt.title(f"{title}: {list((xi, yi) for xi, yi in zip(x, y))}.")
    plt.show()


if __name__ == "__main__":
    main()
