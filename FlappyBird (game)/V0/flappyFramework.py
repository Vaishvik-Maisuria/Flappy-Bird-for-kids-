import pygame
from pygame.locals import *  # noqa
import sys
import random


global QUIT, MOUSECLICK
QUIT = pygame.QUIT
MOUSECLICK = pygame.MOUSEBUTTONDOWN

'''
A flappy bird framework developed to help teach young students the basic of programming
'''

class FlappyBird:
    def __init__(self):
        self.screen = pygame.display.set_mode((400, 708))
        self.score = 0
        self.offset = random.randint(-110, 110)

        pygame.init()

        self.sounds = {}
        self.sounds['die'] = pygame.mixer.Sound('assets/die.wav')
        self.sounds['hit'] = pygame.mixer.Sound('assets/hit.wav')
        self.sounds['point'] = pygame.mixer.Sound('assets/point.wav')
        self.sounds['swoosh'] = pygame.mixer.Sound('assets/swoosh.wav')
        self.sounds['wing'] = pygame.mixer.Sound('assets/wing.wav')

    def loadGameOver(self):
        self.gameOver = pygame.image.load("assets/gameover.png").convert_alpha()
        self.screen.blit(self.gameOver, (110,300))
        pygame.display.update()

    def loadGameStart(self):
        self.gameStart = pygame.image.load("assets/message.png").convert_alpha()
        self.base = pygame.image.load("assets/base.png").convert()
        self.screen.blit(self.gameStart, (28,20))
        self.screen.blit(self.base, (0,650))
        pygame.display.update()
        
    def loadBackground(self, name):
        self.background = pygame.image.load("assets/"+name+".png").convert()
        self.screen.blit(self.background, (0,0))
        pygame.display.update()

    def nameScreen(self, title):
        pygame.display.set_caption(title)

    def playSound(self, soundName):
        self.sounds[soundName].play()

    def loadBird(self, color):
        self.bird = pygame.Rect(65,50,50,50)
        self.jump = 0
        self.jumpSpeed = 0
        self.gravity = 5
        self.over = False
        self.sprite = 0
        self.birdY = 320
        if color == "yellow":
            value = 0
        elif color == "blue":
            value = 1
        elif color == "red":
            value = 2

        
        spriteList = [[pygame.image.load("assets/1.png").convert_alpha(),
    						pygame.image.load("assets/2.png").convert_alpha(),
    						pygame.image.load("assets/dead.png")],
                            [pygame.image.load("assets/bluebird-downflap.png").convert_alpha(),
                            pygame.image.load("assets/bluebird-upflap.png").convert_alpha(),
                            pygame.image.load("assets/dead.png")],
                            [pygame.image.load("assets/redbird-downflap.png").convert_alpha(),
                            pygame.image.load("assets/redbird-upflap.png").convert_alpha(),
                            pygame.image.load("assets/dead.png")]]

        self.birdSprites = spriteList[value]
        
        self.screen.blit(self.birdSprites[self.sprite], (70, self.birdY))
        pygame.display.update()

    def loadWalls(self, gap):
   		self.wallUp = pygame.image.load("assets/bottom.png").convert_alpha()
   		self.wallDown = pygame.image.load("assets/top.png").convert_alpha()
   		self.gap = gap
   		self.wallx = 400

    def updateWalls(self, speed):
        self.wallx -= speed
        if self.wallx < -80:
            self.wallx = 400
            self.offset = random.randint(-110, 110)

        self.showWalls()

    def birdUpdate(self):
        if self.jump:
            self.jumpSpeed -= 1
            self.birdY -= self.jumpSpeed
            self.jump -= 1
        else:
            self.birdY += self.gravity
            self.gravity += 0.2
        self.bird[1] = self.birdY

    def checkHitTopPipe(self):
        upRect = pygame.Rect(self.wallx, 360 + self.gap - self.offset + 10, self.wallUp.get_width() - 10, self.wallUp.get_height())

        if upRect.colliderect(self.bird):
            return True

    def checkHitBottomPipe(self):
        downRect = pygame.Rect(self.wallx, 0 - self.gap - self.offset - 10, self.wallDown.get_width() - 10, self.wallDown.get_height())

        if downRect.colliderect(self.bird):
            return True            

    def resetGame(self):
        self.bird[1] = 50
        self.birdY = 50
        self.over = False
        self.score = 0
        self.wallx = 400
        self.offset = random.randint(-110, 110)
        self.gravity = 5

    def birdNotDead(self):
    	return not self.over

    def birdDead(self):
    	return self.over

    def getClock(self):
    	return pygame.time.Clock()

    def getEvent(self):
    	return pygame.event.get()
        
    def birdJump(self):
    	self.jump = 17
    	self.gravity = 5
    	self.jumpSpeed = 10
    	self.updateBirdImage()
    	self.birdUpdate()

    def updateScore(self):
        self.screen.blit(font.render(str(self.score), -1, (255,255,255)), (200,50))
        
    def updateScreen(self):
    	self.screen.fill((255,255,255))
    	self.screen.blit(self.background, (0,0))
    	#self.screen.blit(self.wallUp, (self.wallx, 360+self.gap-self.offset))
    	#self.screen.blit(self.wallDown, (self.wallx, 0-self.gap-self.offset))
    	#self.screen.blit(font.render(str(self.score), -1, (255,255,255)), (200,50))

    def showWalls(self):
        self.screen.blit(self.wallUp, (self.wallx, 360+self.gap-self.offset))
        self.screen.blit(self.wallDown, (self.wallx, 0-self.gap-self.offset))

    def updateBirdImage(self):
    	if self.over:
    		self.sprite = 2
    	elif self.jump:
    		self.sprite = 1

    	self.screen.blit(self.birdSprites[self.sprite], (70, self.birdY))

    	if not self.over:
    		self.sprite = 0

    def wallPassed(self):
        return self.wallx >= -1 and self.wallx <= 0


    def flap(self):
        self.updateScreen()
        self.updateBirdImage()
        self.birdUpdate()

    def birdOffScreen(self):
        return not 0 < game.bird[1] < 720

def closeGame():
    pygame.quit()

def escapePressed(events):
    for event in events:
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            return True
    return False

def mouseClick(events):
    for event in events:
        if event.type == MOUSECLICK:
            return True
    return False

def checkWhichButtonsPressed():
    return pygame.event.get()

def updateScreen():
    pygame.display.update()

def updateScoreDisplay(game):
    #pygame.font.init()
    # numbers sprites for score display
    IMAGES = {}
    
    IMAGES['numbers'] = (
        pygame.image.load('assets/sprites/0.png').convert_alpha(),
        pygame.image.load('assets/sprites/1.png').convert_alpha(),
        pygame.image.load('assets/sprites/2.png').convert_alpha(),
        pygame.image.load('assets/sprites/3.png').convert_alpha(),
        pygame.image.load('assets/sprites/4.png').convert_alpha(),
        pygame.image.load('assets/sprites/5.png').convert_alpha(),
        pygame.image.load('assets/sprites/6.png').convert_alpha(),
        pygame.image.load('assets/sprites/7.png').convert_alpha(),
        pygame.image.load('assets/sprites/8.png').convert_alpha(),
        pygame.image.load('assets/sprites/9.png').convert_alpha()
    )

    scoreDigits = [int(x) for x in list(str(game.score))]
    totalWidth = 0 # total width of all numbers to be printed

    for digit in scoreDigits:
        totalWidth += IMAGES['numbers'][digit].get_width()

    Xoffset = (400 - totalWidth) / 2

    for digit in scoreDigits:
        game.screen.blit(IMAGES['numbers'][digit], (Xoffset,50))
        Xoffset += IMAGES['numbers'][digit].get_width()

    
    #return pygame.font.SysFont(fontName, fontSize)

def newGameCheck(game):
    while True:
        buttonsPressed = checkWhichButtonsPressed()
        if escapePressed(buttonsPressed):
            closeGame()
        if mouseClick(buttonsPressed):
            game.resetGame()
            return None

def checkForStart(game):

    baseOffset = 10
    x = 0
    while True:
    
        buttonsPressed = checkWhichButtonsPressed()
        if escapePressed(buttonsPressed):
            closeGame()
        if mouseClick(buttonsPressed):
            game.resetGame()
            return None

        x += 1
        if x % 200000 == 0:
            print(x)
            baseOffset = baseOffset * -1
            game.screen.blit(game.base, (baseOffset,650))
            pygame.display.update()


if __name__ == "__main__":
    game = FlappyBird()
    gameSpeed = 5
    wallGap = 350

    game.loadBackground("day")
    game.loadBird("red")

    game.loadGameStart()
    checkForStart(game)

    game.loadWalls(wallGap)
    
    clock = game.getClock()
    
    while True:
        clock.tick(60)

        buttonsPressed = checkWhichButtonsPressed()

        if escapePressed(buttonsPressed):
            closeGame()

        if mouseClick(buttonsPressed) and game.birdNotDead():
            game.birdJump()

        game.flap()
        
        game.updateWalls(gameSpeed)

        if game.wallPassed() and game.birdNotDead():
            game.score = game.score + 1 #This can be a fcn but we think its good for them to learn

        updateScoreDisplay(game)

        if game.checkHitBottomPipe() == True:
            game.over = True

        if game.checkHitTopPipe() == True:
            game.over = True

    	#If bird out of bounds
        if game.birdOffScreen():
            game.loadGameOver()
            newGameCheck(game)
                
        updateScreen()
