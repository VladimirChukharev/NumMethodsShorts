#!/usr/bin/env python
# -*- coding: utf8 -*-

"""Find function root by dissection."""
from random import uniform
from scipy.constants import golden

from typing import Callable


def func1(x: float) -> float:
    """(x - x0) ** 3: Test function to dissect to find its root"""
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
    """Generate a new point to try as an arithmetic average of the last two points"""
    return left + (right - left) / golden


def gen_x_random(left: float, right: float) -> float:
    """Generate a new point to try as a random between the last two points"""
    return uniform(left, right)


def dissect(fun: Callable[[float], float], low: float, high: float, tolerance: float = 1e-9,
            gen_x: Callable[[float, float], float] = None) -> (float, int):
    """Binary dissection method of finding a root on the given segment"""
    if gen_x is None:
        gen_x = gen_x_middle
    assert low != high and tolerance > 0.0
    x_left: float = low
    x_right: float = high
    f_left: float = fun(x_left)
    f_right: float = fun(x_right)
    if abs(f_left) <= tolerance:
        return low
    if abs(f_right) <= tolerance:
        return high
    if same_sign(f_left, f_right):
        raise ValueError(f"Error in dissect({fun}, {low}, {high}, {tolerance}): {f_left=} {f_right=} "
                         f"same sign on both ends.")
    x_new: float = gen_x(x_left, x_right)
    f_new: float = fun(x_new)
    count: int = 0
    while abs(x_right - x_left) >= tolerance:
        # print(f"{count=}, {x_right-x_left=}.")
        # print(f"x:{' ' * 4} {x_left:18.12g} {x_new:18.12g} {x_right:18.12g}.")
        # print(f"f:{' ' * 4} {f_left:18.12g} {f_new:18.12g} {f_right:18.12g}.")
        if same_sign(f_new, f_left):
            x_left, f_left = x_new, f_new
        elif same_sign(f_new, f_right):
            x_right, f_right = x_new, f_new
        else:
            raise RuntimeError(f"\nx: {x_left:18.12g} {x_new:18.12g} {x_right:18.12g}."
                               f"\ny: {f_left:18.12g} {f_new:18.12g} {f_right:18.12g}.")
        count += 1
        x_new = gen_x(x_left, x_right)
        f_new = fun(x_new)
    return x_new, count


if __name__ == "__main__":
    func = func1
    cnt: int
    start: float = -100.0
    finish: float = 100.0
    accuracy: float = 1e-6
    result: float
    result, cnt = dissect(func, start, finish, accuracy)
    print(f"dissect({func.__doc__.split(':')[0]}, {start}, {finish}) = {result}; {cnt=}.")
    result, cnt = dissect(func, start, finish, accuracy, gen_x_random)
    print(f"dissect({func.__doc__.split(':')[0]}, {start}, {finish}) = {result}; {cnt=} random.")
    result, cnt = dissect(func, start, finish, accuracy, gen_x_golden)
    print(f"dissect({func.__doc__.split(':')[0]}, {start}, {finish}) = {result}; {cnt=} golden.")
