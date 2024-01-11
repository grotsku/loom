import pickle
from random import choice
from subprocess import call

mixes = []

class Mix:
    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url

    def printMix(self):
        print(self.name, self.url)

def addMix():
    name = input('name of mix: ')
    url = input('give the url: ')
    newMix = Mix(name, url)
    mixes.append(newMix)

def saveList(mixes):
    with open('loomSave.obj', 'wb') as savedMixes:
        pickle.dump(mixes, savedMixes)

def loadList():
    try:
        with open('loomSave.obj', 'rb') as savedMixes:
            return pickle.load(savedMixes)
    except:
        return []

def printMixes():
    for mix in mixes:
        mix.printMix()

def chooseRandom(mixes):
    if not mixes:
        print('no mixes available :( add some!')
        return None
    return choice(mixes).url

def playMix(url):
    call(['mpv', '--no-video', url])

# main program

mixes = loadList()
url = chooseRandom(mixes)
printMixes()

print('L O O M')
while True:
    toiminto = input('(a)dd, (p)lay or (e)xit: ') 
    if toiminto == 'a':
        addMix()
        saveList(mixes)
    elif toiminto == 'p':
        playMix(url)
    else:
        break
