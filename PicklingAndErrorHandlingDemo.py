# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with pickling and error handling. An example of how
#               pickling is used and an example of how error handling is used
#               is shown in this program.
# ChangeLog (Who,When,What):
# MDiaz,2.25.2023,Initial creation
# ---------------------------------------------------------------------------- #

# Import Modules ------------------------------------------------------------- #
import pickle

# Declare Variables ---------------------------------------------------------- #
# Pickling Example
animals = ["birds", "cows", "pigs"]  # A list of farm animals
dwelling = ["cage", "barn", "pen"]  # A list of farm animal dwellings
food = ["seed", "grass", "feed"]  # A list of farm animal food

# Error Handling Example
file_name = "NonexistentFile.txt"  # A nonexistent file name to demonstrate error handling
table_lst = []  # A list that acts as a 'table' of rows

# Pickling Example ----------------------------------------------------------- #
# Store List Objects in Binary File
fileout = open('farm_info.dat', "wb")
pickle.dump(animals, fileout)
pickle.dump(dwelling, fileout)
pickle.dump(food, fileout)
fileout.close()

# Load List Objects from Binary File
filein = open('farm_info.dat', 'rb')
animals2 = pickle.load(filein)
dwelling2 = pickle.load(filein)
food2 = pickle.load(filein)

# Print Lists from New Variables
print(str(animals2)+"\n", str(dwelling2)+"\n", str(food2)+"\n")

# Error Handling Example ----------------------------------------------------- #

# Try/Except Example
try:  # Tries to open the file with name "NonexistentFile.txt"
    file = open(file_name, "r")
    file.close()
except FileNotFoundError:  # Adds provision for when no file exists yet
    print("File " + '"' + str(file_name) + '"' + " not found.")  # Notifies the user that the file was not found
