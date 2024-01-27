def drawtext(screen, text, font, textCol, x, y):
    img = font.render(text, True, textCol)
    screen.blit(img, (x, y))