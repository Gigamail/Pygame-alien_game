import pygame,sys
pygame.init()
screen=pygame.display.set_mode((640,520))
pygame.display.set_caption("Alien Invasion")
myspace=pygame.image.load("C:\\Users\\vidha\\Desktop\\Mini Projects\\pygame\\images\\ship.png").convert()
pygame.display.set_icon(myspace)
pygame.display.flip()
x=280
y=465
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        y+=1
    if keys[pygame.K_UP]:
        y-=1
    if keys[pygame.K_LEFT]:
        x-=1
    if keys[pygame.K_RIGHT]:
        x+=1
    screen.blit(myspace,(x,y))
    pygame.display.update()
pygame.quit()