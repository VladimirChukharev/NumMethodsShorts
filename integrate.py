#!/usr/bin/env python
# -*- coding: utf8 -*-
#
# https://mybinder.org/v2/gh/VladimirChukharev/NumMethodsShorts/HEAD
# https://mybinder.org/v2/gh/VladimirChukharev/NumMethodsShorts/
# 01db198cd4ad842db03cc5fe174f3d7d92770897?urlpath=lab%2Ftree%2Flagrange.ipynb

"""
Integrate a function by different methods.
"""

from math import log
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
    """Integrate using Simpson's method. dx is length of the 3-point segments (2 half-points overlap)."""
    n: int = len(y)
    if not n % 2:
        print(f"simpson({y}, {dx}): Even number of points is not recommended, use odd number of them.")
    s: float = (y[0] + y[-1] + y[1::2].sum() * 4.0 + y[2:-1:2].sum() * 2.0) * dx / 6.0
    return s


def simpson_3_8(y: np.ndarray, dx: float) -> float:
    """Integrate using Simpson's 3/8 method. dx is length of the 4-point segments (2 half-points overlap)."""
    n: int = len(y)
    if n % 3 != 1:
        print(f"simpson({y}, {dx}): Wrong number of points, {n} is not recommended, use 3*N+1 points.")
    s: float = (y[0] + y[-1] + (y[1::3].sum() + y[2::3].sum()) * 3.0 + y[3:-1:3].sum() * 2.0) * dx / 8.0
    return s


def func(x: np.ndarray) -> np.ndarray:
    """Function to integrate"""
    abs_x: np.ndarray = np.abs(x)
    return np.abs((abs_x - 1.0) ** 3 * (abs_x * 3 + 1.0) / 12.0)


def main() -> None:
    """Do the job"""

    a, b = 1.0, 2.0
    n = 1
    # a, b = -1.0, 1.0
    # n = 200
    n_plus_1 = n + 1
    x, step = np.linspace(a, b, n_plus_1, retstep=True)
    dx: float = float(step)
    shift = dx / 2.0
    x_s = np.linspace(a, b, 2 * n_plus_1 - 1)
    x_s38 = np.linspace(a, b, 3 * n_plus_1 - 2)
    # y = np.exp(x)
    # y_shifted = np.exp(x[:-1] + shift)
    # y_simpson = np.exp(x_s)

    y = 1.0 / x

    y_shifted = 1.0 / (x[:-1] + shift)
    y_simpson = 1.0 / x_s
    y_simp38 = 1.0 / x_s38

    # y: np.ndarray = func(x)
    # y_shifted: np.ndarray = func(x[:-1] + shift)
    # y_simpson: np.ndarray = func(x_s)
    # y_simp38: np.ndarray = func(x_s38)
    print(f"{n=}.")
    print(f"{x=} :{len(x)},\n{x_s=} :{len(x_s)},\n{x_s38=} :{len(x_s38)}.")
    print(f"{y=} :{len(y)},\n{y_shifted=} :{len(y_shifted)},\n"
          f"{y_simpson=} :{len(y_simpson)},\n{y_simp38=} :{len(y_simp38)}.")
    l_rect = l_rectangles(y, dx)
    r_rect = r_rectangles(y, dx)
    m_rect = m_rectangles(y_shifted, dx)
    s_simpson = simpson(y_simpson, dx)
    s_simpson38 = simpson_3_8(y_simp38, dx)
    print(f"{l_rect=},\n{r_rect=},\n{m_rect=},\n{s_simpson=},\n{s_simpson38=}.")
    val = log(2)
    print(f"Actual value of ln(2) = {val}.")


if __name__ == "__main__":
    main()
