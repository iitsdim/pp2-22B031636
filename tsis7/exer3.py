# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    pygame.draw.circle(screen, "red", player_pos, 50)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_pos.y > 20:
        player_pos.y -= 20
    if keys[pygame.K_s] and player_pos.y + 20 < screen.get_height():
        player_pos.y += 20
    if keys[pygame.K_a] and player_pos.x > 20:
        player_pos.x -= 20
    if keys[pygame.K_d] and player_pos.x + 20 < screen.get_width():
        player_pos.x += 20

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()