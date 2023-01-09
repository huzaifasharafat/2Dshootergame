import pygame
import sys
import os
import time


'''
Variables
'''
e = False
worldx = 960
worldy = 720
fps = 40
ani = 3
world = pygame.display.set_mode([worldx, worldy])
enemycount = 0
BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (34, 177, 76)
steps = 10
'''
Objects
'''


class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join('images', 'hero.png'))
        #img.convert_alpha()  # optimise alpha
        #img.set_colorkey(ALPHA)  # set alpha
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()


    def control(self,x, y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y
    def draw(self,world):

        world.blit(self.image,(self.rect.x,self.rect.y))

    def update(self):
        """
        Update sprite position
        """

        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        # moving left

class boundry(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load(os.path.join('images', 'boundry.png'))
        # img.convert_alpha()  # optimise alpha
        # img.set_colorkey(ALPHA)  # set alpha
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = 50  # go to x
        self.rect.y = 0

class enemy(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self,world,y):
        pygame.sprite.Sprite.__init__(self)
        #print ("created a new sprite:", id(self))
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join('images', 'enemy.png'))
        #img.convert_alpha()  # optimise alpha
        #img.set_colorkey(ALPHA)  # set alpha
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = 50  # go to x
        self.rect.y = y
        #self.rect.y = 100 * enemycount  # go to y


class bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join('images', 'bullet.png')).convert()
        img.convert_alpha()  # optimise alpha
        img.set_colorkey(ALPHA)  # set alpha
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = 10000  # go to x
        self.rect.y = 10  # go to y
    def control(self,x,y):
        self.rect.x = x
        self.rect.y = y + 15
        self.movex = -5

    def update(self):

        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

class enemybullet(pygame.sprite.Sprite):
    def __init__(self,enemycount):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join('images', 'bullet.png')).convert()
        img.convert_alpha()  # optimise alpha
        img.set_colorkey(ALPHA)  # set alpha
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = -10000  # go to x
        self.rect.y = 10  # go to y
    def control(self,x,y):
        self.rect.x = x+53
        self.rect.y = y+17
        self.movex= 5

    def update(self):

        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

'''
Setup
'''

backdrop = pygame.image.load(os.path.join('images', 'stage.png'))
circle = pygame.image.load(os.path.join('images', 'hero1.png'))
over = pygame.image.load(os.path.join('images', 'over.png'))
blk = pygame.image.load(os.path.join('images','black.png'))
level1 = pygame.image.load(os.path.join('images','level1.png'))
level1s = pygame.image.load(os.path.join('images','level1small.png'))
level2 = pygame.image.load(os.path.join('images','level2.png'))
level2s =pygame.image.load(os.path.join('images','level2small.png'))
end = pygame.image.load(os.path.join('images','end.png'))
over.convert_alpha()
over.set_colorkey(ALPHA)
clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()

main = True

player = Player()  # spawn playere
player.rect.x = 850  # go to x
player.rect.y = 250  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
boundry = boundry()
b_list = pygame.sprite.Group()
b_list.add(boundry)
#player2 = Player()  # spawn player
print(player_list.sprites())
enemies = pygame.sprite.Group()
enemiesbullets = pygame.sprite.Group()
bullet = bullet()
#bullet.rect.x=1000
bullet_list=pygame.sprite.Group()
bullet_list.add(bullet)

'''
Main Loop
'''
edead = 0
playerdead = False
colid = False
wcolid = False
b=False
k= ''
w= ''
p1shot= time.time()-5
print(time.time()-p1shot)
eshot = time.time()-5
level =1
adead = time.time()
start = time.time()
ed = False

while main:
    d = False
    if player.rect.colliderect(boundry.rect):
        if (k == pygame.K_LEFT or k == ord('a')) and colid == False:
            player.control(steps, 0)
            colid = True
        if (k == pygame.K_RIGHT or k == ord('d')) and colid == False:
            player.control(-steps, 0)
            colid = True


    for x in enemies.sprites():
        if bullet.rect.colliderect(x.rect):
            #x.control(-10000, 0)
            x.kill()
            edead += 1
            print(player.rect.colliderect(x.rect),edead)
            if edead == 2 and level == 1:
                level = 2
                enemycount = 0
                #enemiesbullets.empty()
                #bullet_list.empty()
                adead= time.time()
                start = time.time()
            elif edead == 3 :
               ed = True

    if e== True:
        for x in enemiesbullets.sprites():
            if x.rect.colliderect(player.rect):
                player.kill()
                playerdead = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        if event.type == pygame.KEYDOWN:

            if event.key == ord('q'):
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False
            if playerdead == True and event.key == ord('r'):
                player.rect.x = 800  # go to x
                player.rect.y = 250
                player_list.add(player)
                level = 1
                playerdead = False
                d = True
                adead = time.time()
                start = time.time()
            else:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    k = event.key
                    player.control(-steps, 0)
                    colid = False

                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    k = event.key
                    colid = False
                    player.control(steps, 0)

                if event.key == pygame.K_UP or event.key == ord('w'):
                    w = event.key
                    player.control(0,-steps)

                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    w = event.key
                    player.control(0, steps)

                if event.key == ord("b") and (time.time()-p1shot)>=5:
                    b = True
                    bullet.control(player.rect.x, player.rect.y)
                    p1shot=time.time()
                '''
                if event.key == ord('e'):
                    enemycount +=1
                    enemies.add(enemy(world))
                    enemiesbullets.add(enemybullet(enemycount))
                    #print(enemies.sprites())
                    #print(enemiesbullets.sprites())
                    e = True
                '''

        if event.type == pygame.KEYUP :
            if (event.key == pygame.K_LEFT or event.key == ord('a')) and colid == False :
                    #print("colid")
                    player.control(steps, 0)
            if (event.key == pygame.K_RIGHT or event.key == ord('d'))and colid == False:
                    player.control(-steps, 0)
            if event.key == pygame.K_UP or event.key == ord('w')  :
                    player.control(0, steps)
            if event.key == pygame.K_DOWN or event.key == ord('s') :
                    player.control(0, -steps)

    if time.time()-adead >= 2:
        if level == 1 and enemycount != 2:
            edead = 0
            e = True
            player.rect.x = 850  # go to x
            player.rect.y = 250  # go to y
            for i in range(0, 2):
                y = 100 + 400*enemycount
                enemycount += 1
                enemies.add(enemy(world,y))
                enemiesbullets.add(enemybullet(enemycount))
#        enemies.sprites().remove()
        if level == 2 and enemycount != 3:
            edead = 0
            e = True
            player.rect.x = 850  # go to x
            player.rect.y = 250  # go to y
            for i in range(0, 3):
                y = 100 + 200 * enemycount
                enemycount += 1
                enemies.add(enemy(world, y))
                enemiesbullets.add(enemybullet(enemycount))
    world.blit(backdrop, backdropbox)
    if time.time()-start < 1.5 and level == 1:
        world.blit(level1,(385,200))
    elif time.time()-start < 1.5 and level == 2:
        world.blit(level2,(400,200))
    if level ==1 :
        world.blit(level1s,(470,0))
    elif level == 2:
        world.blit(level2s,(470,0))

    #world.blit(circle , (50,50))
    player.update()
    #player2.update()
    player.draw(world)
    enemies.draw(world)
    #print(player_list)
    if playerdead == True:
        world.blit(blk,(0,0))
        world.blit(over,(300,250))
    if ed == True:
        world.blit(blk, (0, 0))
        world.blit(end, (250, 150))
        playerdead = True
    c=0
    if e == True and time.time()-eshot>=4:
        for i in enemies.sprites():
            #print(time.time()-eshot)
            enemiesbullets.sprites()[c].control(i.rect.x, i.rect.y)

            c += 1
        eshot = time.time()
    enemiesbullets.update()
    enemiesbullets.draw(world)



    bullet.update()
    bullet_list.draw(world)

    pygame.display.flip()
    clock.tick(60)
