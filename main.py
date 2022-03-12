######################### run the game ################################
from Map import Map
from Character import weapon, character
from MonsterAndGoodie import Monster
from function import moving, encounter, CheckEncounter, MonsterGenerator, game

# initialize the game
m = Map()
Weapon = weapon("Weapon",10)
Character = character("Tester",Weapon)
m.Create_character(Character)
EndPoint = Monster(23,23,"End Point",100,10)
m.Create_Monster(EndPoint)
MonsterIndex=[(23,23)]
MonsterList=[EndPoint]
MonsterGenerator(MonsterIndex, MonsterList, m)
# run the game
game(m, Character, MonsterList)
