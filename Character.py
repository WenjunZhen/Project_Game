import matplotlib.image as mpimg 
from matplotlib import pyplot as plt
import numpy as np

class weapon:
    '''
    A class represent weapon,getting weapon from killing the monster
    '''
    def __init__(self,weapon_name,strength):
        '''
        Initialize the the weapon
        Given the name of the weapon and it's strength
        Args:
            None
        Return: 
            None
        '''
        self.weapon_name = weapon
        self.strength = strength
class character:
    '''
    A class represent the character, shows the status of the character
    '''
    def __init__(self, name, weapon, x_col = 0, y_col = 0, HP = 100,attack = 5):
        '''
        Initialize the name, read image, HP, attack,x and y of the character
        Args:
            None
        Return: 
            None
        '''
        self.name = name
        try:
            self.pic_character = mpimg.imread('character.jpg', format = "jpg").copy()
        except FileNotFoundError:
            print("We couldn't find this file or directory")
        self.weapon = weapon
        self.HP = HP
        self.attack = attack
        self.x = x_col
        self.y=y_col
    def show_status(self):
        '''
        Show the status of the character
        Args:
            Print out the attack and HP
        Return: 
            None
        '''
        print("Your Status")
        print("Attack = ",self.attack)
        print("HP = ", self.HP)

 
