import pygame,sys
pygame.init()
screen=pygame.display.set_mode((640,520))
pygame.display.set_caption("Alien Invasion")
myspace=pygame.image.load("C:\\Users\\vidha\\Desktop\\Mini Projects\\pygame\\images\\ship_shield.png").convert()
pygame.display.flip()
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    for i in range(1):
        screen.blit(myspace,(280,465))

    pygame.display.update()
pygame.quit()