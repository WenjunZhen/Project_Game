
##################################################################################
############################## MONSTER CLASS ######################################

class Monster:
    '''
    A class represent the monster, got some attack, HP and position
    '''
    def __init__(self, x_col, y_col, name, HP = 100, attack = 3):
        '''
        Initialize the name, read image:
        1.pic_monster: The one character going to kill
        2.pic_goodie: The thing character going to get from killing the monster
        3.pic_flag: end-point
        4.boss: final boss to kill
        Set the x, y, attack, and name for the monster
        Args:
            None
        Return: 
            None
        '''
        self.pic_monster = mpimg.imread('pic_monster.jpg', format = "jpg").copy()
        self.pic_goodie = mpimg.imread('pic_goodie.jpg', format = "jpg").copy()
        self.pic_flag = mpimg.imread('pic_flag.jpg', format = "jpg").copy()
        self.boss = mpimg.imread('boss.jpg', format = "jpg").copy()
        self.len_pic_monster, self.wid_pic_monster, self.pixels_pic_goodie = self.pic_monster.shape
        self.len_pic_goodie, self.wid_pic_goodie, self.pixels_pic_goodie = self.pic_goodie.shape
        self.x = x_col
        self.y = y_col
        self.HP = HP
        self.attack = attack
        self.name = name
    
    def pic(self):
        '''
        If the position x and y equal to 23 and if the HP less than 0,return pic_flasg or boss, else return pic_goodie or pic_monster
        Args:
             Set up and if statement and make one more if statement inside to determine the conditions satifie or not.
        Return: 
             return pic_flasg or boss, else return pic_goodie or pic_monster
        '''
        if self.x==23 and self.y==23:
            if self.HP<=0:
                return self.pic_flag
            else:
                return self.boss
        else:
            if self.HP<=0:
                return self.pic_goodie
            else:
                return self.pic_monster
    
    def length(self):
        '''
        set up a condition to determine return goodie or monster for length
        Args:
             Make an if statement
        Return: 
            self.len_pic_goodie or self.len_pic_monster
        '''
        if self.HP<=0:
            return self.len_pic_goodie
        else:
            return self.len_pic_monster
        
    def width(self):
        '''
        set up a condition to determine return goodie or monster for width
        Args:
             Make an if statement
        Return: 
             self.len_pic_goodie or self.len_pic_monster
        '''
        if self.HP<=0:
            return self.wid_pic_goodie
        else:
            return self.wid_pic_monster
    
    def attack(self):
        '''
        set up monster attack
        Args:
             None
        Return: 
           self.attack
        '''
        return self.attack
    
    def BeAttacked(self,AttackFromCharacter):
        '''
        Getting attack from character
        Args:
             Subtrack the HP from the attack damage
        Return: 
             None
        '''
        self.HP = self.HP - AttackFromCharacter
    
    def HP(self):
        '''
        Set up HP
        Args:
             None
        Return: 
            HP
        '''
        return self.HP
    
    def name(self):
        '''
        set up name
        Args:
             None
        Return: 
            name
        '''
        return self.name
    
    def x(self):
        '''
        set up x position
        Args:
             None
        Return: 
               self.x
        '''
        return self.x
    
    def y(self):
        '''
        set up y position
        Args:
             None
        Return: 
               self.y
        '''
        return self.y
