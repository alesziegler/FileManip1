
from file_creation import FileCreation
import os

class Database:
  
  def __init__(self, option, filename = None):
    self.__filename = filename
    self.__path = "Data container"
    match option:
      case 1:
        self.create_new_file()
      case 2:
        pass
    
  def create_new_file(self):
    
    try:
      new_file = self.__path + "/" + self.__filename
      FileCreation(new_file,"csv")
    except Exception as error_message:
      raise Exception(error_message)
      
  def find_existing_files(self):
    result =""
    for file in os.listdir(self.__path):
      if file.endswith(".csv"):
        result += file.rstrip(".csv") + "\n"
    return result

  def save_to_csv(self, name, age, date):
    file = self.__path + "/" + self.__filename + ".csv"
    with open(file,"a",encoding = "utf-8") as f:
      values = [name.replace(";", " "),age.replace(";", " "),date.replace(";", " ")]
      line = ";".join(values)
      f.write(line + "\n")

  @property
  def filename(self):
    return self.__filename
  
  @filename.setter
  def filename(self,f):
    self.__filename = f
  
