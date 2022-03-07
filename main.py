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
        if Monster.HP>0:
            print("You encountered a monster! Now let's fight!")
    
        while Monster.HP>0 or character.HP>0:
            Monster.BeAttacked(10)
        # player be attacked by enenmy
        
            if Monster.HP>0:
                print("So bad, you died! The Monster still has " + str(Monster.HP) + " more hit points!")
                return    
    
            if Monster.HP<=0:
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
                else:
                    print("It's fine if you don't need anything.")
                    return
                  
m = Map()
w = weapon("name",10)
c = character("hello",w)
c.show_status()
m.printMap()
moving(m,c)
m.Create_character(c)
