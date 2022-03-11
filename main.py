######################### run the game ################################

m = Map()
Weapon = weapon("Weapon",10)
Character = character("Tester",Weapon)

EndPoint = Monster(23,23,"End Point",100,10)
m.Create_Monster(EndPoint)
MonsterIndex=[(23,23)]
MonsterList=[EndPoint]

MonsterGenerator(MonsterIndex, MonsterList, m)

game(m, Character)
