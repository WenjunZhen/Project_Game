######################### Implementing Function ################################
from Map import Map
from Character import weapon, character
from MonsterAndGoodie import Monster
import random as rand

def moving(m,c):
    
    m.Clean_character_position(c)
    

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
        
        
        if Monster.HP>0:
            print("You encountered a monster! Now let's fight!")
        else:
            return
    
        while Monster.HP>0 and character.HP>0:
            Monster.BeAttacked(character.attack)
            character.HP=character.HP - Monster.attack
            print("Monster attacked you! You now have " + str(character.HP) + " hit points!")
            print("You attacked the monster! It now has " + str(Monster.HP) + " hit points!")
        
        if Monster.HP>0:
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
            
def MonsterGenerator(MonsterIndex,MonsterList,Map):
    for i in range(30):
        x = rand.choice(list(range(24)))
        y = rand.choice(list(range(24)))
        while (x,y) in MonsterIndex or (x,y) in Map.wallIndex or (x,y) == (0,0):
            x = rand.choice(list(range(24)))
            y = rand.choice(list(range(24)))
        new_monster = Monster(x, y, "monster")
        Map.Create_Monster(new_monster)
        MonsterList.append(new_monster)
        MonsterIndex.append((x,y))
    

def game(Map,Character,MonsterList):
    while True:
        Map.printMap()
        Character.show_status()
        if moving(Map,Character) == 'E':
            break
        Map.Create_character(Character)
        CheckEncounter(MonsterList,Character)
