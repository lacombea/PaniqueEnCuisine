# -*- coding: utf-8 -*-

# modules externes
import sys
import os
import time
import select
import tty
import termios
import random
import time

# mes modules
import Background
import Hero
import Monster
import Tir
import Menu
# interaction clavier
old_settings = termios.tcgetattr(sys.stdin)

# donnees du jeu
hero = None
monsters = []
tir = []
background = None
timeStep=None
i=0
u=0
j=0
k=0
l=0
m=0
v=1

def init():
	global hero, monsters, tir, background, timeStep
    
	timeStep=0.02
	
    #  ici on cree hero et background en appelant create
#Menu.Menu()
hero=Hero.create(6,25,17,3,0,'X')

background = Background.create("image.txt")

tty.setcbreak(sys.stdin.fileno())
    # interaction clavier
 
    
 
def live(dt):
    global hero, monsters, tir, background,j,k,l,v,m

    # les monstresvivent leurs vies
    for f in monsters:
        Monster.live(f, dt, background)

    for p in tir:
    	Tir.live(p, dt, background)
        
    x=Hero.getX(hero)
    y=Hero.getY(hero)
    xm=Monster.getX(f)
    ym=Monster.getY(f)
	
    for f in monsters :
    	if Monster.testCollision(f,x,y):
    		hero["lifes"]= hero["lifes"] - 1
    		monsters.remove(f)

    if hero["lifes"] == 0 :
    	sys.stdout.write("\033[40m")
    	c=6
    	txt="\033[3"+str(c%7+1)+";7m"
    	sys.stdout.write(txt)

    	x=str(int(40))
    	y=str(int(22))
    	txt="\033["+y+";"+x+"H"
    	sys.stdout.write(txt)

    	cara = str(0)
    	sys.stdout.write(cara)

    	txt="\033[0m"
    	sys.stdout.write(txt)

    	sys.stdout.write("\033[10;18H")
    	sys.stdout.write("vous avez perdu !")
    	sys.stdout.write("\033[0m")
    	print(" ")
    	print("      Les monstres ont envahi votre cuisine")
    	print(" ")
    	quitGame()
						
    for f in monsters :
    	xm = int(Monster.getX(f))
    	ym = int(Monster.getY(f))
    	for p in tir:
    		y = int(Tir.getY(p))
    		x = int(Tir.getX(p))
    		if y <= ym and x == xm:
    			monsters.remove(f)
    			tir.remove(p)
    			hero["score"] = hero["score"] + 5*v
    			if hero["score"] >= 100:
    				hero["ult"] = 'V'
    			if len(monsters) == 0:
    				if j<15:
    					while j<15 :
    						monsters.append(Monster.create(color=1, rangeX=41, rangeY=5, speedMin=1, speedMax=1, shapes='|/-\\'))
    						j = j + 1
    						v=v+1
    				elif k<20:
    					while k<20 :
    						monsters.append(Monster.create(color=2, rangeX=41, rangeY=5, speedMin=1, speedMax=1.25, shapes='|/-\\'))
    						k = k + 1
    						v=v+1
    				elif l<25:
    					while l<25:
    						monsters.append(Monster.create(color=4, rangeX=41, rangeY=5, speedMin=1.25, speedMax=1.5, shapes='|/-\\'))
    						l = l + 1
    						v=v+1
    				elif m<20:
    					while m<20 :
    						monsters.append(Monster.create(color=0, rangeX=41, rangeY=5, speedMin=1.25, speedMax=1.5, shapes='|/-\\'))
    						monsters.append(Monster.create(color=2, rangeX=41, rangeY=5, speedMin=1.25, speedMax=1.5, shapes='|/-\\'))
    						m = m + 1
    						v=v+1
    				else :
    					sys.stdout.write("\033[1;1H")
    					sys.stdout.write("\033[2J")
    					sys.stdout.write("\033[10;18H")
    					sys.stdout.write("vous avez gagné !")
    					sys.stdout.write("\033[0m")
    					print(" ")
    					print("    Vous avez chassé les monstres de votre cuisine")
    					print("        Votre score final est de :", int(hero["score"]), "points")
    					print(" ")
    					quitGame()	
											
				
    # est-ce que les monstres sortent de lecran ?
    for f in monsters:
         y = int(Monster.getY(f))
         if y > 20 :
         	sys.stdout.write("\033[10;18H")
         	sys.stdout.write("vous avez perdu !")
         	sys.stdout.write("\033[0m")
         	print(" ")
         	print("      Les monstres ont envahi votre cuisine")
         	print(" ")
         	quitGame()
        
    for p in tir:
    	y = int(Tir.getY(p))
    	if y<0:
    		tir.remove(p)
	
        
    #on cree un nombre prédéfini de monstres



while i<10:
	monsters.append(Monster.create(color=0, rangeX=41, rangeY=5, speedMin=1, speedMax=1, shapes='|/-\\'))
	i = i + 1
	
def interact():
    """gestion des evenements clavier"""
    global hero, background, tir

    x=Hero.getX(hero)
    y=Hero.getY(hero)
    
    if isData():
        c = sys.stdin.read(1)
        u = 0
        if c == '\x1b':         
        	quitGame()
        # si une touche est appuyee, on bouge le hero avec q,s,z et d: gauche, haut, bas et droite respectivement, la trouche r sert pour le tir
        elif c == 'p':
            if hero["score"]>=100:
                tir.append(Tir.create(color=5, rangeX=random.randint(9,11), rangeY=y-1, speed=1, shapes='|'))
                tir.append(Tir.create(color=5, rangeX=random.randint(12,15), rangeY=y-1, speed=1, shapes='|'))
                tir.append(Tir.create(color=5, rangeX=random.randint(16,19), rangeY=y-1, speed=1, shapes='|'))
                tir.append(Tir.create(color=5, rangeX=random.randint(20,22), rangeY=y-1, speed=1, shapes='|'))
                tir.append(Tir.create(color=5, rangeX=random.randint(23,25), rangeY=y-1, speed=1, shapes='|'))
                tir.append(Tir.create(color=5, rangeX=random.randint(26,29), rangeY=y-1, speed=1, shapes='|'))
                tir.append(Tir.create(color=5, rangeX=random.randint(30,32), rangeY=y-1, speed=1, shapes='|'))
                tir.append(Tir.create(color=5, rangeX=random.randint(33,35), rangeY=y-1, speed=1, shapes='|'))
                tir.append(Tir.create(color=5, rangeX=random.randint(36,38), rangeY=y-1, speed=1, shapes='|'))
                tir.append(Tir.create(color=5, rangeX=random.randint(39,41), rangeY=y-1, speed=1, shapes='|'))
                hero["score"] = hero["score"]-100
                hero["ult"] = 'X'    

        elif c == 'q':
        	Hero.move(hero,-1,0,background)
        elif c == 'd':
        	Hero.move(hero,1,0,background)
        elif c == 'z':
        	Hero.move(hero,0,-1,background)
        elif c == 's':
        	Hero.move(hero,0,1,background)
        elif c == 'r':
        	tir.append(Tir.create(color=3, rangeX=x, rangeY=y-1, speed=2, shapes='|'))  
       
        while isData():
            sys.stdin.read(1)

def showVague():
	
	
    # couleur fond noire
    sys.stdout.write("\033[40m")
	
    # style heros
    c=6
    txt="\033[3"+str(c%7+1)+";7m"
    sys.stdout.write(txt)

    x=str(int(20))
    y=str(int(24))
    txt="\033["+y+";"+x+"H"
    sys.stdout.write(txt)
    if v<5:
    	cara = str(v)
    else : 
    	cara = "finalle"
    sys.stdout.write(cara)

    txt="\033[0m"
    sys.stdout.write(txt)    

def isData():
    """recuperation evenement clavier"""
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])


def show():
    """rafraichissement de l'affichage"""
    global background, monsters, hero, tir

    # effacer la console
    sys.stdout.write("\033[1;1H")
    sys.stdout.write("\033[2J")

    # affichage des elements
    Background.show(background)
    for f in monsters:
        Monster.show(f)

    Hero.show(hero)
    Hero.showVies(hero)
    Hero.showScore(hero)
    Hero.showUlt(hero)
    showVague()
    
    
    for p in tir:
    	Tir.show(p)

    # restauration couleur
    sys.stdout.write("\033[37m")
    sys.stdout.write("\033[40m")

    # deplacement curseur
    sys.stdout.write("\033[0;0H\n")
    

def run():
    global timeStep

    # Boucle de simulation
    counter = 0
    while 1:
        counter += 1

        # les interactions n'ont lieu qu'une fois sur 2
        if(counter == 2):
            interact()

        live(timeStep)

        # l'affichage n'as lieu qu'une fois sur 2
        if(counter == 2):
            show()
            counter = 0

        time.sleep(timeStep)

def quitGame():

    # restauration parametres terminal
    global old_settings

    # couleur white
    sys.stdout.write("\033[37m")
    sys.stdout.write("\033[40m")

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    sys.exit()

######################################

init()
#try:
run()
#finally:
quitGame()
