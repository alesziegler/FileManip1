
class FileCreation:

  error_message = "File already exists0"

  def __init__(self,file_name,file_suffix):
    self.file = file_name + "." + file_suffix
    self.output()

  def output(self):
    try:
      file = open(self.file,"x")
      file.close()
      return self.file
    except FileExistsError:
      print("File already exists1")
      raise FileExistsError("n;d")
   

  
    
    
    