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
          self.saving_to_new_file()
        case 2:
          self.saving_to_existing_file()
        case 3:
          print("not implemented")
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
      
      new_database.save_to_csv(name, age, date)

    except Exception as error_message:
      print(error_message)

  def saving_to_existing_file(self):
    old_database = Database(2)
    print("There are following files: ")
    print(old_database.find_existing_files())

    target_file = input(
  """
  Write a name of the file to which you 
  wish to save from the list above: 
  """)

    print(old_database.filename)

    old_database.filename = target_file

    print(old_database.filename)

    name = input("Pick a name: ")
    age = input("Pick an age: ")
    date = input("Pick a date: ")

    old_database.save_to_csv(name, age, date)
    
