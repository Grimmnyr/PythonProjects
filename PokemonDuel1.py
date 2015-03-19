import random

#test pokemon like game, will add gui later

pokemon1 = 100
enemy = 100
#Let's user choose the pokemon to duel with
print "Choose your Pokemon!"
Selection = raw_input('Absol Charizard Blastoise Venasaur Pikachu: ')
if Selection == Absol:
    pokemon1 = Absol
else:
    if Selection == Charizard:
        pokemon1 = Charizard
    elif Selection == Blastoise:
        pokemon1 = Blastoise
    elif Selection == Venasaur:
        pokemon1 = Venasaur
    elif Selection == Pikachu:
        pokemon1 = Pikachu
    else:
        print "Please type out the full name"

enemy = random.choice([Absol, Charizard, Blastoise, Venasaur, Pikachu])
if enemy == pokemon1:
    enemy = random.choice([Absol, Charizard, Blastoise, Venasaur, Pikachu])

#names the user's pokemon


#the duel
for turn in range(1000):
    #setting up the parameters for the attacks
    if pokemon1 == Charizard:
        cAttacks = raw_input.lower(('Flamethrower Ember Firekick Flame Tempest: '))
        flamethrower = random.randint(20,30)
        ember = random.randint(10,15)
        firekick = random.randint(15,20)
        flametempest = random.randint(20,25)
        if cAttacks == flamethrower:
            damage= enemy - flamethrower
            print 'Charizard used Flamethrower, %s took %d damage' % (enemy)(damage)
        else:
            if cAttacks == ember:
                damage= enemy-ember
                print 'Charizard used Ember, %s took %d damage' % (enemy)(damage)
            
            elif cAttacks == firekick:
                damage = enemy-firekick
                print 'Charizard used Firekick, %s took %d damage' % (enemy)(damage)
            
            elif cAttacks == flametempest:
                damage = enemy-flametempest
                print 'Charizard used Flametempest, %s took %d damage' % (enemy)(damage)
            
            else:
                print "Please type the full attack"
    else:
        if pokemon1 == Blastoise:
            bAttacks = raw_input.lower(('WaterCanon Squirt Tackle Hydropump: '))
            watercanon = random.randint(20,25)
            squirt= random.randint(15,20)
            tackle = random.randint(15,20)
            hydropump = random.randint(25,35)
            if bAttacks == watercanon:
                damage= enemy - watercanon
                print 'Blastoise used Watercanon, %s took %d damage' % (enemy)(damage)
            else:
                if bAttacks == squirt:
                    damage= enemy-squirt
                    print 'Blastoise used Squirt, %s took %d damage' % (enemy)(damage)
                
                elif bAttacks == tackle:
                    damage = enemy-tackle
                    print 'Blastoise used Tackle, %s took %d damage' % (enemy)(damage)
                
                elif bAttacks == hydropump:
                    damage = enemy-hydropump
                    print 'Blastoise used hydropump, %s took %d damage' % (enemy)(damage)
                
                else:
                    print "Please type the full attack"            
        if pokemon1 == Venasaur:
            vAttacks = raw_input.lower(('VineWhip RazorLeaf SolarBeam Cut: '))
            vinewhip= random.randint(10,15)
            razorleaf = random.randint(15,25)
            solarbeam = random.randint(20,30)
            cut = random.randint(10,15)
            if vAttacks == vinewhip:
                damage= enemy - vinewhip
                print 'Venasaur used VineWhip, %s took %d damage' % (enemy)(damage)
            else:
                if vAttacks == razorleaf:
                    damage= enemy-razorleaf
                    print 'Venasaur used RazorLeaf, %s took %d damage' % (enemy)(damage)
                
                elif vAttacks == solarbeam:
                    damage = enemy-solarbeam
                    print 'Venasaur used SolarBeam, %s took %d damage' % (enemy)(damage)
                
                elif vAttacks == cut:
                    damage = enemy-cut
                    print 'Venasaur used Cut, %s took %d damage' % (enemy)(damage)
                
                else:
                    print "Please type the full attack"            
        if pokemon1 == Absol:
            AbsolAttacks = raw_input.lower(('Bite HyperBeam Tackle Slash:  '))
            bite = random.randint(20,30)
            hyperbeam = random.randint(25,35)
            tackle = random.randint(10,15)
            slash = random.randint(15,20)
            if AbsolAttacks == bite:
                damage= enemy - bite
                print 'Absol used Bite, %s took %d damage' % (enemy)(damage)
            else:
                if AbsolAttacks == hyperbeam:
                    damage= enemy-hyperbeam
                    print 'Absol used HyperBeam, %s took %d damage' % (enemy)(damage)
                
                elif AbsolAttacks == tackle:
                    damage = enemy-tackle
                    print 'Absol used Tackle, %s took %d damage' % (enemy)(damage)
                
                elif AbsolAttacks == slash:
                    damage = enemy-slash
                    print 'Absol used Slash, %s took %d damage' % (enemy)(damage)
                
                else:
                    print "Please type the full attack"            
        if pokemon1 == Pikachu:
            PikachuAttack = raw_input.lower(('Slam Thunder Thunderbolt Tackle: '))
            slam = random.randint(10,20)
            thunder = random.randint(25,30)
            thunderbolt = random.randint(15,20)
            tackle = random.randint(10,15)
            if PikachuAttack == slam:
                damage= enemy - slam
                print 'Pikachu used Slam, %s took %d damage' % (enemy)(damage)
            else:
                if PikachuAttack == thunder:
                    damage= enemy-thunder
                    print 'Pikachu used Thunder, %s took %d damage' % (enemy)(damage)
                
                elif PikachuAttack == thunderbolt:
                    damage = enemy-thunderbolt
                    print 'Pikachu used Thunderbolt, %s took %d damage' % (enemy)(damage)
                
                elif PikachuAttack == tackle:
                    damage = enemy-tackle
                    print 'Pikachu used Tackle, %s took %d damage' % (enemy)(damage)
                
                else:
                    print "Please type the full attack"            
    
    if enemy == Charizard:
        enemyAttacks == random.choice([Flamethrower, Ember, Firekick, Flame Tempest])
        Flamethrower = random.randint(20,30)
        Ember = random.randint(10,15)
        Firekick = random.randint(15,20)
        Flametempest = random.randint(20,25)
        if enemyAttacks == Flamethrower:
            damage= pokemon1 - Flamethrower
            print 'Charizard used Flamethrower, %s took %d damage' % (pokemon1)(damage)
        else:
            if enemyAttacks == Ember:
                damage= pokemon1-Ember
                print 'Charizard used Ember, %s took %d damage' % (pokemon1)(damage)
               
            elif enemyAttacks == Firekick:
                damage = pokemon1-Firekick
                print 'Charizard used Firekick, %s took %d damage' % (pokemon1)(damage)
               
            elif enemyAttacks == flametempest:
                damage = pokemon1-flametempest
                print 'Charizard used Flametempest, %s took %d damage' % (pokemon1)(damage)
    
    else:
        if enemy == Blastoise:
            enemyAttacks = random.choice([watercanon, squirt, tackle, hydropump])
            watercanon = random.randint(20,25)
            squirt= random.randint(15,20)
            tackle = random.randint(15,20)
            hydropump = random.randint(25,35)
            if enemyAttacks == watercanon:
                damage= pokemon1 - watercanon
                print 'Blastoise used Watercanon, %s took %d damage' % (pokemon1)(damage)
            else:
                if enemyAttacks == squirt:
                    damage= pokemon1-squirt
                    print 'Blastoise used Squirt, %s took %d damage' % (pokemon1)(damage)
                
                elif enemyAttacks == tackle:
                    damage = pokemon1-tackle
                    print 'Blastoise used Tackle, %s took %d damage' % (pokemon1)(damage)
                
                elif enemyAttacks == hydropump:
                    damage = pokemon1-hydropump
                    print 'Blastoise used hydropump, %s took %d damage' % (pokemon1)(damage)
           
        if enemy == Venasaur:
            enemyAttacks = random.choice.lower([vinewhip, razorleaf, solarbeam, cut])
            vinewhip= random.randint(10,15)
            razorleaf = random.randint(15,25)
            solarbeam = random.randint(20,30)
            cut = random.randint(10,15)
            if enemyAttacks == vinewhip:
                damage= pokemon1 - vinewhip
                print 'Venasaur used VineWhip, %s took %d damage' % (pokemon1)(damage)
            else:
                if enemyAttacks == razorleaf:
                    damage= pokemon1-razorleaf
                    print 'Venasaur used RazorLeaf, %s took %d damage' % (pokemon1)(damage)
                
                elif enemyAttacks == solarbeam:
                    damage = pokemon1-solarbeam
                    print 'Venasaur used SolarBeam, %s took %d damage' % (pokemon1)(damage)
                
                elif enemyAttacks == cut:
                    damage = pokemon1-cut
                    print 'Venasaur used Cut, %s took %d damage' % (pokemon1)(damage)
            
        if enemy == Absol:
            enemyAttacks = random.choice([bite, hyperbeam, tackle, slash])
            bite = random.randint(20,30)
            hyperbeam = random.randint(25,35)
            tackle = random.randint(10,15)
            slash = random.randint(15,20)
            if enemyAttacks == bite:
                damage= pokemon1 - bite
                print 'Absol used Bite, %s took %d damage' % (pokemon1)(damage)
            else:
                if enemyAttacks == hyperbeam:
                    damage= pokemon1-hyperbeam
                    print 'Absol used HyperBeam, %s took %d damage' % (pokemon1)(damage)
                
                elif enemyAttacks == tackle:
                    damage = pokemon1-tackle
                    print 'Absol used Tackle, %s took %d damage' % (pokemon1)(damage)
                
                elif enemyAttacks == slash:
                    damage = pokemon1-slash
                    print 'Absol used Slash, %s took %d damage' % (pokemon1)(damage)
                        
        if enemy == Pikachu:
            enemyAttacks = random.choice([slam, thunder, thunderbolt, tackle])
            slam = random.randint(10,20)
            thunder = random.randint(25,30)
            thunderbolt = random.randint(15,20)
            tackle = random.randint(10,15)
            if enemyAttacks == slam:
                damage= pokemon1 - slam
                print 'Pikachu used Slam, %s took %d damage' % (pokemon1)(damage)
            else:
                if enemyAttacks == thunder:
                    damage= pokemon1-thunder
                    print 'Pikachu used Thunder, %s took %d damage' % (pokemon1)(damage)
                
                elif enemyAttacks == thunderbolt:
                    damage = pokemon1-thunderbolt
                    print 'Pikachu used Thunderbolt, %s took %d damage' % (pokemon1)(damage)
                
                elif enemyAttacks == tackle:
                    damage = pokemon1-tackle
                    print 'Pikachu used Tackle, %s took %d damage' % (pokemon1)(damage)





    #win conditions
    if pokemon1 <= 0:
        print "Oh no! %s fainted!" % (pokemon1)
        break
    if enemy <= 0:
        print "%s fainted! %s wins!" % (enemy)(pokemon1)
        break
    print "%s's health is " + str(pokemon1) %(pokemon1)
    print "%s's health is " + str(enemy) %(enemy)
    