#!/usr/bin/env python
# -*- coding: utf8 -*-

"""Python Script"""

import numpy as np

if __name__ == "__main__":
    m1 = np.array([[3.0, 4.0],
                   [2.0, 3.0]])
    mt = m1.transpose()
    ms = np.matmul(m1, mt)
    eigen = np.linalg.eigvals(ms)
    lim = 2.0 / max((abs(val) for val in eigen))
    tau_opt = 2.0 / (max((abs(val) for val in eigen)) + min((abs(val) for val in eigen)))
    print(f"{m1=}")
    print(f"{mt=}")
    print(f"{ms=}")
    print(f"{eigen=}")
    print(f"{lim=}")
    print(f"{tau_opt=}")
