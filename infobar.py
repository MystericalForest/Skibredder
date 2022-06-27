import pygame
import constants
import message

class Infobar(pygame.sprite.Sprite):
  def __init__(self):
    super(Infobar, self).__init__()
    self.message=None
		
    # Define the dimension of the port mark
    self.surf = pygame.Surface((constants.infobar_width, constants.infobar_height))
		
    # Define the color of the surface using RGB color coding.
    self.surf.fill(constants.light_blue)
    self.rect = self.surf.get_rect()

#    self.font = pygame.font.Font('freesansbold.ttf', 12)

#    self.port_name = self.font.render(name, True, constants.green, constants.grey)
#    self.textRect = self.port_name.get_rect()
#    self.textRect.bottomleft = (x, y)

  def set_message(self, message):
    self.message = message
    self.font = pygame.font.Font('freesansbold.ttf', 24)

    self.message_title = self.font.render(message.title, True, constants.grey)
    self.textRect = self.message_title.get_rect()
    self.textRect.topleft = (constants.infobar_x + constants.infobar_pan, constants.infobar_y + constants.infobar_pan)

  def has_message(self):
    return self.message is not None

  def draw(self, screen):
    screen.blit(self.surf, (constants.infobar_x, constants.infobar_y))
    if self.has_message():
      screen.blit(self.message_title, self.textRect)

class Info_Dialog(pygame.sprite.Sprite):
  def __init__(self):
    super(Info_Dialog, self).__init__()
    self.message=None
		
    # Define the dimension of the surface
    self.surf = pygame.Surface((constants.dialog_width, constants.dialog_height), flags=pygame.SRCALPHA)
		
    # Define the color of the surface using RGB color coding compined with alpha.
    R, G, B = constants.light_yellow
    alpfa = constants.dialog_alpha
    self.surf.fill((R, G, B, alpfa))
    self.rect = self.surf.get_rect()

    self.font = pygame.font.Font('freesansbold.ttf', 48)

    self.title = self.font.render("Info", True, constants.red)
    self.textRect = self.title.get_rect()
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

  def set_message(self, message):
    self.message=message
    self.title = self.font.render(self.message.title, True, constants.red)
    self.textRect = self.title.get_rect()
    self.textRect.center = (constants.X/2, 50+(constants.Y-constants.dialog_height)/2)

  def draw(self, screen):
    screen.blit(self.surf, ((constants.X-constants.dialog_width)/2, (constants.Y-constants.dialog_height)/2))
    screen.blit(self.title, self.textRect)
    
class Info:
  def __init__(self):
    self.infobar=Infobar()
    self.dialog=Info_Dialog()
    self.dialog_open = False
    self.message=None

  def draw(self, screen):
    self.infobar.draw(screen)
    if self.dialog_open:
      self.dialog.draw(screen)

  def set_message(self, message):
    self.message = message
    self.infobar.set_message(message)

  def inside_dialog(self, pos):
    return self.dialog.inside_dialog(pos)
        
  def close_dialog(self):
    self.dialog_open = False

  def collision(self, pos):
    x, y = pos
    x1 = constants.infobar_x
    y1 = constants.infobar_y
    x2 = x1 + constants.infobar_width
    y2 = y1 + constants.infobar_height
    if (x>x1) and (x<x2) and (y>y1) and (y<y2):
      return True
    else:
      return False

  def is_dialog_open(self):
    return self.dialog_open

  def clicked(self, pos):
    if self.is_dialog_open():
      if self.dialog.inside_dialog(pos) == False:
        self.close_dialog()
    else:
      if self.collision(pos) == True:
        self.dialog.set_message(self.message)
        self.dialog_open = True
