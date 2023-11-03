import pygame,sys
import random
pygame.font.init()
#STARTING THE GAME
pygame.init()

#SETTING THE SCREEN SIZE
WIDTH,HEIGHT=640,520
WIN=pygame.display.set_mode((WIDTH,HEIGHT))

#CHANING THE CAPTION OF THE GAME
pygame.display.set_caption("Alien Invasion")

#player spaceplayer
MYSPACE=pygame.image.load("images\\ship.png").convert()

#shooting missile
MISSILE=pygame.image.load("images\\missile.png").convert()
#ememys spaceplayer
ALIEN1=pygame.image.load("images\\space_invader_red.png").convert()
ALIEN2=pygame.image.load("images\\space_invader_blue.png").convert()
ALIEN3=pygame.image.load("images\\space_invader_green.png").convert()
ALIEN4=pygame.image.load("images\\space_invader_yellow.png").convert()
ALIEN5=pygame.image.load("images\\space_invader_white.png").convert()
#background
BG=pygame.transform.scale(pygame.image.load("images\\background-image.gif"),(WIDTH,HEIGHT))

#SETTING UP THE ICON OF THE GAME
pygame.display.set_icon(MYSPACE)

class Ship:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.myspace=None
        self.missile=None
        self.lasers=[]

    def draw(self,window):
       window.blit(self.myspace,(self.x,self.y))

#Player will inherit Ship
class Player(Ship):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.myspace=MYSPACE
        self.missile=MISSILE
        # mask helps to find the collision of the object as 1 bit per pixel
        self.mask=pygame.mask.from_surface(self.myspace)

#Ememy will inherit Ship
class Enemy(Ship):
    COLOR_MAP={
        "red":(ALIEN1),
        "blue":(ALIEN2),
        "green":(ALIEN3),
        "yellow":(ALIEN4),
        "white":(ALIEN5)
    }
    def __init__(self, x, y,color):
        super().__init__(x, y)
        self.myspace=self.COLOR_MAP[color]
        self.mask=pygame.mask.from_surface(self.myspace)

    def move(self,vel):
        self.y+= vel
def main():
    Run=True
    FPS=60
    CLOCK=pygame.time.Clock()
    lives=3
    level=1
    #this is to maintain the speed
    player_vel=5
    
    # To set the style and size of the text 
    main_font=pygame.font.SysFont("comicsans",30)

    #for the enemies
    enemies=[]
    wave_length=5
    enemy_vel=1
    # calling the class player
    player=Player(270,470)

    def redraw():
        #display BG on screen
        WIN.blit(BG,(0,0))

        #draw text
        lives_label=main_font.render(f"Lives:{lives}",1,(255,255,255))
        level_label=main_font.render(f"Level:{level}",1,(255,255,255))
        
        #display text on screen
        WIN.blit(lives_label,(10,10))
        WIN.blit(level_label,(WIDTH-level_label.get_width()-10,10))

        # for each enemy it will show on the screen
        for enemy in enemies:
            enemy.draw(WIN)
        player.draw(WIN)
        pygame.display.update()
    while Run:
        CLOCK.tick(FPS)
    
        if len(enemies)==0:
            level+=1
            #As soon as the level increases the number of enemies also increases 
            wave_length+=5
            for i in range(wave_length):
                enemy=Enemy(random.randrange(50,WIDTH-100),random.randrange(-1500,100),random.choice(["red","blue","green","yellow","white"]))
                enemies.append(enemy)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run= False
                sys.exit()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and player.y + player_vel +50< HEIGHT:#bottom
            player.y+=player_vel
        if keys[pygame.K_UP] and player.y - player_vel > 0:#up
            player.y-=player_vel
        if keys[pygame.K_LEFT] and player.x - player_vel > 0:#left
            player.x-=player_vel
        if keys[pygame.K_RIGHT] and player.x + player_vel +50< WIDTH:#right
            player.x+=player_vel

        for enemy in enemies:
            enemy.move(enemy_vel)
        redraw()
main()

pygame.quit()