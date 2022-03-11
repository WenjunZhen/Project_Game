######################### Implementing Function ################################
from Map import Map
from Character import weapon, character
from MonsterAndGoodie import Monster
import random as rand

def moving(m,c):
    '''
    Ask user for input a direction or exit command and update
    character's position
    Args:
        m: a monster instance
        c: a character instance
    Return:
        a char which is a direction or exit command
    '''
    # detele last character position
    m.Clean_character_position(c)
    

    # ask for input and update update character's position
    answer = input("Please enter a movement W,A,S,D,E(E to exit): ")
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



def encounter(character, Monster):    
        '''
        character fights with monster and get a goodie
        Args:
        Monster: a monster instance
        Character: a character instance
        '''
        # check if the moster can fight with character
        if Monster.HP>0:
            print("You encountered a monster! Now let's fight!")
        else:
            return
        
        # battle in progress and determine who wins
        while Monster.HP>0 and character.HP>0:
            Monster.BeAttacked(character.attack)
            character.HP=character.HP - Monster.attack
            print("Monster attacked you! You now have " + str(character.HP) + " hit points!")
            print("You attacked the monster! It now has " + str(Monster.HP) + " hit points!")
        
        if character.HP<=0:
            print("So bad, you died! The Monster still has " + str(Monster.HP) + " more hit points!")
            return    
    
        if Monster.HP<=0:
            if Monster.x==23 and Monster.y==23:
                print("congraduation! You win the game! Cheers!")
                print("""☆ *　. 　☆
　　. ∧＿∧　∩　* ☆
* ☆ ( ・∀・)/ .
　. ⊂　　 ノ* ☆
☆ * (つ ノ .☆
　　 (ノ""")
                print("Enter E to exit")
                return
            
            # ask user to choose a goodie.
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
    '''
        check if character encounter a monster
        if so, call encounter()
        Args:
            Monster: a monster instance
            character: a character instance
    '''
    for i in range(len(Monsterlist)):
        if Monsterlist[i].x==character.x and Monsterlist[i].y==character.y:
            encounter(character,Monsterlist[i])
            break
            
def MonsterGenerator(MonsterIndex,MonsterList,Map):
    '''
        generate 30 monster randomly, and store their status and positions
        Args:
            MonsterIndex: a list of tuples to store positions
            MonsterList: a list of Monster instances
            Map: a Map instance

    '''
    for i in range(30):
        # generate a new monster positon.
        x = rand.choice(list(range(24)))
        y = rand.choice(list(range(24)))
        # if the new monster is in the wall, position of other monster, or position of character
        # generate a new monster positon.
        while (x,y) in MonsterIndex or (x,y) in Map.wallIndex or (x,y) == (0,0):
            x = rand.choice(list(range(24)))
            y = rand.choice(list(range(24)))
        # create the new monster.
        new_monster = Monster(x, y, "monster")
        Map.Create_Monster(new_monster)
        # update MonsterIndex and MonsterList
        MonsterList.append(new_monster)
        MonsterIndex.append((x,y))
    

def game(Map,Character,MonsterList):
    '''
    run the game
    Args:
        Map: a Map instance
        Character: a character instance
        MonsterList: a list of Monster instances
    '''
    while True:
        # show the map
        Map.printMap()
        # show the character's status
        Character.show_status()
        # determine if exit the game
        if Character.HP <= 0 or moving(Map,Character) == 'E':
            break
        # update character position and check if he need to fight with a monster
        Map.Create_character(Character)
        CheckEncounter(MonsterList,Character)

