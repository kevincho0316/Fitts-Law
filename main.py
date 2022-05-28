import pygame
import sys
import random
import csv
import time
import math


def time_stamp():
    import time
    timestr = time.strftime("%Y%m%d-%H%M%S")
    return timestr

def file(name,data):
    with open("data/"+file_name+".csv", 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)



SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720

white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
pygame.display.set_caption("fitt's Law")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
size = random.randint(10,100)
pos_x = random.randint(0, SCREEN_WIDTH-size-size)+size
pos_y = random.randint(0, SCREEN_HEIGHT-size-size)+size
initial_mouse_x = pygame.mouse.get_pos()[0]
initial_mouse_y = pygame.mouse.get_pos()[1]
rec_middle_x = pos_x + round(size/2)
rec_middle_y = pos_y + round(size/2)
start = time.time()

realtime_pos=[]

click = False
file_name = time_stamp()

open("data/"+file_name+".csv", 'w', encoding='UTF8', newline='')

pygame.mouse.set_pos((SCREEN_WIDTH/2,SCREEN_HEIGHT/2))

while True:
    clock.tick(60)

    if click ==True:
        while pos_x<pygame.mouse.get_pos()[0]<pos_x+size and pos_y<pygame.mouse.get_pos()[1]<pos_y+size:
            size = random.randint(10,100)
            pos_x = random.randint(0, SCREEN_WIDTH-size-size)+size
            pos_y = random.randint(0, SCREEN_HEIGHT-size-size)+size
            initial_mouse_x = pygame.mouse.get_pos()[0]
            initial_mouse_y = pygame.mouse.get_pos()[1]
            rec_middle_x = pos_x + round(size/2)
            rec_middle_y = pos_y + round(size/2)
            realtime_pos=[]
            click = False

            start = time.time()  # 시작 시간 저장


    screen.fill(black)
    pygame.draw.rect(screen, white, [pos_x, pos_y,size,size])
    realtime_pos.append(pygame.mouse.get_pos())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pos_x<pygame.mouse.get_pos()[0]<pos_x+size and pos_y<pygame.mouse.get_pos()[1]<pos_y+size:
                click = True
                file(file_name, [rec_middle_x,rec_middle_y,size,initial_mouse_x,initial_mouse_y,pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],time.time() - start,realtime_pos])

    

    

    pygame.display.update()