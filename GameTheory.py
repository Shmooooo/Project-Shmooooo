# ================================================
# ++++++++ MMOS solved by game theory! +++++++++++
# ================================================

# ============== Imports =========================

from numpy import array
from random import choice
from itertools import combinations, product
import matplotlib.pyplot as plt

# ============== Initialization ===================

# dictionary to hold all weapon and armour stats indexed by colour.
# In order: damage, reduced speed, absorb, dodge.
s = {"g":array([ 5.0, 18.0, 0.0, 0.24]),\
     "y":array([15.0,  5.0, 2.0, 0.00]),\
     "r":array([ 8.0, 10.0, 0.8, 0.15]),\
     "b":array([10.0,  8.0, 1.2, 0.10])}

# player class to hold each player's stats and records
class player:
    """ Instances of this class should possess semi-persistent attributes.
        their distribution reflects armor/weapon popularity.

        w and a are any of g, y, r and b, standing for colour. """
    def __init__(self, w, a, n):
        self.w = w
        self.a = a
        self.wa = w + a
        
        self.damage = s[w][0]
        self.speed = s[w][1]
        self.absorb = s[a][2]
        self.dodge = s[a][3]
        
        self.id = n
        self.wins = 0
        self.losses = 0
        self.lostTo = []

# clear axes for plotting, clear old limit

plt.cla()
plt.clf()

#get input, initialize other globals
limitRounds = int(raw_input("Stop at given number of rounds? 0 for no, 1 for yes:"))
if limitRounds == True:
    roundLimit = int(raw_input("Maximum number of rounds to fight for:"))
else:
    roundLimit = 0
playerCount = int(raw_input("Number of players participating (anything over 300 will be slow, calculation time is probably O(2^n)):"))
swapThreshold = int(raw_input("How many more defeats than wins for a player to swap out gear:"))
memory = int(raw_input("Do players consider their entire win/loss record before swapping out (0 for no, 1 for yes):"))

j = 1


# list of player instances with random weapons and armour.
players = []
for i in range(playerCount):
    x = "p" + str(i)
    x = player(choice("gyrb"),choice("gyrb"), i)
    players.append(x)

# ============= Relevant Functions ===============

# single round of combat function
def combat(p1, p2):
    """ function plays out a single round of combat between two players """
    p1hp = 1000
    p2hp = 1000
    while p1hp > 0 and p2hp > 0:
        p2hp = p2hp - p1.speed*((p1.damage - p2.absorb)*(1 - p2.dodge))
        p1hp = p1hp - p2.speed*((p2.damage - p1.absorb)*(1 - p1.dodge))  
    if p2hp < p1hp:
        p2.lostTo.append(p1.id)
        p1.wins += 1
        p2.losses += 1
        return p1.id
    else:
        p1.lostTo.append(p2.id)
        p2.wins += 1
        p1.losses += 1
        return p2.id

# after-combat gear change function
def swapout():
    # list of losers
    global losers
    losers = []
    for p in players:
        if p.losses - p.wins > swapThreshold:
            losers.append(p)

    #strings containing w/a colours of players the losers lost to
    for l in losers:
        winWe = ""
        winAr = ""
        for winnerId in l.lostTo:
            winWe += players[winnerId].w
            winAr += players[winnerId].a
        newWe = choice(winWe)
        newAr = choice(winAr)

        # replace stats and gear
        losses = players[l.id].losses
        wins = players[l.id].wins
        players[l.id] = player(newWe, newAr, l.id)
        if memory == True:
            players[l.id].losses = losses
            players[l.id].wins = wins

# function to weapon/armour distribution after combat, respecting combinations
def itemplot(i):
    plotTable = [[a+b, 0] for a, b in product("gyrb", repeat = 2)]
    for p in players:
        for n, li in enumerate(plotTable):
            if p.wa == li[0]:
                plotTable[n][1] += 1
    for li in plotTable:
        plt.plot([i], li[1], li[0][1] + "D", [i + 0.15], li[1], li[0][0] + ">")

# ================== Combat ======================

while True:
    if limitRounds == True:
        print "Fighting for", roundLimit, "rounds:\n"
    else:
        print "Fighting until total domination!\n"
    itemplot(j - 1)
    for p1, p2 in combinations(players, 2):
        combat(p1, p2)
    swapout()

    # reset round stats
    for p in players:
        if memory != True:
            p.wins = 0
            p.losses = 0
        p.lostTo = []
    print "Done round", str(j-1) + "..."

    #break conditions
    if j > roundLimit and limitRounds == True:
        "Round limit reached. Ending.\n"
        break
    totalWin = [bool(players[0].wa == p.wa) for p in players]
    if all(totalWin):
        print "Total domination achieved!\n"
        break

    j += 1

# finishing up
itemplot(j)
plt.savefig("BATTLE", dpi = 200)
print "DONE! Plot saved to BATTLE.png"

#=================================================
#=================================================
    
    

    
