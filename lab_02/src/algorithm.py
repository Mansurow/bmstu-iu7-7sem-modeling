import tkinter
import numpy as np
from scipy.integrate import odeint
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def normalize(probs):
    s = sum(probs)
    for i in range(len(probs)):
        probs[i] /= s

def solve(matrix):
    matrixSize = len(matrix)
    # normalize(start_probs)
    # print(start_probs)
    
    coefficients = matrix.copy()
    coefficients = coefficients.T

    np.fill_diagonal(
        coefficients, matrix.diagonal() - matrix.sum(axis=1)
    )

    coefficients[0] = 1

    constant_terms = np.zeros(matrixSize)
    constant_terms[0] = 1
    # print(constant_terms)

    print("Матрица:")
    for row in coefficients:
        print(row)

    probabilities = np.linalg.solve(coefficients, constant_terms)
    print("Предельные вероятности:")
    print(probabilities)
    v = matrix.sum(axis=0) - matrix.diagonal()
    times = (probabilities / v).tolist()
    print("Времена достижения предельных вероятностей")
    print(times)


    # ps = np.linalg.solve(matrix_to_solve, freeMembersColumn)
    # print("Result:")
    # print(ps)
    # print("Стабильное состояние:")
    # for i in range(len(ps)):
    #     print(f"p{str(i)} = {ps[i]:.2f}; ", end='')
    # print()

    # max_lambda = max([max(matrix[i]) for i in range(len(matrix))])
    # avg_lambda = sum([sum(matrix[i]) for i in range(len(matrix))]) / len(matrix) / (len(matrix) - 1)
    # dt = (1 / (max_lambda + avg_lambda) * 2) * dt
    # solve_ode(matrix, start_probs, dt, ps)


