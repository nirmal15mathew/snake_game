import pygame
from Modules.Vector import Vector2

pygame.init()

win = pygame.display.set_mode((750, 500))
pygame.display.set_caption("learn game")
gameClock = pygame.time.Clock()

RUN = True
class Snake(object):
    def __init__(self, surface):
        self.x = 100
        self.y = 100
        self.win = surface
        self.color = (240, 240, 240)
        self.xvel = 5
        self.yvel = 0
        self.width = 10

    def show(self):
        pygame.draw.rect(self.win, self.color, (self.x, self.y, self.width, self.width))
    
    def update(self):
        self.x += self.xvel
        self.y += self.yvel


dani = Snake(win)

def updateGameWindow():
    win.fill((51,51,51)) # Gives a grey background
    # all drawings here
    dani.show()
    dani.update()
    print(gameClock.get_fps())
    pygame.display.update() # Updates pygame window

while RUN:
    gameClock.tick(60) # sets the frame rate

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
    
    updateGameWindow()

pygame.quit()