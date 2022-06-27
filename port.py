import pygame
import constants

class Port_mark(pygame.sprite.Sprite):
  def __init__(self, x, y, name):
    super(Port_mark, self).__init__()
    self.x = x
    self.y = y
		
    # Define the dimension of the port mark
    self.surf = pygame.Surface((15, 15))
		
    # Define the color of the surface using RGB color coding.
    self.surf.fill(constants.red)
    self.rect = self.surf.get_rect()

    self.font = pygame.font.Font('freesansbold.ttf', 12)

    self.port_name = self.font.render(name, True, constants.blue)
#    self.port_name = self.font.render(name, True, constants.green, constants.grey)
    self.textRect = self.port_name.get_rect()
    self.textRect.bottomleft = (x, y)

  def draw(self, screen):
    screen.blit(self.surf, (self.x, self.y))
    screen.blit(self.port_name, self.textRect)

class Dialog(pygame.sprite.Sprite):
  def __init__(self, name):
    super(Dialog, self).__init__()
    self.name = name
		
    # Define the dimension of the surface
    self.surf = pygame.Surface((constants.dialog_width, constants.dialog_height), flags=pygame.SRCALPHA)
		
    # Define the color of the surface using RGB color coding compined with alpha.
    R, G, B = constants.light_yellow
    alpfa = constants.dialog_alpha
    self.surf.fill((R, G, B, alpfa))
    self.rect = self.surf.get_rect()

    self.font = pygame.font.Font('freesansbold.ttf', 48)

    self.port_name = self.font.render(name, True, constants.green)
    self.textRect = self.port_name.get_rect()
    self.textRect.center = (constants.X/2, 50+(constants.Y-constants.dialog_height)/2)

  def get_dialog_coordinates(self):
    x1 = (constants.X-constants.dialog_width)/2
    y1 = (constants.Y-constants.dialog_height)/2
    x2 = x1 + constants.dialog_width
    y2 = y1 + constants.dialog_height

    return (x1, y1), (x2, y2)

  def inside_dialog(self, pos):
    x, y = pos
    (x1, y1), (x2, y2) = self.get_dialog_coordinates()
    if (x>x1) and (x<x2) and (y>y1) and (y<y2):
      return True
    else:
      return False

  def draw(self, screen):
    screen.blit(self.surf, ((constants.X-constants.dialog_width)/2, (constants.Y-constants.dialog_height)/2))
    screen.blit(self.port_name, self.textRect)
    
class Port:
  def __init__(self, name, size, x, y):
    super(Port, self).__init__()
    self.name = name
    self.size = size
    self.x = x
    self.y = y
    self.next = None
    self.size_x = 15
    self.size_y = 15
    self.port_mark=Port_mark(x, y, name)
    self.dialog=Dialog(name)

  def draw(self, screen):
    self.port_mark.draw(screen)

  def draw_dialog(self, screen):
    self.dialog.draw(screen)

  def inside_dialog(self, pos):
    return self.dialog.inside_dialog(pos)

  def collision(self, pos):
    x, y = pos
    if (x>self.x) and (x<self.x+self.size_x) and (y>self.y) and (y<self.y+self.size_y):
      return True
    else:
      return False

  def get_info(self):
    print("The port name is " + self.name + " and it can handle " + str(self.size) + " ships")

if __name__ == "__main__":
    p1 = Port("New York", 24, 100, 100)
    p1.get_info()
