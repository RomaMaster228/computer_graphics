import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.widgets import Button

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [0, 0, 0, 0]
y = [2, 8, 8, 2]
z = [0, 0, 4, 4]
sides = [list(zip(x, y, z))]

x = [0, 8, 8, 0]
y = [2, 2, 8, 8]
z = [0, 0, 0, 0]
sides.append(list(zip(x, y, z)))

x = [8, 8, 8, 8]
y = [2, 2, 8, 8]
z = [8, 0, 0, 8]
sides.append(list(zip(x, y, z)))

x = [0, 8, 8, 0]
y = [2, 2, 2, 2]
z = [0, 0, 8, 4]
sides.append(list(zip(x, y, z)))

x = [0, 8, 8, 0]
y = [8, 8, 8, 8]
z = [0, 0, 8, 4]
sides.append(list(zip(x, y, z)))

x = [0, 0, 8, 8]
y = [8, 2, 2, 8]
z = [4, 4, 8, 8]
sides.append(list(zip(x, y, z)))

poly = Poly3DCollection(sides, alpha=0.5, edgecolors='black')

ax.add_collection3d(poly)

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)


def button_callback_remove(event):
    ax.add_collection3d(Poly3DCollection(sides, alpha=1, edgecolors='black'))
    plt.draw()


button_ax_remove = fig.add_axes([0.5, 0.05, 0.31, 0.06])
button_remove = Button(button_ax_remove, "Remove invisible lines")
button_remove.on_clicked(button_callback_remove)


def button_callback_show(event):
    ax.add_collection3d(Poly3DCollection(sides, alpha=0.5, edgecolors='black'))
    plt.draw()


button_ax_show = fig.add_axes([0.5, 0.15, 0.31, 0.06])
button_show = Button(button_ax_show, "Show invisible lines")
button_show.on_clicked(button_callback_show)


def button_callback_isometric(event):
    ax.view_init(20, 145)
    plt.draw()


button_ax_isometric = fig.add_axes([0.1, 0.05, 0.31, 0.06])
button_isometric = Button(button_ax_isometric, "Isometric projection")
button_isometric.on_clicked(button_callback_isometric)


def button_callback_orthographic_top(event):
    ax.view_init(90)
    plt.draw()


button_ax_orthographic_top = fig.add_axes([0.1, 0.15, 0.31, 0.06])
button_orthographic_top = Button(button_ax_orthographic_top, "Top orthographic projection")
button_orthographic_top.on_clicked(button_callback_orthographic_top)


def button_callback_orthographic_hip(event):
    ax.view_init(0, 90)
    plt.draw()


button_ax_orthographic_front = fig.add_axes([0.1, 0.85, 0.31, 0.06])
button_orthographic_front = Button(button_ax_orthographic_front, "Side orthographic projection")
button_orthographic_front.on_clicked(button_callback_orthographic_hip)

ax.grid(None)
ax.axis('off')
plt.show()
