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
    """
    ok, we need to make sure that file exists and is csv:
    import os.path
    if os.path.isfile(self.file):
      if self.file.endswith(".csv"):
        ...
      else:
        print("is not csv")
    else:
    print("is not file")
    """
    with open(self.file,"a") as x:
      x.write("something2")
    

  def load(self):
    pass
