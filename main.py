import pygame
import sys
import os

pygame.init()

# main game loop
def main():
    # Main Surface object
    dimension_main = width, height = (800, 600)
    window_surf = pygame.display.set_mode(dimension_main)
    # caption title
    pygame.display.set_caption("Breakers")

    # background
    bg = pygame.image.load(os.path.join('assets/',
                                        'background.png'))
    bg = pygame.transform.scale(bg, dimension_main)

    # player
    playerImg = pygame.image.load(os.path.join('assets/',
                                            'player.png'))
    playerImg = pygame.transform.scale(playerImg, (110,30))
    player_pos = playerX, playerY = 100, 500
    player = playerImg.get_rect(topleft=player_pos)

    # Ball
    ballImg = pygame.image.load(os.path.join('assets/',
                                             'ball.png'))
    ballImg = pygame.transform.scale(playerImg, (60, 60))
    ball_pos = ballX, ballY = 50, 60
    ball = ballImg.get_rect(topleft=ball_pos)

    while 1:

        window_surf.blit(bg, (0,0))

        # checks if user quits program with X box
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and player.right <= width:
            player = player.move(5,0)
        if keys[pygame.K_LEFT] and player.left >= 0:
            player = player.move(-5,0)


        window_surf.blit(playerImg, player)
        window_surf.blit(ballImg, ball)
        pygame.display.update()

    pygame.quit()

main()
