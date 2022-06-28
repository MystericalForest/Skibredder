import port, goods

class Ports:
  def __init__(self):
    self.head = None
    self.dialog = False
    self.load_init()
    self.display_node = None

  def load_init(self):
    tmp=port.Port("New York", 20, 480, 280)
    tmp.append_wanted_goods(goods.Goods("Steel", 50))
    tmp.append_wanted_goods(goods.Goods("Wood", 50))
    tmp.append_goods_on_sale(goods.Goods("Coal", 10))
    tmp.append_goods_on_sale(goods.Goods("Textil", 30))
    self.append(tmp)
    print(self.head.goods_wanted[0].get_info())
    tmp=port.Port("London", 24, 850, 220)
    tmp.append_wanted_goods(goods.Goods("Oil", 100))
    tmp.append_wanted_goods(goods.Goods("Steel", 50))
    tmp.append_goods_on_sale(goods.Goods("Tools", 10))
    tmp.append_goods_on_sale(goods.Goods("Textil", 50))
    self.append(tmp)
    self.append(port.Port("Los Angeles", 18, 260, 350))
    self.append(port.Port("Shanghai", 32, 1470, 340))
    self.append(port.Port("Cape Town", 14, 950, 720))
    self.append(port.Port("Lima", 14, 450, 600))
    self.append(port.Port("Rio de Jeneiro", 14, 650, 600))
    self.append(port.Port("Melbourne", 14, 1600, 760))
    self.append(port.Port("Dekar", 14, 760, 450))
    self.append(port.Port("Mombai", 14, 1225, 430))
    self.append(port.Port("Rome", 14, 910, 285))
    self.append(port.Port("Beirut", 14, 1030, 335))
    self.append(port.Port("Basra", 14, 1100, 350))
    self.append(port.Port("Sankt Petersborg", 14, 1000, 180))

  def get_info(self):
    current_node=self.head
    while current_node is not None:
        current_node.get_info()
        current_node=current_node.next

  def append(self, port):
    if self.head is None:
        self.head = port
        return
    current_node=self.head
    while current_node.next is not None:
        current_node=current_node.next
    current_node.next = port

  def draw(self, screen):
    current_node=self.head
    while current_node is not None:
        current_node.draw(screen)
        current_node=current_node.next
        
  def close_dialog(self):
    self.display_node = None
    
  def get_dialog_coordinates(self):
    if self.display_node is not None:
      return self.display_node.get_dialog_coordinates()
    return
    
  def draw_dialog(self, screen):
    if self.display_node is not None:
      self.display_node.draw_dialog(screen)

  def is_dialog_open(self):
    return self.display_node is not None

  def clicked(self, pos):
    if self.is_dialog_open():
      if self.display_node.inside_dialog(pos) == False:
        self.close_dialog()
    else:
      current_node=self.head
      while current_node is not None:
          if current_node.collision(pos):
            self.display_node=current_node
          current_node=current_node.next
      if self.display_node is not None:
        self.display_node.generate_text()
      

