from entry import Entry
import os.path

class Database:

  
  entries = []

  def __init__(self, file):
    #can file directli initialize FileCreation?
    self.file = file

  def add_entry(self,name,age,date):
    """
    for now use of this method can be suspended.
    Instead of through a list, saving will be directly to a file.
    """
    e = Entry(name,age,date)
    self.entries.append(e)

  def return_all(self):
    return self.entries

  def save(self,new_text):
    
    with open(self.file,"a") as x:
      x.write(new_text)

  def save_through_entries(self):
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
        with open(self.file, "a", encoding = "utf-8") as f:
          for e in self.entries:
            values = [e.name, str(e.age), e.date.strftime("%d.%m.%Y")]
            line = ";".join(values)
            f.write(line + "\n")
            
      else:
        print("this is not a csv")

  def save_to_csv(self, name, age, date):
    if not os.path.isfile(self.file):
      print("not file")
    else:
      print("ok")
      if self.file.endswith(".csv"):
        print("ok")
        with open(self.file, "a", encoding = "utf-8") as f:
          values = [name,age,date]
          line = ";".join(values)
          f.write(line + "\n")
    

  def load(self):
    pass
