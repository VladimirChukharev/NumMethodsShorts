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
    # x = np.array([-1, 0, 1, 2, 1.5])
    # x, x_test = np.array([0.05, 0.1, 0.15, 0.2, 0.25]), 0.12
    x, x_test = np.array([0.05, 0.1, 0.17, 0.25, 0.3]), 0.26

    # y, title = x ** 3, "$x^3$"
    # y, title = x ** 4, "$x^4$"
    # 0.05004, 0.10033, 0.17165, 0.25534, 0.30933
    y, title = np.array([0.05004, 0.10033, 0.17165, 0.25534, 0.30933]), ""
    points = 5

    poly = lagrange(x[0:points], y[0:points])
    polynomial = Polynomial(poly.coef[::-1])
    coefficients = polynomial.coef
    txt: str = (f"${coefficients[0]:g} + " +
                " + ".join((f"{c:.5g} \\cdot x^{e + 1}" for e, c in enumerate(coefficients[1:]))) + "$")
    # x_new = np.arange(-1.1, 2.11, 0.1)
    x_new = np.arange(-0.05, 0.35, 0.005)
    plt.scatter(x, y, label=f"data {polynomial(x_test)=:.6g}")
    plt.plot(x_new, polynomial(x_new), label=txt, linestyle="-.")
    plt.legend()
    # plt.title(f"{title}: {''.join(str((xi, yi)) for xi, yi in zip(x, y))}.")
    # plt.title(f"{''.join(str((xi, yi)) for xi, yi in zip(x, y))}.")
    plt.title(' '.join((f"{xi:15.2g}" for xi in x)) + "\n" +
              ' '.join((f"{yi:12.6g}" for yi in y)))
    plt.show()


if __name__ == "__main__":
    main()
