class Interface:
  welcome = "this will be a menu"

  def __init__(self): #maybe get another class as a parameter?
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
        case 2:
          print(2)
        case 3:
          print(3)
        case 4:
          print("bye")
          done = True
        case _:
          print("invalid choice")
