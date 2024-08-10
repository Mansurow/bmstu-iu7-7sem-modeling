from typing import Callable, Tuple

import distributions as dst
import numpy as np

import matplotlib.pyplot as plt


def DrawUniformDistrGraphs(a: float, b: float):

    x1, y1 = GetUniformDensityTableFunc(a, b, 1000)
    x2, y2 = GetUniformDistributionTableFunc(a, b, 1000)

    str1 = 'Равномерное распределение ~R[' + str(a) + ';' + str(b) + ']'

    fig, axs = plt.subplots(2, 1, figsize=(10, 10))
    fig.suptitle(str1, fontsize=20, fontweight='bold')
    axs[0].plot(x1, y1)
    axs[0].set_title("График функции плотности f(x)", fontsize=15)
    axs[0].grid(alpha=1)
    axs[1].plot(x2, y2)
    axs[1].set_title("График функции распределения F(x)", fontsize=15)
    axs[1].grid(alpha=1)
    plt.show()

def DrawNormalDistrGraphs(m: float, sigma: float):

    x1, y1 = GetNormalDensityTableFunc(m, sigma, 1000)
    x2, y2 = GetNormalDistributionTableFunc(m, sigma, 1000)

    str1 = 'Нормальное распределение ~N(' + str(m) + ',' + str(sigma) + '^2)'

    fig, axs = plt.subplots(2, 1, figsize=(10, 10))
    fig.suptitle(str1, fontsize=20, fontweight='bold')
    axs[0].plot(x1, y1)
    axs[0].set_title("График функции плотности f(x)", fontsize=15)
    axs[0].grid(alpha=1)
    axs[1].plot(x2, y2)
    axs[1].set_title("График функции распределения F(x)", fontsize=15)
    axs[1].grid(alpha=1)
    plt.show()

def GetTableFunc(function: Callable[..., float],
                 arguments: list[float],
                 xLeft: float,
                 xRight: float,
                 stepsNum: int) -> Tuple[list[float], list[float]]:
    step = (xRight - xLeft) / stepsNum

    xColumn = list(np.arange(xLeft, xRight + step / 2, step))
    yColumn = []

    for x in xColumn:
        yColumn.append(function(x, *arguments))

    return xColumn, yColumn


def GetUniformTableFunc(
        func:      Callable[[float, float, float], float],
        arguments: Tuple[float, float],
        interval:  Tuple[float, float],
        stepsNum:  int) -> Tuple[list[float], list[float]]:

    a, b = arguments

    xLeft, xRight = (2 * a - b, 2 * b - a) if interval is None else interval

    return GetTableFunc(func, [a, b], -10, 10, stepsNum)


def GetNormalTableFunc(
        func:      Callable[[float, float, float], float],
        arguments: Tuple[float, float],
        interval:  Tuple[float, float],
        stepsNum:  int) -> Tuple[list[float], list[float]]:

    m, sigma = arguments

    xLeft, xRight = ((m - 4 * sigma, m + 4 * sigma)
                        if interval is None else interval)

    return GetTableFunc(func, [m, sigma], -10, 10, stepsNum)


def GetUniformDensityTableFunc(
        a: float,
        b: float,
        stepsNum: int,
        interval: Tuple[float, float] = None) -> Tuple[list[float], list[float]]:
    return GetUniformTableFunc(dst.UniformDensityFunc, [a, b], interval, stepsNum)


def GetUniformDistributionTableFunc(
        a: float,
        b: float,
        stepsNum: int,
        interval: Tuple[float, float] = None) -> Tuple[list[float], list[float]]:
    return GetUniformTableFunc(dst.UniformDistributionFunc, [a, b],
                               interval, stepsNum)


def GetNormalDensityTableFunc(
        m:     float,
        sigma: float,
        stepsNum: int,
        interval: Tuple[float, float] = None) -> Tuple[list[float], list[float]]:
    return GetNormalTableFunc(dst.NormalDensityFunc, [m, sigma], interval, stepsNum)


def GetNormalDistributionTableFunc(
        m:     float,
        sigma: float,
        stepsNum: int,
        interval: Tuple[float, float] = None) -> Tuple[list[float], list[float]]:
    return GetNormalTableFunc(dst.NormalDistributionFunc, [m, sigma],
                              interval, stepsNum)
