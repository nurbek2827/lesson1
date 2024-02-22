import pygame

pygame.init()

HEIGHT = 600
WIDTH = 800

oyna = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Runner")

FPS = pygame.time.Clock()

player_height = HEIGHT // 2
player_widht = WIDTH // 2

WHITE = (255, 255, 255)

player_x = 250
player_y = 250

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    player = pygame.draw.circle(oyna, WHITE, (player_x, player_y), 16)
    oyna.blit(oyna, player)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= 2
    if keys[pygame.K_d]:
        player_x += 2

    pygame.display.update()