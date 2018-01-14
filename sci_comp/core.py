# coding: utf-8

from typing import Callable

import numpy as np


# 前進差分
def forward_difference(f: Callable[[float], float], x: float, h: float) -> float:
    return (f(x + h) - f(x)) / h


# 後進差分
def backward_difference(f: Callable[[float], float], x: float, h: float) -> float:
    return (f(x) - f(x - h)) / h


# 中心差分
def central_difference(f: Callable[[float], float], x: float, h: float) -> float:
    return (f(x + h / 2) - f(x - h / 2)) / h


# 5点公式
def five_point_formula(f: Callable[[float], float], x: float, h: float) -> float:
    return 1 / (3 * h) * (8 * (f(x + h / 4) - f(x - h / 4)) - (f(x + h / 2) - f(x - h / 2)))


# Warnings found
# 台形公式
def trapezoidal(f: Callable[[float], float], a: float, b: float, n: int):
    h = (b - a) / n

    n_1 = np.linspace(a, b, n + 1)
    n_1 = f(n_1)
    n_1[0], n_1[-1] = n_1[0] / 2, n_1[-1] / 2

    result = h * n_1.sum()

    return result


# Warnings found
# Simpson則
def simpson(f: Callable[[float], float], a: float, b: float, n: int):
    h = (b - a) / (2 * n)

    n_1 = np.linspace(a, b, 2 * n + 1)
    n_1 = f(n_1)

    n_2 = np.concatenate([np.array([1]), np.tile([4, 2], n)])
    n_2[-1] = 1

    result = h / 3 * np.sum(n_1 * n_2)

    return result


# Warnings found
# 二分法
def bisection(f: Callable[[float], float], a: float, b: float, e: float):
    a_n, b_n = a, b

    while True:
        x_n = (a_n + b_n) / 2

        if np.absolute(f(x_n)) <= e:
            return x_n

        if f(a_n) * f(x_n) > 0 > f(b_n) * f(x_n):
            a_n = x_n
        elif f(a_n) * f(x_n) < 0 < f(b_n) * f(x_n):
            b_n = x_n
        else:
            raise ValueError


# はさみうち法
def false_position():
    pass


# ニュートン法
def newton(f, e):
    a_n = 0

    while True:
        x_n = a_n - f(a_n) / central_difference(f, a_n, 10 ** -6)

        if abs(f(x_n)) <= e:
            break
        a_n = x_n

    result = x_n

    return result
