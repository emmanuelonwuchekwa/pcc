first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" # using an f-string to hold the value of variables
print(full_name) 
print(f"Hello, {full_name.title()}!") # using the f-string to compose complete messages using information associated with variables, while also temporarily testing using .title() method without the curved braces.
message = f"Hello, {full_name.title()}!" # using f-string to compose a message and then assigning it to a variable.
print(message)

