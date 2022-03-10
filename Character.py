class weapon:
    def __init__(self,weapon_name,strength):
        self.weapon_name = weapon
        self.strength = strength
class character:
    def __init__(self, name, weapon, HP = 100,attack = 5):
        self.name = name
        try:
        self.pic_character = mpimg.imread('character.jpg', format = "jpg").copy()
        except FileNotFoundError:
            print("We couldn't find this file or directory")
        self.weapon = weapon
        self.HP = HP
        self.attack = attack
    def show_status(self):
        print("Your Status")
        print("Attack = ",self.attack)
        print("HP = ", self.HP)
    def __del__(self):
        return(self.name," You Died!")
 
class Map:
    def Create_character(self,character):
        self.Map[character.x*character.length():(character.x + 1)*character.length(),
                 character.y*character.width():(character.y + 1)*character.width()] = character.pic() 

Game_Over = False 
while (Game_Over == False):
    answer = input("Please enter a movement W,A,S,D: ")
    if answer == "W":
        y+=1
    elif answer == "A":
        x-=1
    elif answer == "S":
        y-=1
    elif answer == "D":
        x+=1
