import sys
import random
import Background
import Hero
import Monster


def create(color,rangeX,rangeY,speed,shapes='|'):
    t=dict()
    t["color"]=color
    t["x"]=rangeX
    t["y"]=rangeY
    t["speed"]=speed
    t["shapes"]=shapes
    return t

# getters et setters pour Y et color

def getX(t):
    return t['x']
def setX(t,x):
    t['x']=x
    return t['x']
def getY(t):
  return t['y']
def setY(t,y):
  t['y']=y
  return t['y']
def getcolor(t):
  return t['color']
def setcolor(t,color):
  t['color']=color
  return t['color']


def show(t) :
    # couleur fond noire
    sys.stdout.write("\033[40m")

    # couleur tir
    c=t["color"]
    txt="\033[3"+str(c%7+1)+";7m"
    sys.stdout.write(txt)

    # affichage du tir
    # on se place a la position du heros dans le terminal
    x=str(int(t["x"]))
    y=str(int(t["y"]))
    txt="\033["+y+";"+x+"H"
    sys.stdout.write(txt)

    # on affiche le heros
    cara = t["shapes"]
    sys.stdout.write(cara)
    txt="\033[0m"
    sys.stdout.write(txt)

def live(t,dt,bg):
    x = t['x']
    y = t['y'] - t['speed']*dt
    t['x']=x
    t['y']=y


