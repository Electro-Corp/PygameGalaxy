import pygame
import star
import random
stars = []
"""star generation"""
(width, height) = (300, 300)
(pointx,pointy) = (width/2,height/2)
for i in range(300):
  x = random.randint(0,width)
  y = random.randint(0,height)
  z = random.randint(1,9)
  stare = star.star(x,y,z)
  stars.append(stare)
background_colour = (0,0,0)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Galaxy Sim')
running = True
zoom = 2
while running:
  pygame.display.flip()
  screen.fill(background_colour)
  mouseX,mouseY = pygame.mouse.get_pos()
  for star in stars:
    finalx = star.x+(mouseX/star.z_index)
    finaly = star.y+(mouseY/star.z_index)
    pygame.draw.circle(screen,(255,255,255),(finalx,finaly),zoom)
  for event in pygame.event.get():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_EQUALS]:
      zoom+=1
    if keys[pygame.K_MINUS]:
      zoom-=1
    if event.type == pygame.QUIT:
      running = False