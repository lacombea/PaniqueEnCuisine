import sys

def create(filename):
    # creation du fond
    bg=dict()
    # ouverture fichier
    myfile = open(filename, "r")
    bg["str"]=myfile.read()
    myfile.close()
    bg["grid"]=bg['str'].splitlines()
    return bg

def isSpace(bg,x,y):
    if y>len(bg['grid']):
        return False
    if x>len(bg['grid'][0]):
        return False
    if bg['grid'][y-1][x-1]==' ':
        return True
    else:
        return False

def show(bg) :
    # goto
    sys.stdout.write("\033[1;1H")

    # couleur fond
    sys.stdout.write("\033[40m")

    # couleur white
    sys.stdout.write("\033[37m")

    # affiche
    sys.stdout.write(bg["str"])
