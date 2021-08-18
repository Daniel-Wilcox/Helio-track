import numpy as np
import matplotlib.pyplot as plt

import os
os.system('clear')


# parabolic mirror
mirror_radius = 1  # meters
num_nodes = 100


class MirrorNodes:

    a = 1

    def __init__(self, mirror_radius, num_nodes):
        self.mirror_radius = mirror_radius
        self.num_nodes = num_nodes
        self.x = np.linspace(0, self.mirror_radius, self.num_nodes)
        self.y = a*np.square(self.x)

    def __str__(self):
        return "Print for this class is not complete"

    def get_half_xy(self):
        return [self.x, self.y]

    def calc_focal_points(self, light_angle):

        return


def init_nodal_points(num_nodes, mirror_radius):
    #y = ax^2
    a = 1
    x = np.linspace(0, mirror_radius, num_nodes)
    y = a*np.square(x)
    return [x, y]


os.system('clear')

test = MirrorNodes(mirror_radius, num_nodes)
nodes = test.get_half_xy()
# nodes = init_nodal_points(num_nodes, mirror_radius)
# print(nodes)
plt.plot(nodes[0], nodes[1])
plt.show()
# print("DONE")
