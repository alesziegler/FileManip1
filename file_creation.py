
class FileCreation:

  def __init__(self,file_name,file_suffix):
    self.file = file_name + "." + file_suffix
    try:
      file = open(self.file,"x")
      file.close()
    except FileExistsError:
      print("File already exists")