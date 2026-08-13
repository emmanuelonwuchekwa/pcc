# Avoiding syntax errors with strings
# syntax errors are the least specific type of error and can be annoying to find and resolve when writing code; but the editor highliting helps one easily find these errors while writing the program.
message = "One of Python's strengths is its diverse community." 
print(message) # here python recognises the apostrophy in the string
# message = 'One of Python's strengths is its diverser commnunity.' 
# here as you can already tell by the editors highlighting python does not recognise where the string stops, resulting in a syntax error.
print(message)
