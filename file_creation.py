
class FileCreation:

  def __init__(self,file_name):
    self.file = file_name + ".txt"
    try:
      file = open(self.file,"x")
      file.close()
    except FileExistsError:
      print("File already exists")