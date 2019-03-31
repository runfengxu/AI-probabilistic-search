import numpy as np
import random
from enum import Enum
import copy
import pygame
from pygame.locals import *

BLOCK_DIM = 50
SIZE = 18
initial_Prob = 1/BLOCK_DIM**2
SCREEN_DIM = BLOCK_DIM * SIZE
LINE_WIDTH = 2
TOTAL_LINE = LINE_WIDTH * BLOCK_DIM + 1

FN_FLAT = 0.1
FN_HILL = 0.3
FN_FOREST = 0.7
FN_MAZE_CAVE = 0.9

P_FLAT = 0.25
P_HILL = 0.25 + P_FLAT
P_FOREST = 0.25 + P_HILL
P_MAZE_CAVE = 0.25 + P_FOREST

colorFlat = (255,255,255)
colorHill = (175, 175, 175)
colorForest = (34, 139, 34)
colorMaze_Cave = (77, 77, 77)
red = (200,0,0)

class RevealStatus(Enum):
    cover = 1
    uncover = 2


class cell:
    def __init__(self, x, y, t, FN, initial_Prob, status=RevealStatus.cover):
        self._x = x
        self._y = y
        self._t = t
        self._FN = FN
        self._Prob = initial_Prob
        self._status = RevealStatus.cover

    def __repr__(self):
        return str(self._t)

    def get_FN(self):
        return self._FN

    FN = property(fget=get_FN)

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    x = property(fget=get_x, fset=set_x)

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

    y = property(fget=get_y, fset=set_y)

    def get_Prob(self):
        return self._Prob

    def set_Prob(self, Prob):
        self._Prob = Prob

    Prob = property(fget=get_Prob, fset=set_Prob)

    def get_status(self):
        return self._status

    def set_status(self, input_status):
        self._status = input_status

    status = property(fget=get_status, fset=set_status)


class terrain:
    def __init__(self, input_M=[]):
        if not input_M:
            self.M = np.random.rand(BLOCK_DIM, BLOCK_DIM)
            self.generate_terrain()
        else:
            self.M = input_M
        self._block = [[cell(i, j, self.get_terrain(self.M[i, j]), self.M[i, j], initial_Prob)
                        for i in range(BLOCK_DIM)] for j in range(BLOCK_DIM)]

        self._targetX, self._targetY = self.set_target()

    def generate_terrain(self):
        flat = self.M < P_FLAT
        hill = self.M < P_HILL
        forest = self.M < P_FOREST
        maze_cave = self.M < P_MAZE_CAVE

        self.M[maze_cave] = FN_MAZE_CAVE
        self.M[forest] = FN_FOREST
        self.M[hill] = FN_HILL
        self.M[flat] = FN_FLAT

    def get_terrain(self, FN):
        if FN == FN_FLAT:
            return "flat"
        elif FN == FN_HILL:
            return "hill"
        elif FN == FN_FOREST:
            return "forest"
        else:
            return "maze_cave"

    def get_cell(self, x, y):
        return self._block[x][y]

    def set_target(self):
        target = np.random.randint(0, BLOCK_DIM, 2)
        return target[0], target[1]

    def get_target(self):
        return self._targetX, self._targetY