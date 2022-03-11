import matplotlib.image as mpimg 
from matplotlib import pyplot as plt
import numpy as np

from Character import weapon, character
from MonsterAndGoodie import Monster

class Map:
    '''
    a class for representing map, and it contains some 
    fucntions that can motify the map.
    '''
    def __init__(self):
        '''
        Initialize the map, read image:
        1. hw: horizontal wall (from view of user) with 200*1000 pixels
        2. vw: vertical wall (from view of user) with 1000*200 pixels
        3. floor: floor with 200*200 pixels.
        4. Map: a blank image.
        then set up map and walls layout, and store walls position in the map
        finally, store an original map, call it realMap
        Args:
            None
        Return: 
            None
        '''
        # read the images
        try:
            self.hw = mpimg.imread('hw.jpg', format = "jpg").copy()
            self.vw = mpimg.imread('vw.jpg', format = "jpg").copy()
            self.floor = mpimg.imread('floor.jpg', format = "jpg").copy()
            self.Map = mpimg.imread('blank.jpg', format = "jpg").copy()
        except FileNotFoundError:
            print("We couldn't find this file or directory")
        self.len_hw, self.wid_hw, self.pixels_hw = self.hw.shape
        self.len_vw, self.wid_vw, self.pixels_vw = self.vw.shape
        self.wallIndex = []
        
        # fill the map with floor.
        for i in range(24):
            for j in range(24):
                self.Map[i*200:(i+1)*200,j*200:(j+1)*200] = self.floor
        
        
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
                self.wallIndex.append((i*5+4+i+j,12))
        
        # store an original map, call it realMap 
        self.realMap = self.Map.copy()
        

    def printMap(self):
        '''
        print the map
        '''
        fig, ax = plt.subplots(1,figsize = (10,10))
        plt.imshow(self.Map)
        plt.show()

        
    def Create_Monster(self,Monster):
        '''
        show a Monster in the map based on its position
        Args:
            Monster: a Moster object.
        Return: 
            None
        '''        
        self.Map[Monster.x*200:(Monster.x + 1)*200,
                 Monster.y*200:(Monster.y + 1)*200] = Monster.pic()

    def Create_character(self,character):
        '''
        show a character in the map based on his position.
        Args:
            character: a character object.
        Return: 
            None
        ''' 
        self.Map[character.x*200:(character.x + 1)*200,
                 character.y*200:(character.y + 1)*200] = character.pic
        
    def Clean_character_position(self,character):
        '''
        recover the place to floor in the map after the character moves.
        Args:
            character: a character object.
        Return: 
            None
        '''
        self.Map[character.x*200:(character.x + 1)*200,
                 character.y*200:(character.y + 1)*200] = self.realMap[character.x*200:(character.x + 1)*200,
                                                                   character.y*200:(character.y + 1)*200]

    def check_character_position(self, character, direction):
        '''
        check the character if hit the wall or go out of the range.
        Args:
            character: a character object.
            direction: a char which means a direction.
        Return: 
            a bool value
        '''
        x = 0
        y = 0                      # initialize x and y to 0
        
        # set x and y based on direction
        if direction == "W":
            x-=1
        elif direction == "A":
            y-=1
        elif direction == "S":
            x+=1
        elif direction == "D":
            y+=1
        
        # check if the character is out of the range.
        if character.x+x > 23 or character.x+x < 0 or character.y+y > 23 or character.y+y < 0:
            print(f"You are out of range.")
            return False
        # check if the character hits a wall.
        elif (character.x+x, character.y+y) in self.wallIndex:
            print(f"You hit the wall.")
            return False
        else:
            return True
        
