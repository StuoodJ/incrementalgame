# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
text_font = pygame.font.SysFont(None, 30)
sW = 600
sH = 400
screen = pygame.display.set_mode((sW, sH))
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")

    #/
    from text import drawtext
    drawtext(screen, "Yes", text_font, (255,255,255), 220, 150)
    #/
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
