import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def define_equation():
    def equation(t, y): #вот тут задаем енобходимое уравнение
        return -t + y
    return equation

def solve(equation, y0, inter):
    solution = solve_ivp(equation, #передаем уравнение, которое мы написали
                         inter, #передаем интеравил по которому интегрируем
                         [y0], # так как иногда может передаться скаляр, то мы это заворачиваем в список, ибо когда я тестировал было много таких кейсов
                         max_step=0.01 # вот это поределяет шаг интегрирования, с ним можно поиграться
                         )
    return solution.t, solution.y[0] # это массивы точек один время, другой - решения

def visualize(t, y, equation):
    plt.figure(figsize=(15, 7)) #просто размер окошка
    
    
    y_prime = [equation(tt, yy) for tt, yy in zip(t, y)] # эту функцию в интернете нашел, она должна опреджелять производные для phase-plot и их вместе упаковывать
    
    # График для time domain
    plt.subplot(1, 2, 1) # разбиваем окно на два графика и юзаем первую половину разбиения
    plt.plot(t, y, markersize=3, linewidth=1) #даем координаты задаем толщину и размер
    plt.xlabel('t', fontsize=12) # подписи
    plt.ylabel('y(t)', fontsize=12)
    plt.title('TIme-domain', fontsize=14)
    plt.grid(True, alpha=0.3) # добавляем сетку потом что юез нее не красиво
    
    # График дял phase-plot
    plt.subplot(1, 2, 2)# разбиваем окно на два графика и зюзаем вторую половину разбиения
    plt.plot(y, y_prime, markersize=3, linewidth=1)
    plt.xlabel('y', fontsize=12)
    plt.ylabel("y'", fontsize=12)
    plt.title('Phase-plot', fontsize=14)
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show() # вывод окна с графицками

equation = define_equation()#говорим какое уравнение используем, устанавливаем его выше в define_equation
y0 = 3.0#значение y 0
inter = [0, 5]#промежуток по которому интегрируем

t, y = solve(equation, y0, inter) # находим массивы точек

visualize(t, y, equation) # вызываем функцию для графика
