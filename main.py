from entry import Entry as entry
from database import Database #as database
from interface import Interface #as interface
from file_creation import FileCreation
import os.path


print("Hello")

"""
Now we are in the stage where we can retain data from
one session, but by next session, file is rewritten.
So we need 
"""

Interface(Database("lets_roll.csv"))


