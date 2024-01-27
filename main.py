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
cash = 0
dt = 0
bX = 50
bY = 50
bW = 80
bH = 40
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    
    mousex, mousey = pygame.mouse.get_pos()
    #/
    from text import drawtext
    drawtext(screen, str(mousex), text_font, (255,255,255), 160, 150)
    drawtext(screen, str(mousey), text_font, (255,255,255), 220, 150)
    drawtext(screen, "Cash:", text_font, (255,255,255), 160, 250)
    drawtext(screen, str(cash), text_font, (255,255,255), 220, 250)
    
    button = pygame.draw.rect(screen, (255,0,0), (bX, bY, bW, bH))
    lM, MM, RM = pygame.mouse.get_pressed()
    if mousex >= bX and mousex <= bX+bW and mousey >= bY and mousey <= bY+bH:
        if lM is True:
            cash += 1

            
    #/
    pygame.display.flip()

    dt = clock.tick(60) # limits FPS to 60

pygame.quit()
