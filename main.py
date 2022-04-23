import pygame
import sys
import os

pygame.init()

# Predefined Colors
white = (255, 255, 255)

# Main Surface object
dimension_main = width, height = (800, 600)
window_surf = pygame.display.set_mode(dimension_main)
# caption title
pygame.display.set_caption("Breakers")

# background (surface object)
bg = pygame.image.load(os.path.join('assets/',
                                    'background.png'))
bg = pygame.transform.scale(bg, dimension_main)

# player loading, sizing, and converting to Rect objects
playerImg = pygame.image.load(os.path.join('assets/',
                                        'player.png'))
playerImg = pygame.transform.scale(playerImg, (110,30))
player_pos = playerX, playerY = 100, 500
player = playerImg.get_rect(topleft=player_pos)

# Ball loading, sizing, and converting to Rect objects
ballImg = pygame.image.load(os.path.join('assets/',
                                         'ball.png'))
ballImg = pygame.transform.scale(ballImg, (50, 50))
ball_pos = ballX, ballY = 50, 60
ball = ballImg.get_rect(topleft=ball_pos)
ball_speed = [5,5]

# bricks loading, sizing, and converting to Rect objects
brickImg = pygame.image.load(os.path.join('assets/'
                                        'brick.png'))
brickImg = pygame.transform.scale(brickImg, (110,30))
brick = brickImg.get_rect()
# dimensions of Rects and its distance from each
rectwidth = 110
rectheight = 30
rectdist = 10

# draw location of where bricks are gonna go, 12 rectangles
block_position = [] # (left, top) values
for i in range(6): # columns
    for j in range(2): # rows
        x = 20 + i * (rectdist + rectwidth)
        y = 20 + j * (rectdist + rectheight)
        block_position.append((x, y))

# creates a list of Rec objects, using elements from block_position
bricks = [pygame.Rect((x, y), (rectwidth, rectheight)) for x, y in\
         block_position]

font = pygame.font.Font("freesansbold.ttf", 64)

# Display Game Over
def Game_Over():
    over_text = font.render("Game Over", True, (white))
    window_surf.blit(over_text, (200, 150))
    pygame.display.update()
    pygame.time.wait(5000)
    pygame.quit()
    sys.exit()

# brick and ball collision
def is_Collision(rec1, rec2, rec_lst):
    """
        rec1 param: ball,
        rec2 param: brick
        rec_lst param: list of rec objects
        takes a rec object to tests if it collides with 2nd rect object
        if so, deletes rec object from list of rects
        else just returns the list of recs
    """
    global ball
    if rec1.colliderect(rec2):
        ball_speed[1] = -(ball_speed[1])
        ball = ball.move(ball_speed)
        rec_lst.pop(rec1.collidelist(rec_lst))

        return rec_lst
    else:
        return rec_lst

while 1:

    window_surf.blit(bg, (0,0))

    # checks if user quits program with X box
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # ball and player collision
    if ball.colliderect(player):
        if ball.collidepoint(player.topleft):
            ball_speed[1] = -(ball_speed[1])
            ball = ball.move(ball_speed)
        elif ball.collidepoint(player.topright):
            ball_speed[1] = -(ball_speed[1])
            ball = ball.move(ball_speed)
        elif ball.collidepoint(player.midtop):
            ball_speed[1] = -(ball_speed[1])
            ball = ball.move(ball_speed)
        elif ball.collidepoint(player.midleft) or ball.collidepoint(player.midright):
            ball_speed[0] = -(ball_speed[0])

    # checking for ball boundary
    if ball.right >= width or ball.left <= 0:
        ball_speed[0] = -(ball_speed[0])
    if ball.bottom >= height or ball.top <= 0:
        ball_speed[1] = -(ball_speed[1])
    ball = ball.move(ball_speed)

    # player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and player.right <= width:
        player = player.move(5,0)
    if keys[pygame.K_LEFT] and player.left >= 0:
        player = player.move(-5,0)

    # checks if all bricks have been cleared, to end game
    if len(bricks) == 0:
        Game_Over()

    # iterates through list of Rect objects and draws onto surface
    for brick in bricks:
        bricks = is_Collision(ball, brick, bricks)
        window_surf.blit(brickImg, brick)

    window_surf.blit(playerImg, player)
    window_surf.blit(ballImg, ball)
    pygame.display.update()

pygame.quit()

# code on standby for use
# pygame.time.wait(5000)
# sys.exit()
