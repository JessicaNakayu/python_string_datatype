# TODO Create Variables
#   - Create the following variables
#   - my_first_name
#       -set this equal to your first name

my_first_name = 'Jessica'

#   - my_last_name
#       -set this equal to your last name

my_last_name = 'Nakayu'

#   - my_year_of_birth
#       -set this equal to your birth year (doesn't have to be real should be less then 100 yrs ago)

my_year_of_birth = 1995

#   - current_year
#       -set this equal to 2020

current_year = 2023




# TODO String Indexing
#   - Print the following items (one per line) (print using variables)
#       - first name  
print(my_first_name)
#       - last name
print(my_last_name)
#       - first letter of your first name (use the +index)
print(my_first_name[0])
#       - second letter of your last name (use the -index)
print(my_last_name[-5])
#       - first two letter of your first name (use the +index)
print(my_first_name[0,1])
#       - second two letter of your last name (use the -index)




#TODO Combining Strings
#   - Print the following items (one per line) (print using variables)
#       -first name and last name combined
#       -first name six times





# TODO Formatting Strings
#   - Print the following items (one per line) (print using variables)
#       - first name last name -was born in- year of birth
#       - first name last name -was born in- year of birth. first name -enjoyed celebrating- current year



# TODO Escape characters
#   - Print the following items (one per line) (print using variables)
#       - possesive first name -birth year is- year of birth 
print(my_first_name + '\'s' + " birth year is " + str(my_year_of_birth))

#       - tab last name current year
print("\t", my_last_name, current_year)



# TODO String methods
#   - Print the following items (one per line) (print using variables)
#       - first name and last name in lower case
print(my_first_name.casefold(), my_last_name.casefold())
#       - length of last name
print(len(my_last_name))
#       - first name and last name all in upper case
print(my_first_name.upper(), my_last_name.upper())