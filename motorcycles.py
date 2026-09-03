motorcycles = ['honda', 'yamaha', 'suzuki'] # a list of motorcycles
print(motorcycles)

# to mordify the first item on the already created list:
motorcycles[0] = 'ducati' # assign a new value to the first index.
print(motorcycles) # output the mordified list.

# Appending elements to the end of a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati') # adds the new element to the end of the list.
print(motorcycles)

# using .Append() method to dynamically build lists
empty_motorcyles_list = []
empty_motorcyles_list.append('honda')
empty_motorcyles_list.append('yamaha')
empty_motorcyles_list.append('suzuki')
print(empty_motorcyles_list)

# using the .insert() method
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducatzi') # using the first parameter to specify the index you want to modify; you can add values to any part of your list.
print(motorcycles)

# Removing items according to their position or value.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0] # removing the first item 'honda' from the list.
print(motorcycles)

# Removing items using the pop() method
motorcycles = ['honda', 'yamaha', 'suzuki'] # arranged in chronological order lets remove the last bike we purchased and output a statement with it
last_owned = motorcycles.pop() # this removes the last value from the list and saves it in the last owned variable.
print(f"The last motorcycle I owned was the {last_owned.title()}") # this outputs a message with the value stored in the last owned variable.

# you can pop items from a list using their index number
first_owned = motorcycles.pop(0) # this removes the first value in the list with the index zero. 
print(f"the first motorcycle I owned was the {first_owned.title()}") # using the poped valued in a statement

