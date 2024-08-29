from entry import Entry
import os.path

class Database:

  
  entries = []

  def __init__(self, file):
    self.file = file

  def add_entry(self, name, property1, property2):
    e = Entry(name, property1, property2)
    self.entries.append(e)

  def return_all(self):
    return self.entries

  def save(self,new_text):
    
    with open(self.file,"a") as x:
      x.write(new_text)

  def save_to_csv(self):
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
    if not os.path.isfile(self.file):
      print("not file")
    else:
      print("ok")
      if self.file.endswith(".csv"):
        print("ok")
      else:
        print("this is not a csv")
    

  def load(self):
    pass
