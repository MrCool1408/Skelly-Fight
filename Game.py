import random
print("After traversing a dungeon in search of a mystical spell book, you encounter a furious skeleton, filled with hatred from his untimely demise. He makes mouth movements akin to talking, but, due to the lack of... uh... really anything, he just lets out a terible rattling sound")
print("THE FIGHT BEGINS! What will you do? you:[HP-100 ARMOR-20] Skelly:[HP-140]  1.[GREATWSORD SLASH -64hp, high chance to dismember] 2.[CROSSBOW BOLT -20hp, moderate chance to penetrate armor] 3.[DAGGER SLICE -15hp, Slight chance to cause bleed]")
class you:
    HP=100
    ARMOR=20
class Skelly:
    HP=140
    ARMOR=20
    EFFECT="none"
    DP=15
def greatsword_slash():
        chance=random.randint(1,100)
        if chance<=50:
            print("you weild your greatsword and violently slash your foe")
            damage=100
            print("one of the enemy's limbs is lobbed of, causing massive damage")
            if Skelly.ARMOR>1:
                damage=damage-15
                print("The enemy's armor deflects some of the force")
            Skelly.HP=Skelly.HP-damage
            print("Skelly:[HP-",Skelly.HP,"]")
        elif chance>50:
            damage=64
            print("you weild your greatsword and violently slash your foe")
            if Skelly.ARMOR>1:
                damage=damage-15
                print("The enemy's armor deflects some of the force")
            Skelly.HP=Skelly.HP-damage
            print("Skelly:[HP-",Skelly.HP,"ARMOR-",Skelly.ARMOR,"]")
def crossbow_bolt():
    damage=20
    penetrate=20
    #moderate chance to pen armor (30/100)
    chance=random.randint(1,100)
    if chance<=30:
        print("You ready your 40 lb crossbow and release a bolt")
        print("The 1/2 lb bolt penetrates the enemy's armor like butter. -20 armor")
        print("You start winding up the behemoth of a crossbow, this leaves you vulnerable. +5 damage")
        Skelly.DP=Skelly.DP+5
        Skelly.ARMOR=Skelly.ARMOR-penetrate
        Skelly.HP=Skelly.HP-damage
        print("Skelly:[HP-",Skelly.HP,"ARMOR-",Skelly.ARMOR,"]")       
    elif chance>30:
        print("You ready your 40 lb crossbow and release a bolt.")
        if Skelly.ARMOR>1:
            damage=damage-5
            print("The enemy's armor deflects the bolt")
        print("You start winding up the behemoth of a crossbow, this leaves you vulnerable. +5 damage")
        Skelly.DP=Skelly.DP+5
        Skelly.HP=Skelly.HP-damage
        print("Skelly:[HP-",Skelly.HP,"ARMOR-",Skelly.ARMOR,"]")
def dagger_slice():
    damage=15
    #slight chance to cause bleed. (25/100)
    chance=random.randint(1,100)
    if chance<=25:
        print("You quickly unsheath your dagger and slice your foe.")
        print("You strike an artery and cause severe bleeding. -10 lingering damage")
        Skelly.EFFECT="bleed"
        if Skelly.ARMOR>1:
            print("the enemy's armor deflects some of the damage")
            damage=damage-5
            Skelly.HP=Skelly.HP-damage
            print("Skelly:[HP-",Skelly.HP,"ARMOR-",Skelly.ARMOR,"]")
        elif chance>25:
            print("You quickly unsheath your dagger and slice your foe.")
            if Skelly.ARMOR>1:
                print("the enemy's armor deflects some of the damage")
                damage=damage-5
            Skelly.HP=Skelly.HP-damage
            print("Skelly:[HP-",Skelly.HP,"ARMOR-",Skelly.ARMOR,"]")
def turn_end():
    print("the skeleton slashes at you with its hands")
    if you.ARMOR>1:
        print("your armor deflects some of the damage")
        Skelly.DP=Skelly.DP-10
    you.HP=you.HP-Skelly.DP
    if Skelly.EFFECT=="bleed":
        print("the blood loss sets in and the enemy is damaged")
        Skelly.HP=Skelly.HP-10
    print("you:[HP-",you.HP,"ARMOR-",you.ARMOR,"] Skelly:[HP-",Skelly.HP,"ARMOR-",Skelly.ARMOR,"]")
    Skelly.DP=15
while Skelly.HP>0:
    keypress=input()
    if keypress=="1":
        greatsword_slash()
    elif keypress=="2":
        crossbow_bolt()
    elif keypress=="3":
        dagger_slice()
    turn_end()
    if you.HP<0:
        print("GAME OVER")
        exit()
print("Congradulations! You won!")