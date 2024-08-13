class Entry:
  content = "something"

  def __init__(self,name, property1, property2):
    self.name = name
    self.property1 = property1
    self.property2 = property2

  def __str__(self):
    return self.name