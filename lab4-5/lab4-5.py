import math
import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


# параметры освещения
light_pos = (20, 30, 30)  # положение источника света
light_intensity = 5  # интенсивность света
reflection = 115  # параметр отражения
# фоновое освещение - окружающее освещеие, которое всегда будет придавать объекту некоторый оттенок
ambient = [0.8, 0.0, 0.0, 0.5]
# диффузное освещение - имитирует воздействие на объект направленного источника света
diffuse = [1.0, 0.0, 0.0, light_intensity]
# зеркальный свет - устанавливает цвет блика на объекте
specular = [1.0, 0.0, 0.0, light_intensity]

# вращение
x_rot = 0
y_rot = -40
z_rot = 0

# параметры эллипсоида
approximation = 35  # количество образующих
size = 1
a, b, c = 6, 4, 4


def init():
    glClearColor(255, 255, 255, 1.0)  # белый цвет для первоначальной закраски
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)  # обновляем буфер глубины
    glDepthFunc(GL_LEQUAL)
    glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)  # сглаженные полигоны, больше пикселей для отрисовки
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)  # хорошее качество текстур, цветов
    glEnable(GL_NORMALIZE)
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)  # определяем текущую модель освещения
    glEnable(GL_LIGHTING)  # включаем освещение
    glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)  # вершины заднего многоугольника зажигаются с помощью параметров
    # заднего материала и имеют обратную норму перед вычислением уравнения освещения


def ellipsoid():
    global a, b, c, approximation
    latitude_delta = math.pi / approximation
    longitude_delta = 2 * math.pi / approximation
    vertices = []

    for i in range(approximation + 1):
        lat = i * latitude_delta
        for j in range(approximation + 1):
            lon = j * longitude_delta
            x = a * math.sin(lat) * math.cos(lon)
            y = b * math.sin(lat) * math.sin(lon)
            z = c * math.cos(lat)
            vertices.append([x, y, z])
    for i in range(approximation + 1):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(approximation + 1):
            glVertex3fv(vertices[j + i * approximation])
            glVertex3fv(vertices[j + (i + 1) * approximation])
        glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(10, 10, 10, 0, 0, 0, 0, 0, 2)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glTranslatef(size, size, size)
    init_lighting()
    glRotatef(x_rot, 1, 0, 0)
    glRotatef(y_rot, 0, 0, 1)
    glRotatef(z_rot, 0, 1, 0)

    glPushMatrix()  # сохраняем текущее положение "камеры"
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, diffuse)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, specular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 128 - reflection)
    ellipsoid()
    glPopMatrix()  # возвращаем сохраненное положение "камеры"
    glutSwapBuffers()  # выводим все нарисованное в памяти на экран


def init_lighting():
    glEnable(GL_LIGHT0)  # включаем один источник света
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)  # определяем положение источника света

    l_dif = (2.0, 2.0, 3.0, light_intensity)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, l_dif)
    l_dir = (light_pos[0], light_pos[1], light_pos[2], 1.0)
    glLightfv(GL_LIGHT0, GL_POSITION, l_dir)

    # делаем затухание света
    attenuation = float(101 - light_intensity) / 25.0
    distance = math.sqrt(pow(light_pos[0], 2) + pow(light_pos[1], 2) + pow(light_pos[2], 2))
    constant_attenuation = attenuation / 3.0
    linear_attenuation = attenuation / (3.0 * distance)
    quadratic_attenuation = attenuation / (3.0 * distance * distance)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, constant_attenuation)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, linear_attenuation)
    glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, quadratic_attenuation)


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, float(width) / float(height), 1.0, 60.0)  # 1) угол, под которым пользователь видит фигуру, по y;
    # 2) отношение x/y, которое задаёт положение по x; 3) расстояние до ближней плоскости; 4) до дальней плоскости
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1, 0)


def specialkeys(key, x, y):
    global x_rot, y_rot, z_rot, size, approximation, light_intensity
    if key == b'w':
        x_rot += 5  # вращаем на 5 градусов по оси X
    if key == b's':
        x_rot -= 5  # вращаем на -5 градусов по оси X
    if key == b'a':
        y_rot += 5  # вращаем на 5 градусов по оси Y
    if key == b'd':
        y_rot -= 5  # вращаем на -5 градусов по оси Y
    if key == b'q':
        z_rot += 5  # вращаем на 5 градусов по оси Z
    if key == b'e':
        z_rot -= 5  # вращаем на -5 градусов по оси Z
    if key == b'=':
        size += 1  # увеличиваем размер на 1
    if key == b'-':
        size -= 1  # уменьшаем размер на 1
    if key == b'p':
        approximation += 1  # увеличиваем число образующих на 1
    if key == b'o':
        approximation -= 1  # уменьшаем число образующих на 1
        approximation = max(10, approximation)
    if key == b'l':
        light_intensity += 5  # увеличиваем интенсивность света на 5
        light_intensity = min(100, light_intensity)
    if key == b'k':
        light_intensity -= 5  # уменьшаем интенсивность света на 5
        light_intensity = max(-100, light_intensity)

    glutPostRedisplay()  # вызываем процедуру перерисовки


def main():
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)  # используем двойную буферизацию и формат RGB
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutInit(sys.argv)  # инициализируем opengl
    glutCreateWindow("lab 4-5")
    glutDisplayFunc(display)  # определяем функцию для отрисовки
    glutReshapeFunc(reshape)  # определяем функцию для масштабирования
    glutKeyboardFunc(specialkeys)  # определяем функцию для обработки нажатия клавиш
    init()
    glutMainLoop()


if __name__ == "__main__":
    print("Rotation:")
    print("OX: W S")
    print("OY: A D")
    print("OZ: Q E")
    print()
    print("Change figure size: - +")
    print("Change approximation: o p")
    print("Change light intensity: k l")
    main()
