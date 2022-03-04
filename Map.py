import matplotlib.image as mpimg 
from matplotlib import pyplot as plt
import numpy as np
class Map:
    def __init__(self):
        self.hw = mpimg.imread('hw.jpg', format = "jpg").copy()
        self.vw = mpimg.imread('vw.jpg', format = "jpg").copy()
        self.darkness = mpimg.imread('darkness.jpg', format = "jpg").copy()
        self.floor = mpimg.imread('floor.jpg', format = "jpg").copy()
        self.Map = mpimg.imread('blank.jpg', format = "jpg").copy()
        self.character = mpimg.imread('character.jpg', format = "jpg").copy()
        self.len_hw, self.wid_hw, self.pixels_hw = self.hw.shape
        self.len_vw, self.wid_vw, self.pixels_vw = self.vw.shape
        self.visiableIndex = {}
        self.wallIndex = []
        
        for i in range(24):
            for j in range(24):
                self.Map[i*200:(i+1)*200,j*200:(j+1)*200] = self.floor
                self.visiableIndex[(i,j)] = False
        
        
        # outer four horizontal walls
        for i in range(2):
            self.Map[(0)*self.len_hw+600:(1)*self.len_hw+600,(3*i)*self.wid_hw+400:(3*i+1)*self.wid_hw+400] = self.hw
            for j in range(5):
                self.wallIndex.append((3,i*15+2+j))
            self.Map[(0)*self.len_hw+4200:(1)*self.len_hw+4200,(3*i)*self.wid_hw+400:(3*i+1)*self.wid_hw+400] = self.hw
            for j in range(5):
                self.wallIndex.append((21,i*15+2+j))
        
        
        # outer four vertical walls
        self.Map[(0)*self.len_vw+800:(1)*self.len_vw+800,(0)*self.wid_vw+200:(1)*self.wid_vw+200] = self.vw
        for i in range(5):
                self.wallIndex.append((4+i,1))
        self.Map[(0)*self.len_vw+800:(1)*self.len_vw+800,(0)*self.wid_vw+4400:(1)*self.wid_vw+4400] = self.vw
        for i in range(5):
                self.wallIndex.append((4+i,22))
        self.Map[(0)*self.len_vw+3200:(1)*self.len_vw+3200,(0)*self.wid_vw+200:(1)*self.wid_vw+200] = self.vw
        for i in range(5):
                self.wallIndex.append((16+i,1))
        self.Map[(0)*self.len_vw+3200:(1)*self.len_vw+3200,(0)*self.wid_vw+4400:(1)*self.wid_vw+4400] = self.vw
        for i in range(5):
                self.wallIndex.append((16+i,22))
                
                
        # inner four horizontal walls
        for i in range(2):
            self.Map[(0)*self.len_hw+1600:(1)*self.len_hw+1600,(2*i)*self.wid_hw+1000:(2*i+1)*self.wid_hw+1000] = self.hw
            for j in range(5):
                self.wallIndex.append((8,i*10+5+j))
            self.Map[(0)*self.len_hw+3200:(1)*self.len_hw+3200,(2*i)*self.wid_hw+1000:(2*i+1)*self.wid_hw+1000] = self.hw
            for j in range(5):
                self.wallIndex.append((16,i*10+5+j))
        
        
        # left-middle and right-middle two vertical walls
        self.Map[(0)*self.len_vw+2000:(1)*self.len_vw+2000,(0)*self.wid_vw+600:(1)*self.wid_vw+600] = self.vw
        for i in range(5):
                self.wallIndex.append((10+i,3))
        self.Map[(0)*self.len_vw+2000:(1)*self.len_vw+2000,(0)*self.wid_vw+4000:(1)*self.wid_vw+4000] = self.vw
        for i in range(5):
                self.wallIndex.append((10+i,20))
        
        
        # central three vertical walls
        for i in range(3):
            self.Map[(i)*self.len_vw+800+200*i:(i+1)*self.len_vw+800+200*i,(0)*self.wid_vw+2400:(1)*self.wid_vw+2400] = self.vw
            for j in range(5):
                self.wallIndex.append((i*5+4+1+j,12))
        
        
        self.realMap = self.Map
        
        self.Map[0:200,0:200] = self.character
        
        #for i in range(24):
            #for j in range(24):
                #self.Map[i*self.len_floor:(i+1)*self.len_floor,j*self.wid_floor:(j+1)*self.wid_floor] = self.darkness

    def printMap(self):
        fig, ax = plt.subplots(1,figsize = (10,10))
        plt.imshow(self.Map)
        
    def updateVisiableMap(self):
        for i in range(24):
            for j in range(24):
                if visiableIndex[(i,j)]:
                    self.Map[i*self.len_floor:(i+1)*self.len_floor,
                             j*self.wid_floor:(j+1)*self.wid_floor] = self.realMap[i*self.len_floor:(i+1)*self.len_floor,
                                                                                   j*self.wid_floor:(j+1)*self.wid_floor]

        
m = Map()
m.printMap()
