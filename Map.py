import matplotlib.image as mpimg 
from matplotlib import pyplot as plt
import numpy as np
class Map:
    def __init__(self):
        self.hw = mpimg.imread('hw.jpg', format = "jpg").copy()
        self.vw = mpimg.imread('vw.jpg', format = "jpg").copy()
        self.floor = mpimg.imread('floor.jpg', format = "jpg").copy()
        self.Map = mpimg.imread('blank.jpg', format = "jpg").copy()
        self.len_floor, self.wid_floor, self.pixels_floor = self.floor.shape
        self.len_hw, self.wid_hw, self.pixels_hw = self.hw.shape
        self.len_vw, self.wid_vw, self.pixels_vw = self.vw.shape
        for i in range(24):
            for j in range(24):
                self.Map[i*self.len_floor:(i+1)*self.len_floor,j*self.wid_floor:(j+1)*self.wid_floor] = self.floor
        for i in range(3):
            self.Map[(5*i+2)*self.len_hw:(5*i+3)*self.len_hw,(i+1)*self.wid_hw:(i+2)*self.wid_hw] = self.hw
        for i in range(3):
            self.Map[(i)*self.len_vw+600:(i+1)*self.len_vw+600,(5*i+4)*self.wid_vw:(5*i+5)*self.wid_vw] = self.vw
        for i in range(3,6):
            self.Map[(4*i+2)*self.len_hw:(4*i+3)*self.len_hw,1*self.wid_hw-200:2*self.wid_hw-200] = self.hw

    def printMap(self):
        fig, ax = plt.subplots(1)
        plt.imshow(self.Map)
        
m = Map()
m.printMap()
