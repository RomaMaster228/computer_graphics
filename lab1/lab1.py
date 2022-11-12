import PySimpleGUI as sg
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, num=1000)


def y1(a):
    return (a ** (2 / 3) - abs(x) ** (2 / 3)) ** (3 / 2)


def y2(a):
    return -(a ** (2 / 3) - abs(x) ** (2 / 3)) ** (3 / 2)


def draw_plot(a=10):
    if a <= 0:
        sg.popup('Please, enter correct a value!')
    else:
        ax = plt.gca()
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.plot(x, y1(a), 'r', label=f"a = {a}")
        ax.plot(x, y2(a), 'r', label=r'$x ^ {\frac{2}{3}} + y ^ {\frac{2}{3}} = a ^ {\frac{2}{3}}$')
        ax.legend()
        plt.show()


layout = [
    [sg.Text('Parameter a:'), sg.InputText()],
    [sg.Button('Plot'), sg.Button('Exit'), sg.Button('Enter')]]

window = sg.Window("Window", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Plot':
        draw_plot()
    elif event == 'Enter':
        draw_plot(int(values[0]))
window.close()
