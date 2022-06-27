import ports, infobar, message
import pygame
import constants

class Engine:
  def __init__(self):
      self.clicks=0
      self.ports = ports.Ports()
      self.infobar = infobar.Info()
      self.dialog_open=False
      self.bg_image = pygame.image.load(r'kort.png')

  def mouse_left_click(self, pos):
      self.ports.clicked(pos)
      self.infobar.clicked(pos)
      self.clicks+=1
      if self.clicks>5:
          self.infobar.set_message(message.Message("New Message", "More text about this message", 2))

  def is_dialog_open(self):
      return self.ports.is_dialog_open()

  def draw(self, screen):
      screen.fill(constants.white)
      screen.blit(self.bg_image, (0, 0))
      self.ports.draw(screen)
      self.infobar.draw(screen)
      if (self.is_dialog_open()):
        self.ports.draw_dialog(screen)
