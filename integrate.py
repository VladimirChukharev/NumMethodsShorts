#!/usr/bin/env python
# -*- coding: utf8 -*-
#
# https://mybinder.org/v2/gh/VladimirChukharev/NumMethodsShorts/HEAD
# https://mybinder.org/v2/gh/VladimirChukharev/NumMethodsShorts/
# 01db198cd4ad842db03cc5fe174f3d7d92770897?urlpath=lab%2Ftree%2Flagrange.ipynb

"""
Integrate a function by different methods.
"""

import numpy as np


# import matplotlib.pyplot as plt
# import sympy as sp


def l_rectangles(y: np.ndarray, dx: float) -> float:
    """Integrate using left rectangles method"""
    s: float = y[:-1].sum() * dx
    return s


def r_rectangles(y: np.ndarray, dx: float) -> float:
    """Integrate using right rectangles method"""
    s: float = y[1:].sum() * dx
    return s


def m_rectangles(y: np.ndarray, dx: float) -> float:
    """Integrate using middle rectangles method"""
    s: float = y.sum() * dx
    return s


def simpson(y: np.ndarray, dx: float) -> float:
    """Integrate using Simpson's method. dx is length of the 3-point segments."""
    n: int = len(y)
    if not n % 2:
        print(f"Even number of points is not recommended, use odd number of them: simpson({y}, {dx}).")
    s: float = (y[0] + y[-1] + y[1::2].sum() * 4.0 + y[2:-1:2].sum() * 2.0) * dx / 6.0
    return s


def main() -> None:
    """Do the job"""

    # a, b = 0.0, 1.0
    # n = 911
    a, b = 1.0, 2.0
    n = 1
    n_plus_1 = n + 1
    x, dx = np.linspace(a, b, n_plus_1, retstep=True)
    shift = dx / 2.0
    x_s = np.linspace(a, b, 2 * n_plus_1 - 1)
    # y = np.exp(x)
    # y_shifted = np.exp(x[:-1] + shift)
    # y_simpson = np.exp(x_s)
    y = 1.0 / x
    y_shifted = 1.0 / (x[:-1] + shift)
    y_simpson = 1.0 / x_s
    print(f"{x=}, {y=}, {y_shifted=}, {y_simpson=}.")
    s_lrec = l_rectangles(y, dx)
    s_rrec = r_rectangles(y, dx)
    s_mrec = m_rectangles(y_shifted, dx)
    s_simpson = simpson(y_simpson, dx)
    print(f"{s_lrec=}, {s_rrec=}, {s_mrec=}, {s_simpson=}.")


if __name__ == "__main__":
    main()
