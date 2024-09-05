from entry import Entry
from file_creation import FileCreation
import os

class Database:
  """
  This class needs to be reworked:
  1) There will be one method starting a new file.
  2) another method continuing existing file.
  """
  
  entries = []

  def __init__(self, option, filename = None):
    #can file directly initialize FileCreation?
    #self.option = option
    self.__filename = filename
    self.__path = "Data container"
    match option:
      case 1:
        self.create_new_file()
      case 2:
        pass
    #print(self.file)
    #print(os.path.isfile(self.file))

  def create_new_file(self):
    
    try:
      new_file = self.__path +"/" + self.__filename
      FileCreation(new_file,"csv")
    except Exception as error_message:
      raise Exception(error_message)
      
  def find_existing_files(self):
    #path = "/Data container"
    result =""
    for file in os.listdir(self.__path):
      if file.endswith(".csv"):
        result += file + "\n"
    return result

  def save_to_csv(self, name, age, date):
    print("launch")
    print(name + age + date)
    print(self.__filename) #it is recognized as a string, not as a file?
    file = self.__path + "/" + self.__filename + ".csv"
    print(os.path.isfile(self.__filename))
    print(os.path.isfile(file))
    with open(file,"a",encoding = "utf-8") as f:
      values = [name,age,date]
      line = ";".join(values)
      f.write(line + "\n")

  @property
  def filename(self):
    return self.__filename
  
  @filename.setter
  def filename(self,f):
    self.__filename = f
    
    """
    with open(self.__filename + ".csv", "a") as f:
      values = ["fq","dq","fdf"]
      line = ";".join(values)
      f.write(line + "\n")
    
    
    print(name + age + date)
    print("we are here")
    print(self.file)
    if not os.path.isfile(self.file):
      print("not file")
      print(os.path.isfile(self.file))
    else:
      print("ok")
      if self.file.endswith(".csv"):
        print("ok")
        
    with open(self.__filename,"a", encoding = "utf-8") as f:
      values = [name,age,date]
      line = ";".join(values)
      f.write(line + "\n")
  """
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
    print("here1")
    print(self.file)
    print("here2")
    if not os.path.isfile(self.file):
      print(os.path.isfile(self.file))
      print("not file")
    else:
      print("ok")
      if self.file.endswith(".csv"):
        print("ok")
        with open(self.file, "w", encoding = "utf-8") as f:
          for e in self.entries:
            values = [e.name, str(e.age), e.date]
            line = ";".join(values)
            f.write(line + "\n")
            
      else:
        print("this is not a csv")

  


  def load(self):
    pass
