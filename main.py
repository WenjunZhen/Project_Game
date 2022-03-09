######################### Implementing Main Function ################################


def moving(m,c):
    Game_Over = False
    
    m.Clean_character_position(c)
    
    if Game_Over == False:
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
            elif answer == "E":
                Game_Over = True        

        m.Create_character(c)



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

            
            ########################## item Creation ##############################
m = Map()

Weapon = weapon("Test Weapon",10)
Character = character("Tester",Weapon)

EndPoint = Monster(23,23,"End Point",0)
m.Create_Monster(EndPoint)

Monster1 = Monster(1,6,"Monster1",1)
m.Create_Monster(Monster1)

Monster2 = Monster(10,7,"Monster2",1)
m.Create_Monster(Monster2)

Monster3 = Monster(15,5,"Monster3",1)
m.Create_Monster(Monster3)

MonsterList=[Monster1, Monster2, Monster3, EndPoint]

def game():
    while True:
        m.printMap()
        Character.show_status()
        moving(m,Character)
        m.Create_character(Character)
        CheckEncounter(MonsterList,Character)

######################## Game Interface #########################

game()
