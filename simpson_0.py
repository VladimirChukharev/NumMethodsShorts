#!/usr/bin/env python
# -*- coding: utf8 -*-
#
# https://mybinder.org/v2/gh/VladimirChukharev/NumMethodsShorts/HEAD
# https://mybinder.org/v2/gh/VladimirChukharev/NumMethodsShorts/
# 01db198cd4ad842db03cc5fe174f3d7d92770897?urlpath=lab%2Ftree%2Flagrange.ipynb

"""
Find the Lagrange polynomial for three given points.
"""

# import numpy as np
# import matplotlib.pyplot as plt
import sympy as sp  # type: ignore


def main() -> None:
    """Do the job"""

    x, x0 = sp.symbols("x x0", real=True)
    h = sp.symbols("h", real=True, positive=True)
    a0, a1, a2 = sp.symbols("a0 a1 a2", real=True)
    a, b, c = x0, x0 + 2 * h, x0 + h

    f = a0 + a1 * x + a2 * x ** 2
    f0 = f.subs(x, a)
    f1 = f.subs(x, c)
    f2 = f.subs(x, b)
    fd = sp.simplify(f1 - f0)

    s = sp.simplify(sp.integrate(f, (x, a, b)))
    res = sp.simplify(s - (f0 + 4 * f1 + f2) * h / 3)

    print(f"{dir() = }.")
    for name, item in (("x", x), ("x0", x0), ("h", h), ("a0", a0), ("a1", a1), ("a2", a2), ("a", a), ("b", b), ("c", c),
                ("f", f), ("f0", f0), ("f1", f1), ("f2", f2), ("fd", fd), ("s", s), ("res", res)):
        print(f"{name}: {item} = {item.expand()}.")


if __name__ == "__main__":
    main()
