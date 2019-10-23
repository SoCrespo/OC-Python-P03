import sys, pygame
pygame.init()

size = 800, 800

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Labyrinthe Mac Gyver")

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True

while run:
    pygame.time.delay(20)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel :
       x -= vel
        
    if keys[pygame.K_RIGHT] and x < 600 - vel - width:
       x += vel 
       
    if keys[pygame.K_UP] and y > vel:
        y -= vel
        
    if keys[pygame.K_DOWN] and y < 600 - vel - height:
        y += vel
    
    screen.fill((0,0,0)) 
    pygame.draw.rect(screen, (255,0,0), (x, y, width, height))
    pygame.display.update()
             
pygame.quit()            