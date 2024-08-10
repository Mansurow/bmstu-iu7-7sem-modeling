from PyQt6.QtWidgets import (
    QMainWindow,
    QToolBar,
    QMessageBox
)
from PyQt6.QtGui import QAction

from main_page import MainPage


title = 'Лабораторная работа №3 по курсу "Моделирование", тема: Генерация псевдослучайных чисел'
width = 900
height = 600
info_title = 'Подробнее о программе'
info_text = 'Генерация псевдослучайных чисел'


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(title)
        self.setFixedSize(width, height)
        page = MainPage()
        self.setCentralWidget(page)