class Ship:
  def __init__(self, name, size):
    self.name = name
    self.size = size

  def get_info(self):
    print("The ships name is " + self.name)
    print("This ships can carry " + str(self.size) + " containers")

if __name__ == "__main__":
    s1 = Ship("John", 36)
    s1.get_info()
