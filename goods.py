class Goods:
  def __init__(self, name, price):
    self.name = name
    self.price = price

  def get_info(self):
    return self.name + " : " + str(self.price) + " $$$"

if __name__ == "__main__":
    g1 = Goods("Steel", 36)
    print(g1.get_info())
