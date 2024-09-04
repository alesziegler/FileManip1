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
          self.saving_to_existing_file()
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
      new_database = Database(1, filename)

      name = input("Pick a name: ")
      age = input("Pick an age: ")
      date = input("Pick a date: ")

      #now initialize addition method od database object.
      
      new_database.save_to_csv(name, age, date)

    except Exception as error_message:
      print(error_message)

  def saving_to_existing_file(self):
    old_database = Database(2)
    print("There are following files: ")
    print(old_database.find_existing_files())

    #here should be a mechanism for picking a file. We need a setter?
    target_file = input(
    """
    Write a name of the file to which you 
    wish to save from the list above (without".csv"): 
    """)

    print(old_database.filename)

    old_database.filename = target_file

    print(old_database.filename)

    name = input("Pick a name: ")
    age = input("Pick an age: ")
    date = input("Pick a date: ")

    old_database.save_to_csv(name, age, date)
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
