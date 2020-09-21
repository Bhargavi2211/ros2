from array import *
import matplotlib.pyplot as plt
x_pos = 0
y_pos = 0
mag = 0.1
arr_x = array('f', [])
arr_y = array('f', [])


def velocity_vector(way_x, way_y):
    x = x_pos
    y = y_pos
    distance = (((x_pos - way_x) ** 2 + (y_pos - way_y) ** 2) ** 0.5)
    vector_x = (((way_x - x_pos) / distance) * 0.1)
    vector_y = (((way_y - y_pos) / distance) * 0.1)
    while (vector_x < way_x) and (vector_y < way_y):
        x = x + vector_x
        y = y + vector_y

        if x >= way_x and y >= way_y:
            print(str(way_x) + "i + " + str(way_y) + "j")
            break
        else:
            print(str(x) + "i + " + str(y) + "j")
            arr_x.append(x)
            arr_y.append(y)


for j in range(0, 5):
    waypoint = input()
    msg = waypoint.split()
    way_x = float(msg[0])
    way_y = float(msg[1])
    velocity_vector(way_x, way_y)
    arr_x.append(way_x)
    arr_y.append(way_y)
    x_pos = arr_x[-1]
    y_pos = arr_y[-1]
plt.plot(arr_x, arr_y, linewidth=2.0)
plt.show()
