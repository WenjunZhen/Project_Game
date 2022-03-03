
##################################################################################
############################## MONSTER CLASS ######################################

class Monster:

    def __init__(self, x_col, y_col, name, HP = 100, attack = 3):
        self.pic_monster = mpimg.imread('pic_monster.jpg', format = "jpg").copy()
        self.pic_goodie = mpimg.imread('pic_goodie.jpg', format = "jpg").copy()      
        self.len_pic_monster, self.wid_pic_monster = self.pic_monster.shape
        self.len_pic_goodie, self.wid_pic_goodie = self.pic_goodie.shape
        self.location = [x_col,y_col]
        self.HP = HP
        self.attack = attack
        self.name = name
    
    def location(self):
        return self.location
    
    def pic(self):
        if self.HP<=0:
            return self.pic_goodie
        else:
            return self.pic_monster
    
    def length(self):
        if self.HP<=0:
            return self.len_pic_goodie
        else:
            return self.len_pic_monster
        
    def width(self):
        if self.HP<=0:
            return self.wid_pic_goodie
        else:
            return self.wid_pic_monster
    
    def attack(self):
        return self.attack
    
    def BeAttacked(self,AttackFromCharacter):
        self.attack = self.attack - AttackFromCharacter
    
    def HP(self):
        return self.HP
    
    def name(self):
        return self.name

##################################################################################
############################## MAP CLASS ######################################

class Map:
    
    ......
    
    def Create_Monster(self,Monster):
        self.Map[Monster.x*Monster.length():(Monster.x + 1)*Monster.length(),
                 Monster.y*Monster.width():(Monster.y + 1)*Monster.width()] = Monster.pic()

################################################################################
############################## GENERAL FUNCTIONS ########################################

def encounter(character, Monster):
    #if the location of two overlaps:
    
    if Monster.HP()>0:
        print("You encountered a monster! Now let's fight!")
    
    while Monster.HP()>0: # and player's HP>0
        Monster.BeAttacked(playerAttack)
        # player be attacked by enenmy
        
    if Monster.HP()>0:
        print("So bad, you died! The Monster still has" + Monster.HP() + " more hit points!")
        return    
    
    if Monster.HP()<=0:
        answer = input("You found a Goodie! Select from 1) Torch, 2) Archor, 3) Armor.")
        if answer == "1":
            print("Now you have a torch in your hand, congratulations!")
            return
        elif answer == "2":
            print("Now you have a archor in your hand, congratulations!")
            return
        elif answer == "3":
            print("Now you have a armor in your hand, congratulations!")
            return
        else
            print("It's fine if you don't need anything.")
            return


