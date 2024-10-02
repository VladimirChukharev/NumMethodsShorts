#!/usr/bin/env python
# -*- coding: utf8 -*-

""""Демонстрация численного интегрирования методом Симпсона"""

from math import log
from collections.abc import Callable


def simpson(a: float, b: float, func: Callable[[float], float], n: int) -> float:
    """
    Численно интегрировать методом Симпсона от a до b функцию func по n интервалам со срединными точками,

    a, b - пределы интегрирования
    func - интегрируемая функция одного действительного аргумента, возвращающая действительное значение
    n - натуральное число, количество интервалов элементарного интегрирования по Симпсону

    Функция func вызывается для 2n+1 значений аргумента.
    """
    h = (b - a) / n
    half_h = h / 2.0
    a_half = a + half_h
    return (4.0 * sum((func(a_half + i * h) for i in range(n))) +
            2.0 * sum((func(a + i * h) for i in range(1, n))) +
            func(a) + func(b)) * h / 6.0
    # Эти строки использовались при отладке:
    # s4 = sum((func(a_half + i * h) for i in range(n)))
    # s2 = sum((func(a + i * h) for i in range(1, n)))
    # result = (4.0 * sum((func(a_half + i * h) for i in range(n))) +
    #           2.0 * sum((func(a + i * h) for i in range(1, n))) + func(a) + func(b)) * h / 6.0
    # print(f"\t{h=} {half_h=} {a_half=} {s4=} {s2=}.")
    # return result


def funct(x: float) -> float:
    """"Тестовая функция для численного интегрирования"""
    try:
        return 1.0 / x
    except ArithmeticError as exc:
        print(f"Error in funct({x}): {exc=}.")
        raise


def main() -> None:
    """Do the job"""

    for j in range(8):
        k = 2 ** j
        print(f"{j}: {k=}, {simpson(1, 2, funct, k)}")
    print(f"Библиотечная функция: {log(2)=}.")


if __name__ == "__main__":
    main()
