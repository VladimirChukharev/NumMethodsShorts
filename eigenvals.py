#!/usr/bin/env python
# -*- coding: utf8 -*-

"""Python Script"""

import numpy as np
from numpy import ndarray

if __name__ == "__main__":
    # Начальные данные
    m1 = np.array([[3.0, 4.0],
                   [2.0, 3.0]])
    vec_v1 = np.array([1.0, 1.0])
    epsilon = 0.001

    # Проверка точным методом
    m1_inv = np.linalg.inv(m1)
    m1_E = np.matmul(m1_inv, m1)
    res = np.matmul(m1_inv, vec_v1)

    # Переходим к задаче с симметричной матрицей
    m1t = m1.transpose()
    matA = np.matmul(m1, m1t)
    vec_b: ndarray = np.matmul(m1t, vec_v1)

    # Проверка точным методом в задаче с симметричной матрицей
    matA_inv = np.linalg.inv(matA)
    matA_E = np.matmul(matA_inv, matA)
    resA = np.matmul(matA_inv, vec_b)
    nevyazka = np.matmul(matA, resA) - vec_b
    norm_nev = np.linalg.norm(nevyazka)

    # Ищем границу для тау и оптимальное значение тау
    eigenA = np.linalg.eigvals(matA)
    tau_max = 2.0 / max((abs(val) for val in eigenA))
    tau_opt = 2.0 / (max((abs(val) for val in eigenA)) + min((abs(val) for val in eigenA)))

    matE = np.array([[1.0, 0.0],
                     [0.0, 1.0]])
    matG = matE - tau_opt * matA
    vec_g = tau_opt * vec_b
    eigenG = np.linalg.eigvals(matG)
    norm_G = max((abs(val) for val in eigenG))
    norm_g = np.sqrt(np.matmul(vec_g, vec_g))
    q = max(np.abs(eigenG))
    iteration_N = np.log(epsilon * (1 - norm_G) / norm_g) / np.log(q)

    print(f"{epsilon=}")
    # print(f"{m1=}")
    # print(f"{vec_v1=}")
    #
    # print(f"{m1_inv=}")
    # print(f"{m1_E=}")
    # print(f"{res=}")
    #
    # print(f"{m1t=}")
    print(f"{matA=}")
    print(f"{vec_b=}")

    print(f"{matA_inv=}")
    print(f"{matA_E=}")
    print(f"{resA=}")
    print(f"{nevyazka=}")
    print(f"{norm_nev=}")

    # print(f"{matE=}")
    print(f"{eigenA=}")
    print(f"{tau_max=}")
    print(f"{tau_opt=}")

    print(f"{19*matG=}")
    print(f"{19*vec_g=}")

    print(f"{eigenG=}")
    print(f"{norm_G=}")
    print(f"{norm_g=}")
    print(f"{q=}")
    print(f"{iteration_N=}")

    # vec_x = np.zeros((2,1))
    vec_x = np.array([0.0, 0.0])
    k: int = 0
    print(f"{k}: {vec_x=}")
    for k in range(int(iteration_N)):
        # print(f"{vec_x}: {vec_x=}")
        vec_x = np.matmul(matG, vec_x) + vec_g
    resMPI = np.matmul(matA, vec_x)
    nevMPI = resMPI - vec_b
    norm_nevMPI = np.linalg.norm(nevMPI)
    print(f"{k + 1}: {vec_x=}")
    print(f"{resMPI=}")
    print(f"{nevMPI=}")
    print(f"{norm_nevMPI=}")
