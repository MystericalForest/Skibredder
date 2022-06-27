class Route:
  def __init__(self, port_1, port_2, distance):
    self.port_1 = port_1
    self.port_2 = port_2
    self.distance = distance
    self.next = None

  def get_info(self):
    print("The distance between " + self.port_1.name + " and " + self.port_2.name + " is " + str(self.distance) + " steps")

  def find(self, port_1, port_2, fixed_direction=True):
    if (self.port_1==port_1) and (self.port_2==port_2):
      return True
    else:
      if (fixed_direction==False):
        if self.find_reverse(port_1, port_2):
          return True
    return False

  def find_reverse(self, port_1, port_2):
    if (self.port_1==port_2) and (self.port_2==port_1):
      return True
    else:
      return False
    
if __name__ == "__main__":
  import port
  r1 = Route(port.Port("New York",10), port.Port("London",15), 24)
  r1.get_info()
