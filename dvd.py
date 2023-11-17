import math
import pygame

RUNNING  = True

WIN_SIZE = (600,600)
WIN_TITLE = 'DVD'

BLACK = (0,0,0)

win = pygame.display.set_mode(WIN_SIZE)

pygame.display.set_caption(WIN_TITLE)

pos = [WIN_SIZE[0]/2,WIN_SIZE[1]/2]
pos_offsetx = 50
pos_offsety = 50
direction = [2,3]

speed = 0.2
speedx = speedy = speed

dvd = pygame.image.load('logo.png').convert_alpha()
dvd = pygame.transform.scale(dvd,(150,100))

def normalize(vec):
    mag = math.sqrt((vec[0]*vec[0])+(vec[0]*vec[0]))
    return [vec[0]/mag,vec[1]/mag]

def draw_img(win,x,y):
    global dvd
    win.blit(dvd,(x,y))

direction = normalize(direction)

while RUNNING:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit()
    win.fill(BLACK)
    draw_img(win,pos[0],pos[1])

    pos_offset = [pos[0]+pos_offsetx,pos[1]+pos_offsety]
    
    if pos_offset[0] > WIN_SIZE[0]:
        speedx = -speed 
    if pos_offset[1] > WIN_SIZE[1]:
        speedy = -speed 
    if pos_offset[0] < 0:
        speedx = speed
    if pos_offset[1] < 0:
        speedy = speed  

    pos[0] += direction[0]*speedx
    pos[1] += direction[1]*speedy

    pygame.display.update()
