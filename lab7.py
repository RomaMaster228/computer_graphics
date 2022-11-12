import PySimpleGUI as sg
import math
import matplotlib.pyplot as plt


def bezier_formula(n, t, index, def_points):
    return sum(math.comb(n - 1, i) * ((1 - t) ** (n - 1 - i)) * (t ** i) * def_points[i][index] for i in range(n))


def bezier_curve_explicit(def_points, speed=0.01):
    n = len(def_points)
    points = []
    for t in [_ * speed for _ in range(int((1 + speed * 2) // speed))]:  # get values between 0 and 1
        points.append([bezier_formula(n, t, 0, def_points), bezier_formula(n, t, 1, def_points)])
    return points


initial_data = [
    [0, 0],
    [0.625, 0.5],
    [1, 0.5],
]


def draw_bezier(data=initial_data):
    points = bezier_curve_explicit(data)
    plt.plot([point[0] for point in points], [point[1] for point in points], 'r')
    for point, name in zip(data, ("A", "B", "C")):
        plt.text(point[0], point[1], name, color='b')
    plt.plot([point[0] for point in data + [data[0]]], [point[1] for point in data + [data[0]]])
    plt.show()


layout = [
    [sg.Text('Points: '), sg.InputText()],
    [sg.Button('Plot'), sg.Button('Exit'), sg.Button('Enter')]]

window = sg.Window("Window", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Plot':
        draw_bezier()
    elif event == 'Enter':
        i = 2
        points = []
        for point in values[0].split():
            if i % 2 == 0:
                points.append([float(point[1:len(point) - 1])])
            else:
                points[-1].append(float(point[:len(point) - 1]))
            i += 1
        draw_bezier(points)
window.close()

# (1, 2) (20, 1) (15, 17)
# (3.5, 100) (7, 1.3) (15.9090, 17)
