from database import Database

class Interface:
  
  def __init__(self):
    #self.database = database
    self.menu()

  def menu(self):
    done = False

    while not done:

      print('''
          1) add a new csv file.
          2) add entry to an existing csv file.
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
          self.saving_to_new_file()
        case 2:
          print(2)
        case 3:
          print(3)
        case 4:
          print("bye")
          done = True
        case _:
          print("invalid choice")

  def saving_to_new_file(self):
    filename = input("Pick a filename: ")
    try:
      new_database = Database(1,filename)
    except Exception as error_message:
      print(error_message)
    """
    When file already exists,
    error needs to go through 3 levels:
    1) FileCreation raises error,
    2) error is then passed to Database,
    3) then it is passed to an Interface.
    
    name = input("Pick a name: ")
    age = input("Pick an age: ")
    date = input("Pick a date: ")
    
    self.database.add_entry(name,age,date)
    print(self.database.test)
    print(self.database.entries)
    self.database.save_through_entries()
    #print(name + age + date)
    self.menu()
    """
