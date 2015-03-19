#take two of pokemon game, going to define pokemon as a class and have the battle as a function of that class

import random     

Vinewhip= random.randint(10,15)
Razorleaf = random.randint(15,25)
Solarbeam = random.randint(20,30)
Cut = random.randint(10,15)
Flamethrower = random.randint(20,25)
Slam = random.randint(10,20)
Thunder = random.randint(25,30)
Thunderbolt = random.randint(15,20)
Tackle = random.randint(10,15)
Bite = random.randint(20,30)
Hyperbeam = random.randint(25,35)
Slash = random.randint(15,20)
Watercanon = random.randint(20,25)
Squirt= random.randint(15,20)
Hydropump = random.randint(25,35)
Ember = random.randint(10,15)
Firekick = random.randint(15,20)
Flametempest = random.randint(20,25)
class Pokemon(object):
    #the pokemon
    def __init__(self, name, hp, type, attack1, attack2, attack3, attack4):
        self.name = name
        self.hp = 100
        self.type = type
        self.attack1 = attack1
        self.attack2 = attack2
        self.attack3 = attack3
        self.attack4 = attack4
        
Absol = Pokemon('Absol', 100, 'Dark', Bite, Hyperbeam, Tackle, Slash)

Charizard = Pokemon('Charizard', 100, 'Fire/Flying', Flamethrower, Ember, Firekick, Flametempest)

Blastoise = Pokemon('Blastoise', 100,'Water',Watercanon, Squirt, Tackle,Hydropump)

Venasaur = Pokemon('Venasaur', 100, 'Grass', Vinewhip, Razorleaf, Solarbeam, Cut)

Pikachu = Pokemon('Pikachu', 100, 'Electric', Slam, Thunder, Thunderbolt, Tackle)



print "Choose your Pokemon!"

selection = raw_input('Absol, Charizard, Blastoise, Venasaur, Pikachu: ')

if selection == 'Absol':
    pokemon1 = Absol
else:
    if selection == 'Charizard':
        pokemon1 = Charizard
    elif selection == 'Blastoise':
        pokemon1 = Blastoise
    elif selection == 'Venasaur':
        pokemon1 = Venasaur
    elif selection == 'Pikachu':
        pokemon1 = Pikachu
        
Enemy = random.choice([Absol, Charizard, Blastoise, Venasaur, Pikachu])

if Enemy == pokemon1:
    Enemy = random.choice([Absol, Charizard, Blastoise, Venasaur, Pikachu])
    
print "Your Rival chose " + str(Enemy)
