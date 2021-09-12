 
import sys
import random
import Background


def create(color,X,Y,lifes,score,ult):
    """Creation du heros"""
    s=dict()
    s["color"]=color
    s["x"]=X
    s["y"]=Y
    s["lifes"]=lifes 
    s["score"]=score
    s["ult"]=ult
    return s

#getters et setters
def getColor(s):
  return s['color']
def getX(s):
  return s['x']
def getY(s):
  return s['y']
def setColor(s,color):
  s['color']=color
  return s['color']
def setX(s,X):
  s['x']=X
  return s['x']
def setY(s,Y):
  s['y']=Y
  return s['y']
def getLifes(s):
	return s["lifes"] 
def setLifes(s,lifes):
	s["lifes"]= lifes 
	return s["lifes"]
def getScore(s):
	return s["score"] 
def setScore(s,score):
	s["score"]= score 
	return s["score"]
def getUlt(s):
    return s["ult"] 
def setUlt(s,ult):
    s["ult"]= ult 
    return s["ult"]
	
def show(s) :
    # couleur fond noire
    sys.stdout.write("\033[40m")

    # style heros
    c=s["color"]
    txt="\033[3"+str(c%7+1)+";7m"
    sys.stdout.write(txt)

    # affichage du heros : le caractere affiche est ^
    # on se place a la position du heros dans le terminal
    x=str(int(s["x"]))
    y=str(int(s["y"]))
    txt="\033["+y+";"+x+"H"
    sys.stdout.write(txt)

    cara = "^"
    sys.stdout.write(cara)

    txt="\033[0m"
    sys.stdout.write(txt)
    
def showVies(s) :
    # couleur fond noire
    sys.stdout.write("\033[40m")

    # style heros
    c=s["color"]
    txt="\033[3"+str(c%7+1)+";7m"
    sys.stdout.write(txt)

    x=str(int(40))
    y=str(int(22))
    txt="\033["+y+";"+x+"H"
    sys.stdout.write(txt)

    cara = str(s["lifes"])
    sys.stdout.write(cara)

    txt="\033[0m"
    sys.stdout.write(txt)
    
def showScore(s) :
    # couleur fond noire
    sys.stdout.write("\033[40m")

    # style heros
    c=s["color"]
    txt="\033[3"+str(c%7+1)+";7m"
    sys.stdout.write(txt)

    x=str(int(20))
    y=str(int(22))
    txt="\033["+y+";"+x+"H"
    sys.stdout.write(txt)

    cara = str(s["score"])
    sys.stdout.write(cara)

    txt="\033[0m"
    sys.stdout.write(txt)

def showUlt(s) :
    # couleur fond noire
    sys.stdout.write("\033[40m")

    # style heros
    c=s["color"]
    txt="\033[3"+str(c%7+1)+";7m"
    sys.stdout.write(txt)

    x=str(int(34))
    y=str(int(23))
    txt="\033["+y+";"+x+"H"
    sys.stdout.write(txt)

    cara = str(s["ult"])
    sys.stdout.write(cara)

    txt="\033[0m"
    sys.stdout.write(txt)

def move(s,x,y,bg):
  x= x+s['x']
  y= y+s['y']
  if Background.isSpace(bg,x,y):
    s['x']=x
    s['y']=y
        
