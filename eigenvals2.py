#!/usr/bin/env python
# -*- coding: utf8 -*-

"""Make calculations for a task of SOR"""

import numpy as np

if __name__ == "__main__":
    # Начальные данные
    matL = np.array([[0.0, 0.0],
                     [1.0, 0.0]])
    matD = np.array([[1.0, 0.0],
                     [0.0, 2.0]])
    matU = np.array([[0.0, 1.0],
                     [0.0, 0.0]])
    vec_b = np.array([1.0, 1.0])
    epsilon = 0.001

    # Собираем A
    matA = matL + matD + matU

    # Проверка точным методом
    matA_inv = np.linalg.inv(matA)
    matA_E = np.matmul(matA_inv, matA)
    resA = np.matmul(matA_inv, vec_b)
    nevyazka = np.matmul(matA, resA) - vec_b
    norm_nev = np.linalg.norm(nevyazka)

    # Ищем границу для тау и оптимальное значение тау
    eigenA = np.linalg.eigvals(matA)
    tau_max = 2.0 / max((abs(val) for val in eigenA))
    tau_opt = 2.0 / (max((abs(val) for val in eigenA)) + min((abs(val) for val in eigenA)))

    matB = tau_opt * matL + matD
    matC = (1 - tau_opt) * matL - matU
    matB_inv = np.linalg.inv(matB)
    matG = np.matmul(-matB_inv, matC)
    vec_g = np.matmul(matB_inv, vec_b)
    eigenG = np.linalg.eigvals(matG)
    norm_G = max((abs(val) for val in eigenG))
    norm_g = np.sqrt(np.matmul(vec_g, vec_g))
    q = max(np.abs(eigenG))
    iteration_N = np.log(epsilon * (1 - norm_G) / norm_g) / np.log(q)

    print(f"{epsilon=}")
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

    print(f"{matB=}")
    print(f"{matC=}")
    print(f"{matB_inv=}")
    print(f"{matG=}")
    print(f"{vec_g=}")

    print(f"{eigenG=}")
    print(f"{norm_G=}")
    print(f"{norm_g=}")
    print(f"{q=}")
    print(f"{iteration_N=}")

    vec_x = np.array([0.0, 1.0])
    k: int = 0
    print(f"{k}: {vec_x=}")
    print(f"{1}: {np.matmul(matG, vec_x) + vec_g}")
    for k in range(int(iteration_N)):
        # print(f"{vec_x}: {vec_x=}")
        vec_x = np.matmul(matG, vec_x) + vec_g
    resSOR = np.matmul(matA, vec_x)
    nevSOR = resSOR - vec_b
    norm_nevSOR = np.linalg.norm(nevSOR)
    print(f"{k+1}: {vec_x=}")
    print(f"{resSOR=}")
    print(f"{nevSOR=}")
    print(f"{norm_nevSOR=}")
