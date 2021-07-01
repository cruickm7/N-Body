import pygame
G = 6.67408 * 10 ** -11
f = [[]]
d = [[]]
a == [[]]
dx = [[]]
xy = [[]]
iv = [[]]
x = []
y = []
def math():
    

pygame.init()   
screen = pygame.display.set_mode([500, 500])
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 40)
    pygame.display.update()
    #for steps in range(1000):
        
# Done! Time to quit.
pygame.quit()