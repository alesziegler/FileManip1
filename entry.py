class Entry:
  content = "something"

  def __init__(self,name,age,date):
    self.name = name
    self.age = age
    self.date = date

  def __str__(self):
    return self.name