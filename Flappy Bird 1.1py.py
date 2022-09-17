import pygame, random, sys
from pygame.locals import *
windowWidth = 800
windowHeight = 800
FPS = 40
def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
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
pygame.display.set_caption("Flappy Bird 1.1")
windowSurface = pygame.display.set_mode((windowWidth,windowHeight))
font = pygame.font.SysFont(None, 48)
playerRect = pygame.Rect((windowWidth/2)-74,(windowHeight/2)-50,50,50)
path = "C:/Users/dombr_nwji1sf/OneDrive/Documents/Programming/Python/Flappy Bird/Resources/"
playerImage = pygame.image.load(path + "Bird.png")
backgroundImage = pygame.image.load(path +"FBBackground.png")
bottomBarRect = pygame.Rect(0,windowHeight - 125,800,125)
bottomBarImage = pygame.image.load(path +"FBBottomBar.png")
topPipeImage = pygame.image.load(path +"FBTopPipe.png")
bottomPipeImage = pygame.image.load(path +"FBBottomPipe.png")
greenBarImage = pygame.image.load(path +"FBGreenBar.png")
while True:
    velocity = 0
    counter = 0
    playerRect = pygame.Rect((windowWidth/2)-37,(windowHeight/2)-50,50,50)
    windowSurface.fill((255,255,255))
    windowSurface.blit(backgroundImage,(0,0))
    windowSurface.blit(playerImage,playerRect)
    windowSurface.blit(bottomBarImage,bottomBarRect)
    drawText("Play? Press Space",50,200)
    pygame.display.update()
    waitForPlayerToPressKey()
    velocity = 21
    topPipes = []
    bottomPipes = []
    greenBars = [pygame.Rect(0,675,800,29)]
    pipeStartCounter = 0
    pipeAddCounter = 0
    breaker = False
    score = 0
    scoreFile = open(path +"FBScores.txt","r")
    topScore = int(scoreFile.read())
    scoreFile.close()
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    velocity = 21
                if event.key == K_ESCAPE:
                    terminate()
        if counter % 160 == 0:
            greenBars.append(pygame.Rect(800,675,800,29))
        if counter % 3 == 0:            
            velocity -= 6
        playerRect.move_ip(0,int(-1*velocity))
        gameOver = False
        if playerRect.bottom >= windowHeight or playerRect.top <= 0 or playerRect.colliderect(bottomBarRect):
            break
        pipes = topPipes + bottomPipes
        for p in pipes:
            if playerRect.colliderect(p):
                breaker = True
        if breaker:
            break
        windowSurface.blit(backgroundImage,(0,0))

        if pipeStartCounter <= 100:
            pipeStartCounter += 1
        else:
            pipeAddCounter += 1
        if pipeAddCounter == 100:
            pipeAddCounter = 0
            pipeGap = random.randint(75,400)
            newTopPipe = pygame.Rect(800,pipeGap-750,135,750)
            newBottomPipe = pygame.Rect(800,pipeGap+200,135,750)
            topPipes.append(newTopPipe)
            bottomPipes.append(newBottomPipe)
        for tpipe in topPipes[:]:
            windowSurface.blit(topPipeImage,tpipe)
            pygame.draw.rect(topPipeImage,(0,0,0),tpipe)
            tpipe.move_ip(-5,0)
            if tpipe.right <= 0:
                topPipes.remove(tpipe)
            if (tpipe.left)+70 == windowWidth/2:
                score += 1
        for bpipe in bottomPipes[:]:
            windowSurface.blit(bottomPipeImage,bpipe)
            pygame.draw.rect(bottomPipeImage,(0,0,0),bpipe)
            bpipe.move_ip(-5,0)
            if bpipe.right <= 0:
                bottomPipes.remove(bpipe)
        windowSurface.blit(bottomBarImage,bottomBarRect)
        for gBar in greenBars[:]:
            windowSurface.blit(greenBarImage,gBar)
            pygame.draw.rect(greenBarImage,(0,0,0),gBar)
            gBar.move_ip(-5,0)
            if gBar.right <= 0:
                greenBars.remove(gBar)
        drawText(str(score),windowWidth/2,150)
        windowSurface.blit(playerImage,playerRect)
        pygame.draw.rect(playerImage,(0,0,0),playerRect)
        pygame.display.update()
        counter += 1
        mainClock.tick(FPS)
    if score > topScore:
        topScore = score
        scoreChangeFile = open(path +"FBScores.txt","w")
        scoreChangeFile.write(str(topScore))
        scoreChangeFile.close()
    windowSurface.blit(backgroundImage,(0,0))
    windowSurface.blit(playerImage,playerRect)
    for bpole in bottomPipes:
        windowSurface.blit(bottomPipeImage,bpole)
    for tpole in topPipes:
        windowSurface.blit(topPipeImage,tpole)
    windowSurface.blit(bottomBarImage,bottomBarRect)
    pygame.draw.rect(playerImage,(0,0,0),playerRect)
    drawText("Game Over!",50,50)
    drawText("Play again?",50,100)
    drawText("Score: " + str(score),50,150)
    drawText("Top Score: " + str(topScore),50,200)
    pygame.display.update()   
    waitForPlayerToPressKey()