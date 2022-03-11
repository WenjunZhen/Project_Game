
##################################################################################
############################## MONSTER CLASS ######################################

class Monster:

    def __init__(self, x_col, y_col, name, HP = 100, attack = 3):
        self.pic_monster = mpimg.imread('pic_monster.jpg', format = "jpg").copy()
        self.pic_goodie = mpimg.imread('pic_goodie.jpg', format = "jpg").copy()
        self.pic_flag = mpimg.imread('pic_flag.jpg', format = "jpg").copy()
        self.len_pic_monster, self.wid_pic_monster, self.pixels_pic_goodie = self.pic_monster.shape
        self.len_pic_goodie, self.wid_pic_goodie, self.pixels_pic_goodie = self.pic_goodie.shape
        self.x = x_col
        self.y = y_col
        self.HP = HP
        self.attack = attack
        self.name = name
    
    def pic(self):
        if self.x==23 and self.y==23:
            return self.pic_flag
        else:
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
        self.HP = self.HP - AttackFromCharacter
    
    def HP(self):
        return self.HP
    
    def name(self):
        return self.name
    
    def x(self):
        return self.x
    
    def y(self):
        return self.y

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
        if Monster.x==23 and Monster.y==23:
            print("congraduation! You win the game! Cheers!")
            print("""☆ *　. 　☆
　　. ∧＿∧　∩　* ☆
* ☆ ( ・∀・)/ .
　. ⊂　　 ノ* ☆
☆ * (つ ノ .☆
　　 (ノ""")
            return
        
        if Monster.HP>0:
            print("You encountered a monster! Now let's fight!")
    
        while Monster.HP>0 and character.HP>0:
            Monster.BeAttacked(character.attack)
            character.HP=character.HP - Monster.attack
            print("Monster attacked you! You now have " + str(character.HP) + " hit points!")
            print("You attacked the monster! It now has " + str(Monster.HP) + " hit points!")
        
        if Monster.HP>0:
            print("So bad, you died! The Monster still has " + str(Monster.HP) + " more hit points!")
            return    
    
        if Monster.HP<=0:
            answer = input("You found a Goodie! Select from 1) Torch, 2) Archor, 3) Armor.")
            if answer == "1":
                print("Now you have a torch in your hand, congratulations!")
                print("Currently its a useless tool, but you looks fancier!")
                return
            elif answer == "2":
                print("Now you have a archor in your hand, congratulations!")
                character.attack = character.attack + 10
                print("Your Attacks increased by 10!")
                return
            elif answer == "3":
                print("Now you have a armor in your hand, congratulations!")

                character.HP = character.HP + 50
                print("Your Hitpoints increased by 50!")
                return
            else:
                print("It's fine, you don't have to select a goodie. It's not a bad idea to rely only on yourself!")
                return
                  
def CheckEncounter(Monsterlist,character):
    for i in range(len(Monsterlist)):
        if Monsterlist[i].x==character.x and Monsterlist[i].y==character.y:
            encounter(character,Monsterlist[i])
            break


