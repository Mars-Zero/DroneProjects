import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((400,400))

def getKey(keyName):
    sol = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        sol=True
    pygame.display.update()

    return sol

def main():
    if getKey("LEFT"):
        print("Ai apasat tasta LEFT")
    if getKey("RIGHT"):
        print("Ai apasat tasta RIGHT")


if __name__=='__main__':
    init()
    while True:
        main()