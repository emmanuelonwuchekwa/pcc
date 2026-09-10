# using the sort() method to order a list permanently.
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # orders the list permanently
print(cars)
# sorting the list in reverse order from Z-A
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True) # the reverse=True argument sorts the list in reverse.
print(cars)

# sorting a list temporarily with the sorted() function.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"Here's the original list:\n{cars}") # shows the list in its original order.
print(f"\nHere's the sorted list:\n{sorted(cars)} ") # temporarily sorts and shows the ordered version of the original list.
print(f"\nHere's the original list again\n{cars}") # outputs the original list showing the previous sorting was temporal.
# NOTE sorted() method can also take the reverse=True argument.


