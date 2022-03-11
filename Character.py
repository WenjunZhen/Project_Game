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
    def __init__(self, name, weapon, HP = 100,attack = 5):
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
    def __del__(self):
        '''
        The character is death
        Args:
            None
        Return: 
            name and you died
        '''
        return(self.name," You Died!")
 

def moving(m,c):
    
    m.Clean_character_position(c)
    answer = input("Please enter a movement W,A,S,D,E: ")
    if m.check_character_position(c, answer):
        if answer == "W":
             c.x-=1
        elif answer == "A":
            c.y-=1
        elif answer == "S":
            c.x+=1
        elif answer == "D":
             c.y+=1

        m.Create_character(c)
        return answer
        
################################################# Monster Generator        
for i in range(30):
    aa = Monster(np.random.choice(2),np.random.choice(20),"Area1")
    bb = Monster(random.randrange(5,8),random.randrange(2,9),"Area2")
    cc = Monster(random.randrange(5,8),random.randrange(14,21),"Area3")
    dd = Monster(random.randrange(10,16),random.randrange(4,11),"Area4")
    ee = Monster(random.randrange(10,14),random.randrange(14,19),"Area5")
    ff = Monster(random.randrange(16,19),random.randrange(2,9),"Area6")
    gg = Monster(random.randrange(16,19),random.randrange(14,21),"Area7")
    list = [aa,bb,cc,dd,ee,ff,gg]
    d = random.choice(list)
    m.Create_Monster(d)
