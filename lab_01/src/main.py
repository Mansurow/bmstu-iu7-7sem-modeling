import graph as g

def MainMenu():
    print("------------ Меню ---------------")
    print("1 - Равномерное распределение")
    print("2 - Нормальное распределение")
    print("0 - Выйти")

def GraphUniform():
    print("\nВведите отрезок для равномерного распределения: ")
    a = float(input("a = "))
    b = float(input("b = "))

    g.DrawUniformDistrGraphs(a, b)

# choice = -1;
# while (choice != 0):
#     MainMenu()
#     choice = int(input("Выбор: "))
#
#     if choice == 1:
#         GraphUniform()
#     elif choice == 2:
#         print()


g.DrawUniformDistrGraphs(-5, 5)
#g.DrawNormalDistrGraphs(1, 4)