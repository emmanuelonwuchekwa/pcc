# WHITESPACES i.e. nonpriting characters:
print("Python") # output: python
print("\tPython") # using '\t' to add tab to the text.
print("Languages:\nPython\nC\nJavaScript") # use '\n' to add new line in a string.
print("Languages:\n\tPython\n\tC\n\tJavaScript") # '\n\t' tells python to move to a newline and start the newline with a tab

# Note that all this is done using a single line of code
# REMOVING WHITESPACES
favourite_language = ' python '
print(favourite_language.rstrip()) # remove whitespace from right side
print(favourite_language.lstrip()) # remove whitespace from left side
print(favourite_language.strip()) # remove whitesspace form left and right side.
print(favourite_language)
# to remove a whitespace permanently you associate the stripped value with the variable name
favourite_language = favourite_language.rstrip()
print(favourite_language)
favourite_language = favourite_language.lstrip()
print(favourite_language) 
favourite_language = ' python '
print(favourite_language)
favourite_language = favourite_language.strip() # removes whitespace from both sides permanently 
print(favourite_language)