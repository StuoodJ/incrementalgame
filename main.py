# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
text_font = pygame.font.SysFont(None, 30)
sW = 600
sH = 400
screen = pygame.display.set_mode((sW, sH))
time = pygame.time
clock = time.Clock()
#/variables
cash = 0
dt = 0
bX = 50
bY = 50
bW = 80
bH = 40
#/run
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    
    mousex, mousey = pygame.mouse.get_pos()
    #/drawtext
    from text import drawtext

    drawtext(screen, "Cash:", text_font, (255,255,255), 20, 20)
    drawtext(screen, str(cash), text_font, (255,255,255), 80, 20)
    
    #/buttons
    
    button = pygame.draw.rect(screen, (255,0,0), (bX, bY, bW, bH))
    drawtext(screen, "1+", text_font, (255,255,255), bX+30, bY+12.5)
    
    lM, MM, RM = pygame.mouse.get_pressed()
    
    if mousex >= bX and mousex <= bX+bW and mousey >= bY and mousey <= bY+bH:
        if lM is True:
            cash += 1
            time.delay(150)

    #/
    pygame.display.flip()

    dt = clock.tick(60) # limits FPS to 60

pygame.quit()
