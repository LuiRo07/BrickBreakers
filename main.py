import pygame
import sys
import os

pygame.init()

# caption title
pygame.display.set_caption("Brick Breakers")

# font to display text
font = pygame.font.Font("freesansbold.ttf", 64)

# Predefined Colors
white = (255, 250, 250)

# clock object
clock = pygame.time.Clock()

# Display Game Over
def Game_Over():
    over_text = font.render("Game Over", True, (white))
    window_surf.blit(over_text, (200, 150))
    pygame.display.update()
    pygame.time.wait(4000)
    pygame.quit()
    sys.exit()

# displays Winner
def Winner():
    win_text = font.render("You Win!", True, white)
    window_surf.blit(win_text, (200, 150))
    pygame.display.update()
    pygame.time.wait(4000)
    pygame.quit()
    sys.exit()

# creates image surface from asset files
def create_imgSurf(img_name, size):
    BASE = 'assets/'
    surf_img = pygame.image.load(os.path.join(BASE + img_name))
    surf_img = pygame.transform.scale(surf_img, size)
    return surf_img

# Main Surface
mainSurf_dimensions = surf_width, surf_height = (800, 600)
window_surf = pygame.display.set_mode(mainSurf_dimensions)

# background
bg = create_imgSurf('background.png', mainSurf_dimensions)

# player
player_size = (110, 30)
player_pos = (100, 500)
playerSurf = create_imgSurf('player.png', player_size)
playerRect = playerSurf.get_rect(topleft=player_pos)

# ball
ball_size = (50, 50)
ballSurf = create_imgSurf('ball.png', ball_size)
ball_start = ballX, ballY = (0, 350)
ballRect = ballSurf.get_rect(topleft=ball_start)
ball_speeds = {"easy": [2, 2], "medium": [3, 3], "hard": [5, 5]}
ball_speed = ball_speeds["easy"]

# bricks
brick_size = (110, 30)

# bricks will draw according to brick coordinates
def get_brickPositions():
    block_positions = [] # (left, top) values
    rectdist = 5

    for i in range(6): # columns
        for j in range(4): # rows
            x = 20 + i * (rectdist + brick_size[0])
            y = 20 + j * (rectdist + brick_size[1])
            block_positions.append((x, y))

    return block_positions

def  getSurf_copy(surf):
    return surf.copy()


brickSurf = create_imgSurf('brick.png', brick_size)
brick_positions = get_brickPositions()
brickRecs = [pygame.Rect((x, y), brick_size) for x, y in\
        brick_positions]

# updates the speed of ball depending on the number of bricks left
def check_speed():
    global ball_speed

    if len(brickRecs) == 12:
        ball_speed = ball_speeds["medium"]
    elif len(brickRecs) == 9:
        ball_speed = ball_speeds["hard"]
    return ball_speed

# game loop
while 1:
    # draw background first
    window_surf.blit(bg, (0,0))

    # checks if user quits program with X box
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # starts ball movement
    ballRect = ballRect.move(check_speed())

    # stores sequence of key pressed
    keys = pygame.key.get_pressed()

    # player movement
    if keys[pygame.K_RIGHT] and playerRect.right <= surf_width:
        playerRect = playerRect.move(5, 0)
    if keys[pygame.K_LEFT] and playerRect.left >= 0:
        playerRect = playerRect.move(-5,0)

    # checks for ball boundaries within main window
    if ballRect.right >= surf_width or ballRect.left <= 0:
        ball_speed[0] = -(ball_speed[0])
    elif ballRect.top <= 0 or ballRect.bottom >= surf_height:
        ball_speed[1] = -(ball_speed[1])

    # check if player wins the game or loses
    if ballRect.bottom >= surf_height:
        Game_Over()
    elif len(brickRecs) == 0:
        Winner()

    # ball and player collision
    if ballRect.colliderect(playerRect):
        ball_speed[1] = -(ball_speed[1])

    # ball and brick collision
    for brick in brickRecs:
        if ballRect.colliderect(brick):
            ball_speed[1] = -(ball_speed[1])
            brick_index = brickRecs.index(brick)
            del brickRecs[brick_index]
        window_surf.blit(brickSurf, brick)

    window_surf.blit(playerSurf, playerRect)
    window_surf.blit(ballSurf, ballRect)
    pygame.display.update()

pygame.quit()
