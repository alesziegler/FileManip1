from entry import Entry as entry
from database import Database #as database
from interface import Interface #as interface
from file_creation import FileCreation


print("Hello")

FileCreation("test","txt")

FileCreation("test2","txt")

#ok, we need to integrate class database in a way that its instance can handle file openings

FileCreation("test5","csv")

database_integrated = Database(FileCreation("test6","csv"))

database_test = Database("test5.csv")
database_test.save_to_csv()
database_test.save("\n this is a new text")

"""
with open("test.txt", "a") as f:
  f.write("\n somethin else")


database_test = Database("/test.txt")
database_test.save()
"""
#Interface()


