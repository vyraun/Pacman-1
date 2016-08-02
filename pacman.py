#-- PACMAN GAME --
# Ayush Mishra
# mishraiiit

#The game is implemented using four main classes.
#The Game class, The person class, The Pacman class and the Ghost class.
#The Game class contains methods relevant to the game,
#the board is also there in the game class.
#The main function contains the logic of the program using
#self-explanatory variable names and function names.

import random

class Person():
    def __init__(self, coordinateX, coordinateY):
        self.x = coordinateX
        self.y = coordinateY

    def canPersonMoveHere(self, coordinateX, coordinateY, instanceOfGame):
        if coordinateX > 34 or coordinateX < 0 or coordinateY > 14 or \
	coordinateY < 0:
            return False
        if 'X' in instanceOfGame.array[coordinateY][coordinateX]:
            return False
        return True

class Pacman(Person):
    def __init__(self, coordinateX, coordinateY):
        Person.__init__(self, coordinateX, coordinateY)
        self.score = 0

    def checkGhost(self, instanceOfGame):
        #Here [ instanceOfGame ] should be of Game class.
        if 'G' in instanceOfGame.array[self.y][self.x]:
            instanceOfGame.gameOver = True
            return True

    def checkCoin(self, instanceOfGame):
        return 'C' in instanceOfGame.array[self.y][self.x]

    def collectCoin(self, instanceOfGame):
        self.score = self.score + 1
        #Increment the score
        instanceOfGame.array[self.y][self.x].remove('C')
        #Remove the coin from that place as it's taken by PacMan.

    def printScore(self):
        print "Score : " + str(self.score)

    def moveAccordingToInput(self, char, instanceOfGame):
        if char == 'q': exit()
        elif char == 'w' or char == 'W':
            if self.canPersonMoveHere(self.x, self.y-1, instanceOfGame):
                instanceOfGame.array[self.y][self.x].remove('P')
                instanceOfGame.array[self.y-1][self.x].append('P')
                self.x = self.x
                self.y = self.y-1
        elif char == 'a' or char == 'A':
            if self.canPersonMoveHere(self.x-1, self.y, instanceOfGame):
                instanceOfGame.array[self.y][self.x].remove('P')
                instanceOfGame.array[self.y][self.x-1].append('P')
                self.x = self.x-1
                self.y = self.y

        elif char == 's' or char == 'S':
            if self.canPersonMoveHere(self.x, self.y+1, instanceOfGame):
                instanceOfGame.array[self.y][self.x].remove('P')
                instanceOfGame.array[self.y+1][self.x].append('P')
                self.x = self.x
                self.y = self.y+1

        elif char == 'd' or char == 'D':
            if self.canPersonMoveHere(self.x+1, self.y, instanceOfGame):
                instanceOfGame.array[self.y][self.x].remove('P')
                instanceOfGame.array[self.y][self.x+1].append('P')
                self.x = self.x+1
                self.y = self.y

class Ghost(Person):
    def __init__(self, instanceOfGame):
        coordinateX = random.randint(0, 34)
        coordinateY = random.randint(0, 14)
        while len(instanceOfGame.array[coordinateY][coordinateX]) != 1:
            coordinateX = random.randint(0, 34)
            coordinateY = random.randint(0, 14)
        Person.__init__(self, coordinateX, coordinateY)
        instanceOfGame.array[coordinateY][coordinateX].append('G')

    def randomMoveGhost(self, instanceOfGame):
        num = random.randint(1, 4)
        if num is 1:
            if self.canPersonMoveHere(self.x+1, self.y, instanceOfGame):
                instanceOfGame.array[self.y][self.x].remove('G')
                instanceOfGame.array[self.y][self.x+1].append('G')
                self.x = self.x+1
                self.y = self.y
            else:
                num = 2

        if num is 2:
            if self.canPersonMoveHere(self.x-1, self.y, instanceOfGame):
                instanceOfGame.array[self.y][self.x].remove('G')
                instanceOfGame.array[self.y][self.x-1].append('G')
                self.x = self.x-1
                self.y = self.y
            else:
                num = 3

        if num is 3:
            if self.canPersonMoveHere(self.x, self.y+1, instanceOfGame):
                instanceOfGame.array[self.y][self.x].remove('G')
                instanceOfGame.array[self.y+1][self.x].append('G')
                self.x = self.x
                self.y = self.y+1
            else:
                num = 4

        if num is 4:
            if self.canPersonMoveHere(self.x, self.y-1, instanceOfGame):
                instanceOfGame.array[self.y][self.x].remove('G')
                instanceOfGame.array[self.y-1][self.x].append('G')
                self.x = self.x
                self.y = self.y-1

class Game():

    def __init__(self):
        self.gameOver = False
        self.createArray()
        self.buildWalls()
        self.generateCoins()

    def ghostPosition(self):
        for i in range(0, 35):
            for j in range(0, 15):
                if 'G' in self.array[j][i]:
                    return i, j

    def createArray(self):
        self.array = []

        for i in range(0, 15):
            self.array.append([])
            for j in range(0, 35):
                self.array[i].append(['.'])

    def printGame(self):
        for i in range(0, 15):
            toPrint = ''
            for j in range(0, 35):
                if 'G' in self.array[i][j]:
                    toPrint = toPrint + 'G' + ' '
                elif 'P' in self.array[i][j]:
                    toPrint = toPrint + 'P' + ' '
                elif 'C' in self.array[i][j]:
                    toPrint = toPrint + 'C' + ' '
                elif 'X' in self.array[i][j]:
                    toPrint = toPrint + 'X' + ' '
                else:
                    toPrint = toPrint + '.' + ' '
            print toPrint

    def buildWalls(self):
        for i in range(3, 20):
            if 'X' not in self.array[8][i]:
                self.array[8][i].append('X')

        for i in range(5, 14):
            if 'X' not in self.array[i][11]:
                self.array[i][11].append('X')

        for i in range(0, 10):
            if 'X' not in self.array[i][25]:
                self.array[i][25].append('X')


    def generateCoins(self):
        coinsToProduce = 20
        #Change the above value to generate more coins.
        while coinsToProduce:
            x = random.randint(1, 33)
            y = random.randint(1, 13)
            if 'C' not in self.array[y][x] and 'X' not in self.array[y][x]:
                self.array[y][x].append('C')
                coinsToProduce = coinsToProduce - 1;

    def getPacmanStartingCoordinates(self):
        x = random.randint(3, 33)
        y = random.randint(3, 12)
        while len(self.array[y][x]) != 1:
                x = random.randint(3, 33)
                y = random.randint(3, 12)
        self.array[y][x].append('P')
        return x, y

def main():
    ourGame = Game();
    pacmanCoordinates =  ourGame.getPacmanStartingCoordinates()
    ourPacman = Pacman(pacmanCoordinates[0], pacmanCoordinates[1])
    ourGhost = Ghost(ourGame)

    while ourGame.gameOver == False and ourPacman.score<20:
        ourGame.printGame()
        ourPacman.printScore()
        inp = raw_input("Enter Move: ")
        ourPacman.moveAccordingToInput(inp, ourGame)
        if ourPacman.checkCoin(ourGame):
            ourPacman.collectCoin(ourGame)
        ourPacman.checkGhost(ourGame)
        ourGhost.randomMoveGhost(ourGame)
        ourPacman.checkGhost(ourGame)

    if ourGame.gameOver:
        ourGame.printGame()
        print "Game Over your score was " + str(ourPacman.score)
    if ourPacman.score==20:
        print "You have collected all coins. You win"

main()
