from numpy import random


class Monster:
    def __init__(self, race, damage, hp):
        self.race = race
        self.damage = damage
        self.hp = hp

    def getRace(self):
        return self.race

    def getDamage(self):
        return self.damage

    def getHP(self):
        return self.hp

    def __str__(self):
        return f"{self.race}({self.damage},{self.hp})"  #when printing you see values rather than memory location



def ranNum(mult):
    damage = 0
    i=0
    while i<mult:
        damage = damage + random.randint(10)
        i=i+1
    return damage


m1 = Monster("skeleton", 1, 5)
m2 = Monster("zombie",2, 10)
m3 = Monster("minotaur",3, 18)


def monsterAttack(attackingObj,defendingObj):  #recursive
    
    mult = attackingObj.getDamage()
    damage = ranNum(mult)
    
    life = defendingObj.getHP() - damage

    if life < 1:
        life = 0
    defendingObj.hp = life
    
    
    print("The "+attackingObj.getRace()+" attacks the "+defendingObj.getRace()+" inflicting "+str(damage)+" damage!")
    print("The "+defendingObj.getRace()+" has "+str(defendingObj.getHP())+" life points remaining.")

    if life == 0:
        print("The "+defendingObj.getRace()+" is dead.\n")
        return
    else:
        tempAttacker = defendingObj
        defendingObj = attackingObj
        attackingObj = tempAttacker
        monsterAttack(attackingObj,defendingObj)

print(m1,m2,m3,"\n")

attackingObj = m2
defendingObj = m3
monsterAttack(attackingObj,defendingObj)



attackingObj = m1
if (m2.getHP()==0):
    defendingObj = m3
else:
    defendingObj = m2 
monsterAttack(attackingObj,defendingObj)

winner = ""
if (m1.getHP()!=0):
    winner = "SKELETON"
elif (m2.getHP()!=0):
    winner = "ZOMBIE"
else:
    winner = "MINOTAUR"

print("The winner is "+winner+"!!!\n")    
print(m1,m2,m3) 
