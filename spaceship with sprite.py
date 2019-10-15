import pygame
import sys
import os

pygame.init()

os.chdir(os.getcwd() + '/spaceship')
"""   EFFECTLER  """
hit = pygame.mixer.Sound('boom9.wav')
hit.set_volume(0.5)
"""    MUSİC    """

pygame.mixer.music.load('Vindication.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)
"""    IMAGES   """

fire = pygame.image.load('fire2.png')
ship_image = pygame.image.load('greenships.png')
bg = pygame.image.load('bg1.png')
laser = pygame.image.load('Red_laser.png')
laser = pygame.transform.scale(laser,(60,20))

"""---OPTİONS---"""

WIDTH = 1000
HIGHT = 600
font = pygame.font.SysFont("Helvetica",100)

win = pygame.display.set_mode((WIDTH , HIGHT))
clock = pygame.time.Clock()



class spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = ship_image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.kalakn = 100
        print(self.rect)
        self.fuze_sayisi = 100

    def update(self, *args):
        up, down, right, left = args

        if up:
            self.rect.y -= 10
        if down:
            self.rect.y += 10

    def shoot(self):
        if self.fuze_sayisi == 0:
            pass
        else:
            fuze = Fuze(self.rect.y)
            self.fuze_sayisi -=1
            all_sprites.add(fuze)
            fuzeler.add(fuze)
            hit.play()
class Fuze(pygame.sprite.Sprite):
    def __init__(self,parcay):
        super().__init__()
        self.image = laser
        print(parcay)
        #self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.x = 44
        self.rect.y = parcay +40
    def update(self, *args):
        self.rect.x += 8
        if self.rect.left > WIDTH:
            self.kill()



"""GRUPLAR"""
all_sprites = pygame.sprite.Group()
mermiler = pygame.sprite.Group()
fuzeler = pygame.sprite.Group()

wight_text = font.size('100')[0]
height_text = font.size('100')[1]

print(wight_text , '-' , height_text)
ship = spaceship()
all_sprites.add(ship)
while True :
    win.fill((0, 0, 0))
    win.blit(bg,(0,0))
    keys = pygame.key.get_pressed()

    fuze_sayisi = font.render(str(ship.fuze_sayisi), 0, (255, 255, 255))
    win.blit(fuze_sayisi, ( 832 , 487))

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ship.shoot()

    up, down, right, left = keys[pygame.K_UP], keys[pygame.K_DOWN], keys[pygame.K_RIGHT], keys[pygame.K_LEFT]
    all_sprites.update(up,down,right,left)
    all_sprites.draw(win)
    pygame.display.update()