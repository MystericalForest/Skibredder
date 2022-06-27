# import the pygame module
import pygame
import engine
import constants

# import pygame.locals for easier
# access to key coordinates
from pygame.locals import *

# initialize pygame
pygame.init()

# Define the dimensions of screen object
screen = pygame.display.set_mode((constants.X, constants.Y))
clock = pygame.time.Clock()

# set the pygame window name
pygame.display.set_caption('Skibsredder')

# Game engine class
engine=engine.Engine()

# Variable to keep our game loop running
gameOn = True

# Our game loop
while gameOn:
  # for loop through the event queue
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse_presses = pygame.mouse.get_pressed()
      if mouse_presses[0]:
        engine.mouse_left_click(pygame.mouse.get_pos())
    # Check for KEYDOWN event
    elif event.type == KEYDOWN:
			
    # If the Backspace key has been pressed set
    # running to false to exit the main loop
      if event.key == K_BACKSPACE:
        gameOn = False
      elif event.key == K_SPACE:
        pass
				
      # Check for QUIT event
    elif event.type == QUIT:
      gameOn = False

  engine.draw(screen)

  # Update the display using flip
  pygame.display.flip()
  clock.tick(30)

pygame.quit()

