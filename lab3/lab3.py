import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button, TextBox
from matplotlib.colors import LightSource

approximation = 4
alpha = 0.5
steps = 11
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Ellipsoid equation: x^2 / a^2 + y^2 / b^2 + z^2 / c^2 = 1
coefficients = (1, 2, 2)
rx, ry, rz = 1 / np.sqrt(coefficients)

u = np.linspace(0, 2 * np.pi, 40)
v = np.linspace(0, np.pi, 40)

x = rx * np.outer(np.cos(u), np.sin(v))
y = ry * np.outer(np.sin(u), np.sin(v))
z = rz * np.outer(np.ones_like(u), np.cos(v))

ax.plot_surface(x, y, z,  rstride=approximation, cstride=approximation, color='b', alpha=alpha, edgecolors="black")

max_radius = max(rx, ry, rz)
for axis in 'xyz':
    getattr(ax, 'set_{}lim'.format(axis))((-max_radius, max_radius))


def button_callback_remove(event):
    global alpha
    alpha = 1
    ax.plot_surface(x, y, z,  rstride=approximation, cstride=approximation, color='b', alpha=alpha, edgecolors="black")
    plt.draw()


button_ax_remove = fig.add_axes([0.6, 0.05, 0.31, 0.06])
button_remove = Button(button_ax_remove, "Remove invisible lines")
button_remove.on_clicked(button_callback_remove)


def button_callback_show(event):
    global alpha
    alpha = 0.5
    ax.plot_surface(x, y, z,  rstride=approximation, cstride=approximation, color='b', alpha=alpha, edgecolors="black")
    plt.draw()


button_ax_show = fig.add_axes([0.6, 0.15, 0.31, 0.06])
button_show = Button(button_ax_show, "Show invisible lines")
button_show.on_clicked(button_callback_show)


def turn_on_light(intensitivity=1):
    ls = LightSource()
    illuminated_surface = ls.shade(z, plt.cm.copper, fraction=float(intensitivity))
    ax.plot_surface(x, y, z,  rstride=approximation, cstride=approximation, color='b', alpha=alpha, edgecolors="black", antialiased=False, facecolors=illuminated_surface)
    plt.draw()


light_box = fig.add_axes([0.184, 0.15, 0.31, 0.06])
text_box_light = TextBox(light_box, "Turn on light: ")
text_box_light.on_submit(turn_on_light)


def change_approximation(new_approximation):
    global approximation, alpha
    approximation = steps - int(new_approximation)
    ax.clear()
    ax.plot_surface(x, y, z, rstride=approximation, cstride=approximation, color='b', alpha=alpha, edgecolors="black")
    max_radius = max(rx, ry, rz)
    for axis in 'xyz':
        getattr(ax, 'set_{}lim'.format(axis))((-max_radius, max_radius))
    ax.grid(None)
    ax.axis('off')
    plt.draw()


axbox = fig.add_axes([0.184, 0.05, 0.31, 0.06])
text_box_B = TextBox(axbox, "Approximation: ")
text_box_B.on_submit(change_approximation)
text_box_B.set_val(str(steps - approximation))

print("Approximataion from 1 to 10 only integers")
print("Light from 0 to 1")

ax.grid(None)
ax.axis('off')
plt.show()
