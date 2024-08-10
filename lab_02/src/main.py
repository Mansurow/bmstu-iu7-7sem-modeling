import random
import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from algorithm import solve
import networkx as nx
from ui.matrixComponent import *
from ui.modelingSettingsComponent import *
from Config import Config

def genRandLambdas():
    matrSize = matrixComponent.matrixSize
    entries = matrixComponent.matrixEntries
    limit = float(modelingSettingsComponent.maxLambdaEntry.get())
    for i in range(matrSize):
        for j in range(matrSize):
            entries[i][j].delete(0, len(entries[i][j].get()))
            entries[i][j].insert(0, '0' if i == j else f"{random.random() * limit:.2f}")

def drawGraph():
    matrSize = matrixComponent.matrixSize
    matrix = [[float(matrixComponent.matrixEntries[i][j].get()) for j in range(matrSize)] for i in range(matrSize)]

    G = nx.DiGraph(np.matrix(matrix), create_using=nx.DiGraph)
    layout = nx.circular_layout(G)
    nx.draw(G, layout, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=nx.get_edge_attributes(G,'weight'), label_pos=0.2)
    plt.show()

def start():
    matrSize = matrixComponent.matrixSize
    matrix = np.array([[float(matrixComponent.matrixEntries[i][j].get()) for j in range(matrSize)] 
                       for i in range(matrSize)])
    # start_probs = np.array([float(matrixComponent.initProbsEntries[i].get()) for i in range(matrSize)])
    # dt = float(modelingSettingsComponent.timeDeltaEntry.get())
    solve(matrix)

def callRefreshMatrix(event):
    val = modelingSettingsComponent.matrixSizeEntry.get()
    matrixComponent.refreshMatrix(val)

if __name__ == "__main__":
    conf = Config()
    root = tk.Tk()
    root.title("ЛР 2")
    root["bg"] = conf.MAIN_COLOR
    root.geometry(str(conf.WINDOW_WIDTH) + "x" + str(conf.WINDOW_HEIGHT))
    root.resizable(height=False, width=False)

    menu = tk.Menu()
    # menu.add_command(label='Сгенерировать интенсивности', command=genRandLambdas)
    # menu.add_command(label='Нарисовать граф', command=drawGraph)
    menu.add_command(label='Решить', command=start)
    root.config(menu=menu)

    matrixComponent = MatrixComponent(root, conf, 2)
    modelingSettingsComponent = ModelingSettingsComponent(root, conf)
    modelingSettingsComponent.matrixSizeBtn.bind('<Button-1>', callRefreshMatrix)

    root.mainloop()





