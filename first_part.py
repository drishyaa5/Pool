import pygame
import pymunk
import pymunk.pygame_util

pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 678

#game window
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Pool")

#pymunk space
space = pymunk.Space()
static_body = space.static_body
draw_options = pymunk.pygame_util.DrawOptions(screen)


#clock
clock = pygame.time.Clock()
FPS = 120


#colors
BG = (50,50,50)


#function for creating balls
def create_ball(radius,pos):
    body = pymunk.Body()
    body.position = pos

    shape = pymunk.Circle(body, radius)
    shape.mass = 5

    space.add(body,shape)
    return shape

new_ball = create_ball(25, (300,300))

cue_ball = create_ball(25,(600,310))
#gameloop 
run = True
while run:

    clock.tick(FPS)
    space.step(1 / FPS)

    #fill bg
    screen.fill(BG)
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            cue_ball.body.apply_impulse_at_local_point((-1500,0),(0,0))
        if event.type == pygame.QUIT:
            run = False

    space.debug_draw(draw_options)
    pygame.display.update()

pygame.quit()