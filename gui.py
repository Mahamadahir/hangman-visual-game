import pygame
pygame.init()

HEIGHT = pygame.display.Info().current_h
WIDTH = pygame.display.Info().current_w
SCREEN = pygame.display.set_mode((int(WIDTH), int(HEIGHT)))
COLOUR = (25, 25, 112)
FPS = 60


def createGrid():
    #There are 3 sections :
    # A - The unknown word
    # B - The alphabet
    # C - The hanged man

    #These are rectangular sections defined by their vertices (clockwise order from leftmost corner)
     
    sectionA = [(0,0),(int(0.7*WIDTH),0) ,(int(0.7*WIDTH),int(0.4*HEIGHT)), (0, int(0.4*HEIGHT))]
    rectA = (0,0, int(0.7*WIDTH),int(0.4*HEIGHT))
    sectionB = [(0,int(0.4*HEIGHT)) ,(int(0.7*WIDTH),int(0.4*HEIGHT)) ,(int(0.7*WIDTH),HEIGHT) ,(0,HEIGHT)]   
    rectB = (0,int(0.4*HEIGHT), int(0.7*WIDTH), int(0.6*HEIGHT))
    sectionC = [(int(0.7*WIDTH),0), (WIDTH, 0), (WIDTH, HEIGHT), ((int(0.7*WIDTH), HEIGHT))] 
    rectC = (int(0.7*WIDTH), 0, int(0.3*WIDTH), HEIGHT)
    pygame.draw.rect(SCREEN, (255,255,255),rectA)
    pygame.draw.rect(SCREEN,(255, 0, 0), rectB)
    pygame.draw.rect(SCREEN, (0, 255, 0), rectC)
    

def createScreen():
    SCREEN.fill(COLOUR)
    createGrid()
    pygame.display.update()


running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    createScreen()
    clock.tick(FPS)
pygame.quit()