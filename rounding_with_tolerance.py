#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
Получив величину и оценку её погрешности записать их по правилам округлений
"""

import random
import math


def first_digit_and_power(val: float) -> tuple[float, int]:
    """Определить первую значащую цифру и порядок числа"""
    if val == 0.0:
        return 0, 0
    ten_power: float = 1.0
    power: int = 0
    while ten_power <= val:
        power += 1
        ten_power *= 10.0
    while ten_power > val:
        power -= 1
        ten_power /= 10.0
    return math.floor(val / ten_power), power


def all_digits(val: float) -> str:
    """Преобразовать число в строку с максимальной точностью десятичного представления без степени 10"""
    if val == 0.0:
        return "0"
    residual = abs(val)
    power: int = 0
    ten_power: float = 1.0
    s: str = ""
    while ten_power <= residual:
        power += 1
        ten_power *= 10.0
    while ten_power > residual:
        power -= 1
        ten_power /= 10.0
    dig = math.floor(residual / ten_power)
    s += str(dig) if val > 0.0 else str(-dig)
    residual -= dig * ten_power
    while residual > 0.0:
        power -= 1
        try:
            ten_power /= 10.0
            dig = math.floor(residual / ten_power)
        except ZeroDivisionError:
            break
        if power == -1:
            s += "."
        s += str(dig)
        residual -= dig * ten_power
    if power > 0:
        s += "0" * power
    return s


def round_1or2digits(val: float) -> float:
    """Округлить число до 1 цифры, если она от 3 до 9, или до 2 цифр, если первая 1 или 2"""
    digit, power = first_digit_and_power(val)
    ten_power: float = pow(10, power)
    if digit in range(3, 10):
        return digit * ten_power
    return digit * ten_power


def digit_from_floating_point(val: float, dig: int) -> int:
    """
    Return a decimal digit at the position `dig` from the floating point (FP).
    The digit to the left from FP is number 0, positive to the left, negative to the right.
    """
    return math.floor(val / pow(10, dig)) % 10


def main() -> None:
    """Do the job"""
    dig: float
    power: int
    samples = (0.0, 1.0, 0.1, 1e10, 1e-10, 1.1, 9.99, 1.9999e10, 1.9999e-10)
    for i, num in enumerate(samples):
        dig, power = first_digit_and_power(num)
        print(f"{i}: {num=}, {dig=}, {power=}.")
    for j in range(len(samples) + 1, 21):
        num: float = random.expovariate(1e-6)
        dig, power = first_digit_and_power(num)
        print(f"{j}: {num=}, {dig=}, {power=}, {digit_from_floating_point(num, power)=}.")
        if dig != digit_from_floating_point(num, power):
            print(f">>>>>>> {j}: {num=}, {dig=}, {power=}, {digit_from_floating_point(num, power)=}.")
    num = 1234567890.1234567890
    dig, power = first_digit_and_power(num)
    print(f"\n{num=}, {dig=}, {power=}, {digit_from_floating_point(num, power)=}.")
    s = ""
    for i in range(10, -1, -1):
        s += str(digit_from_floating_point(num, i))
    s += "."
    for i in range(-1, -11, -1):
        s += str(digit_from_floating_point(num, i))
    print(f"{num=} => {s=}, {all_digits(num)=}.")


if __name__ == "__main__":
    """This is run if the file is run"""
    main()
