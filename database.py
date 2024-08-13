from entry import Entry


class Database:
  entries = []

  def __init__(self, file):
    self.file = file

  def add_entry(self, name, property1, property2):
    e = Entry(name, property1, property2)
    self.entries.append(e)

  def return_all(self):
    return self.entries

  def save(self):
    pass

  def load(self):
    pass
