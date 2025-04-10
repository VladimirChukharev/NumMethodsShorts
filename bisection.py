#!/usr/bin/env python
# -*- coding: utf8 -*-

"""Find function root by bisection."""

from random import uniform
from typing import Callable

from scipy.constants import golden


def func1(x: float) -> float:
    """(x - x0) ** 3: Test function to bisect to find its root"""
    x0: float = 9.0
    return (x - x0) ** 3


def same_sign(a: float, b: float) -> bool:
    """Return True if both a and b are positive or both are negative"""
    if a > 0.0:
        return b > 0.0
    return b < 0.0


def gen_x_middle(left: float, right: float) -> float:
    """Generate a new point to try as an arithmetic average of the last two points"""
    return (left + right) / 2.0


def gen_x_golden(left: float, right: float) -> float:
    """Generate a new point to try as a golden section between the last two points"""
    return left + (right - left) / golden


def gen_x_random(left: float, right: float) -> float:
    """Generate a new point to try as a random between the last two points"""
    return uniform(left, right)


def bisect(fun: Callable[[float], float], low: float, high: float, tolerance: float = 1e-9,
           gen_x: Callable[[float, float], float] | None = None) -> tuple[float, int]:
    """Binary dissection method of finding a root on the given segment"""
    if gen_x is None:
        gen_x = gen_x_middle
    assert low != high and tolerance > 0.0
    x_left: float = low
    x_right: float = high
    f_left: float = fun(x_left)
    f_right: float = fun(x_right)
    if same_sign(f_left, f_right):
        raise ValueError(f"Error in bisect({fun}, {low}, {high}, {tolerance}): {f_left=} {f_right=} no sign change.")
    x_new: float = gen_x(x_left, x_right)
    count: int = 0
    while abs(x_right - x_left) >= tolerance:
        f_new = fun(x_new)
        # print(f"{count=}, {x_right-x_left=}.")
        # print(f"x:  {x_left:18.12g} {x_new:18.12g} {x_right:18.12g}.")
        # print(f"f:  {f_left:18.12g} {f_new:18.12g} {f_right:18.12g}.\n")
        if same_sign(f_new, f_left):
            x_left, f_left = x_new, f_new
        elif same_sign(f_new, f_right):
            x_right, f_right = x_new, f_new
        else:
            raise RuntimeError(f"\nx: {x_left:18.12g} {x_new:18.12g} {x_right:18.12g}."
                               f"\ny: {f_left:18.12g} {f_new:18.12g} {f_right:18.12g}.")
        x_new = gen_x(x_left, x_right)
        count += 1
    # print(f"{[(var, getattr(val, '__annotations__', '')) for var, val in vars().items()]}")
    return x_new, count


if __name__ == "__main__":
    func = func1
    assert(func.__doc__ is not None)
    cnt: int
    start: float = -100.0
    finish: float = 100.0
    accuracy: float = 1e-6
    result: float
    result, cnt = bisect(func, start, finish, accuracy)
    print(f"bisect({func.__doc__.split(':')[0]}, {start}, {finish}) = {result}; {cnt=}.")
    result, cnt = bisect(func, start, finish, accuracy, gen_x_golden)
    print(f"bisect({func.__doc__.split(':')[0]}, {start}, {finish}) = {result}; {cnt=} golden.")
    result, cnt = bisect(func, start, finish, accuracy, gen_x_random)
    print(f"bisect({func.__doc__.split(':')[0]}, {start}, {finish}) = {result}; {cnt=} random.")
