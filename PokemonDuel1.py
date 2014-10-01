import random

#test pokemon like game, will add gui later
Absol = 100
Pikachu = 100

#the duel
for turn in range(1000):
    #setting up the parameters for the attacks
    AbsolAttacks = raw_input('Bite HyperBeam Tackle Use Potion:  ')
    AbsolUsePotion = Absol + 20
    Slam =  random.randint(10,20)
    Thunder =  random.randint(30,45)
    Thunderbolt =  random.randint(25,30)
    PikachuUsePotion = +20
    #beginning absol's attack
    if AbsolAttacks.startswith('b'):
        damage = random.randint(20,35)
        Pikachu -= damage
        print 'Absol used Bite, Pikachu took %d damage' % (damage)
    else:
        if AbsolAttacks.startswith('h'):
            damage = random.randint(30,60)
            Pikachu -= damage
            print 'Absol used Hyper Beam, Pikachu took %d damage' % (damage)
        elif AbsolAttacks.startswith('t'):
            damage = random.randint(10,15)
            Pikachu -= damage
            print 'Absol used Tackle, Pikachu took %d damage' % (damage)
        elif AbsolAttacks.startswith('u'):
            Absol += 20
            if Absol >= 100:
                Absol = 100
            print 'Absol used Potion and recovered 20 health'
        else:
            print 'Try again, type out the whole word or the first letter (b) for bite'
#beginning Pikachu's attack
    if Pikachu >= 30:
        PikachuAttack = random.choice([Slam, Thunder, Thunderbolt]) # (-15,-25,-20)
        Absol = Absol - PikachuAttack
        if PikachuAttack == Slam:
            print "Pikachu used Slam, Absol took %d damage" % (PikachuAttack)
        else: 
            if PikachuAttack == Thunder:
                print "Pikachu used Thunder,Absol took %d damage" % (PikachuAttack)
            elif PikachuAttack == Thunderbolt:
                print "Pikachu used Thunderbolt, Absol took %d damage" % (PikachuAttack)
    else:
        if Pikachu <=29:
            pikachuAttack2 = random.choice([Slam, PikachuUsePotion])
            if pikachuAttack2 == Slam:
                Absol = Absol - pikachuAttack2
                print "Pikachu used Slam, Absol took %d damage" % (pikachuAttack2)
            else: 
                if pikachuAttack2 == PikachuUsePotion:
                    Pikachu += 20
                    print "Pikachu used Potion and restored 20 health!"
    #win conditions
    if Absol <= 0:
        print "Oh no! Absol fainted!"
        break
    if Pikachu <= 0:
        print "Pikachu fainted! Absol wins!"
        break
    print "Absol's health is " + str(Absol)
    print "Pikachu's health is " + str(Pikachu)
    