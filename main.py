from entry import Entry as entry
from database import Database #as database
from interface import Interface #as interface
from file_creation import FileCreation


print("Hello")

FileCreation("test")

FileCreation("test2")

#ok, we need to integrate class database in a way that its instance can handle file openings
"""
database_test = Database("test.txt")
database_test.save()
"""
with open("test.txt", "a") as f:
  f.write("\n somethin else")

"""
database_test = Database("/test.txt")
database_test.save()
"""
Interface()


