import route

class Routes:
  def __init__(self):
    self.head = None

  def get_info(self):
    current_node=self.head
    while current_node is not None:
        current_node.get_info()
        current_node=current_node.next
      
  def get_distance(self, port_1, port_2, fixed_direction=True):
    current_node=self.head
    while current_node is not None:
      if current_node.find(port_1, port_2, fixed_direction):
        return current_node.distance
      current_node=current_node.next
    return

  def append(self, route):
    if self.head is None:
        self.head = route
        return
    current_node=self.head
    while current_node.next is not None:
        current_node=current_node.next
    current_node.next = route
  
if __name__ == "__main__":
    import port
    routes = Routes()
    shanghai=port.Port("Shanghai", 32)
    los_angeles=port.Port("Los Angeles", 18)
    routes.append(route.Route(port.Port("New York", 20), port.Port("London", 24), 20))
    routes.append(route.Route(port.Port("London", 24), los_angeles, 24))
    routes.append(route.Route(los_angeles, shanghai, 18))
    routes.append(route.Route(shanghai, port.Port("Cape Town", 14), 32))
    routes.append(route.Route(port.Port("Cape Town", 14), port.Port("New York", 20), 14))
    routes.get_info()
    tmp=routes.get_distance(shanghai, los_angeles, False)
    if tmp:
      print(tmp)
    else:
      print("Not found")
    
