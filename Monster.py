
import sys
import random
import Background


def create(color,rangeX,rangeY,speedMin,speedMax,shapes='|'):
    o=dict()
    o["color"]=color
    o["x"]=random.randint(10,rangeX)
    o["y"]=random.randint(2,rangeY)
    o["speed"]=speedMin + random.random()*(speedMax-speedMin)
    o["shapes"]=shapes
    o["rotation"]=0
    return o

# getters et setters pour Y et color

def getX(o):
  return o['x']
def setX(o,x):
  o['x']=x
  return o['x']
def getY(o):
  return o['y']
def setY(o,y):
  o['y']=y
  return o['y']
def getcolor(o):
  return o['color']
def setcolor(o,color):
  o['color']=color
  return o['color']


def show(o) :
    # couleur fond noire
    sys.stdout.write("\033[40m")

    # couleur monstres
    c=o["color"]
    txt="\033[3"+str(c%7+1)+";7m"
    sys.stdout.write(txt)

    # affichage des monstres
    # on se place a la position du heros dans le terminal
    x=str(int(o["x"]))
    y=str(int(o["y"]))
    txt="\033["+y+";"+x+"H"
    sys.stdout.write(txt)

    # on affiche le heros
    cara = o["shapes"][int(o["rotation"])]
    sys.stdout.write(cara)

    txt="\033[0m"
    sys.stdout.write(txt)

def live(o,dt,bg):
    x = o['x']
    y = o['y'] + o['speed']*dt
    o['x']=x
    o['y']=y
    o['rotation'] += 2*int(o['speed'])*dt
    o['rotation'] %= len(o['shapes'])


def testCollision(o,x,y):
    x=int(x)
    y=int(y)
    if int(o['x'])==x:
      if int(o['y'])==y:
        return True
      else:
        return False
      

    
    
