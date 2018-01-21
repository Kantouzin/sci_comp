# coding: utf-8

from typing import Callable, Union

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


# 台形公式
def trapezoidal(f: Callable[[float], float], a: float, b: float, n: int):
    h = (b - a) / n

    n_1 = np.linspace(a, b, n + 1)
    n_1 = np.frompyfunc(f, 1, 1)(n_1)
    n_1[0], n_1[-1] = n_1[0] / 2, n_1[-1] / 2

    result = h * n_1.sum()

    return result


# Simpson則
def simpson(f: Callable[[float], float], a: float, b: float, n: int):
    h = (b - a) / (2 * n)

    n_1 = np.linspace(a, b, 2 * n + 1)
    n_1 = np.frompyfunc(f, 1, 1)(n_1)

    n_2 = np.concatenate([np.array([1]), np.array([4, 2] * n)])
    n_2[-1] = 1

    result = h / 3 * np.sum(n_1 * n_2)

    return result


# 二分法
def bisection(f: Callable[[float], float], a: float, b: float, e: float):
    a_n, b_n = a, b
    u_func = np.frompyfunc(f, 1, 1)

    while True:
        x_n = (a_n + b_n) / 2

        if np.absolute(f(x_n)) <= e:
            return x_n

        if u_func(a_n) * u_func(x_n) > 0 > u_func(b_n) * u_func(x_n):
            a_n = x_n
        elif u_func(a_n) * u_func(x_n) < 0 < u_func(b_n) * u_func(x_n):
            b_n = x_n
        else:
            raise ValueError


# はさみうち法
def false_position():
    pass


# ニュートン法
def newton(f: Callable[[float], float], i: float = 0, e: float = 10**-6):
    a_n = i

    while True:
        x_n = a_n - f(a_n) / central_difference(f, a_n, e)

        if abs(f(x_n)) <= e:
            break
        a_n = x_n

    result = x_n

    return result


# 1次方程式における最小二乗法
def least_squares(x: Union[np.ndarray], y: Union[np.ndarray]) -> Callable[[float], float]:
    n = x.size

    a = (n * np.sum(x * y) - x.sum()*y.sum()) / (n * np.sum(x**2) - x.sum()**2)
    b = (np.sum(x**2)*y.sum() - np.sum(x * y)*x.sum()) / (n * np.sum(x**2) - x.sum()**2)

    return lambda t: a * t + b
