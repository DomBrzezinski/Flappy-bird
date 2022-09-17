import pygame, random, sys
from pygame.locals import *

windowWidth = 600
windowHeight = 600
FPS = 60

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Pressing ESC quits.
                    terminate()
                if event.key == K_SPACE:
                    return
def terminate():
    pygame.quit()
    sys.exit()
def drawText(text,x,y):
    textObject = font.render(text,1,(0,0,0))
    textRect = textObject.get_rect()
    textRect.topleft = (x,y)
    windowSurface.blit(textObject, textRect)
pygame.init()
mainClock = pygame.time.Clock()
pygame.display.set_caption("Flappy Bird Alpha")
windowSurface = pygame.display.set_mode((windowWidth,windowHeight))
font = pygame.font.SysFont(None, 48)
playerRect = pygame.Rect(windowWidth/2,windowHeight/2,50,50)
playerImage = pygame.image.load("Bird.png")

while True:
    velocity = 0
    counter = 0
    windowSurface.fill((255,255,255))
    windowSurface.blit(playerImage,playerRect)
    drawText("Play? Press Space",50,200)
    pygame.display.update()
    waitForPlayerToPressKey()
    velocity = 17
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    velocity = 17
                if event.key == K_ESCAPE:
                    terminate()
        if counter == 3:            
            velocity -= 5
            counter = 0
        playerRect.move_ip(0,int(-1*velocity))
        gameOver = False
        if playerRect.bottom >= windowHeight or playerRect.top <= 0:
            break
        windowSurface.fill((255,255,255))
        windowSurface.blit(windowSurface,playerRect)
        print(str(velocity))
        pygame.draw.rect(playerImage,(0,0,0),playerRect)
        pygame.display.update()
        counter += 1
        mainClock.tick(FPS)
    windowSurface.blit(playerImage,playerRect)
    windowSurface.fill((255,255,255))
    drawText("Game Over!",50,50)
    drawText("Play again?",50,150)
    pygame.display.update()   
    waitForPlayerToPressKey()
            
