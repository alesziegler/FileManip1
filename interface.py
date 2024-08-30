class Interface:
  welcome = "this will be a menu"

  def __init__(self,database): #maybe get another class as a parameter?
    self.database = database
    self.database.file = ""#this is problematic
    self.menu()

  def menu(self):
    done = False

    while not done:

      print('''
          1) add entry to the database.
          2) show the whole database.
          3) load.
          4) quit.
        ''')
      choice = input("Pick what do you want to do: ")

      try:
        choice = int(choice)
      except ValueError:
        print("invalid choice")
        continue
        

      match choice:
        case 1:
          print("s")
          self.saving()
        case 2:
          print(2)
        case 3:
          print(3)
        case 4:
          print("bye")
          done = True
        case _:
          print("invalid choice")

  def saving(self):
    name = input("Pick a name: ")
    age = input("Pick an age: ")
    date = input("Pick a date: ")
    #ok, how to connect database with file here?
    #what about FileCreation? Probably each database should create one file,
    #so file creation should be connected with Database class?
    self.database.save_to_csv(name,age,date)
    print(name + age + date)
    self.menu()
    
