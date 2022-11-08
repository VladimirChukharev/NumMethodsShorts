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


def l_rectangles(x: np.ndarray, y: np.ndarray) -> float:
    """Integrate using left rectangles method"""
    dx: float = x[1] - x[0]
    s: float = y[0:-1].sum() * dx
    return s


def r_rectangles(x: np.ndarray, y: np.ndarray) -> float:
    """Integrate using right rectangles method"""
    dx: float = x[1] - x[0]
    s: float = y[1:].sum() * dx
    return s


def m_rectangles(x: np.ndarray, y: np.ndarray) -> float:
    """Integrate using right rectangles method"""
    dx: float = x[1] - x[0]
    s: float = y.sum() * dx
    return s


def main() -> None:
    """Do the job"""

    a, b = 0.0, 1.0
    n = 911
    x = np.linspace(a, b, n)
    y = np.exp(x)
    shift = (x[0] + x[1]) / 2.0
    y_shifted = np.exp(x[:-1] + shift)
    print(f"{x=}, {y=}, {y_shifted=}.")
    s_lrec = l_rectangles(x, y)
    s_rrec = r_rectangles(x, y)
    s_mrec = m_rectangles(x, y_shifted)
    print(f"{s_lrec=}, {s_rrec=}, {s_mrec=}.")


if __name__ == "__main__":
    main()
