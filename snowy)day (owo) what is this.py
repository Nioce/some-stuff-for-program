# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "SNOWY DAYYY(press y)[ᵔĹ̯ᵔ] [ᵔĹ̯ᵔ] [ᵔĹ̯ᵔ] [ᵔĹ̯ᵔ] [ᵔĹ̯ᵔ] [ᵔL̯ᵔ] andrew.wilomovsky"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)
BLACK = (0,0,0)
def snowww(x,y):
    pygame.draw.rect(screen, WHITE, [x + 2, y + 2, 6, 4])
def smoldraw_cloud(x, y):
    pygame.draw.ellipse(screen, YELLOW, [x, y + 10, 20 , 20])
    pygame.draw.ellipse(screen, YELLOW, [x + 30, y + 10, 20 , 20])
    pygame.draw.ellipse(screen, YELLOW, [x + 10, y + 10, 5, 5])
    pygame.draw.ellipse(screen, YELLOW, [x + 16, y, 25, 25])
    pygame.draw.rect(screen, YELLOW, [x + 10, y + 10, 30, 20])


def draw_cloud(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])

def yellowsnow(x, y):
    pygame.draw.rect(screen, YELLOW, [x + 1, y + 1, 2, 2])
''' make clouds '''
snow = []

ysnow = []

clouds = []
for i in range(10):
    x = random.randrange(-100, 1600)
    y = random.randrange(0,200)
    speed = random.randrange(1, 4)
    clouds.append([x, y, speed])

smallclouds = []
for i in range(10):
    x = random.randrange(-100, 1600)
    y = random.randrange(0,200)
    speed = random.randrange(5, 6)
    smallclouds.append([x, y, speed, snow])
    
# Game loop
done = False

ysnowove  = False


   
while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                ysnowove = not ysnowove
    # Game logic
    ''' move clouds '''

        
    for c in clouds:
        c[0] -= c[2]
        if c[2] <= 4:
            pygame.mixer.music.load('Neewwwwww.wav')
            pygame.mixer.music.play(1)
        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(0, 200)

        if random.randrange(0, 10) < 3:
            snow_x = random.randrange(c[0], c[0] + 60)
            snow_y = c[1] + 40
            snow.append([snow_x, snow_y])
        
    for s in snow:
        s[1] += random.randrange(1, 10)
        s[0] += random.randrange(0, 5)

            

    snow = [s for s in snow if s[1] < 600]   
            

    for c in smallclouds:
        c[0] -= c[2]
        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(0, 200)
        if random.randrange(0, 10) < 3:
            if ysnowove  == True:
                ysnow_x = random.randrange(c[0], c[0] + 60)
                ysnow_y = c[1] + 40
                ysnow.append([ysnow_x, ysnow_y])

    for s in ysnow:
        s[1] += random.randrange(1, 10)
        s[0] += random.randrange(0, 5)
    ysnow = [s for s in ysnow if s[1] < 600] 
    # Drawing code

    
    ''' sky '''
    screen.fill(BLUE)


    ''' Smol cloud'''
    for c in smallclouds:
        smoldraw_cloud(c[0], c[1])
    for s in ysnow:
        yellowsnow(s[0], s[1])
    ''' sun '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

    ''' clouds '''
    for c in clouds:
        draw_cloud(c[0], c[1])
    for s in snow:
        snowww(s[0], s[1])

    ''' grass '''
    pygame.draw.rect(screen, WHITE, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)

    ''' shnow '''

    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
