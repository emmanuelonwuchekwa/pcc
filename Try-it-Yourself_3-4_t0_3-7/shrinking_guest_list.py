guest_list = ['goodnes', 'mercy', 'femi']
print("Hello everyone, i've just been informed that a bigger table is available for the guests.")
guest_list.insert(0, 'john') # adding a new guest to the beginning of the list.
guest_list.insert(2, 'Emeka') # adding a new guest to the middle of the list.
guest_list.append('Abu') # adding a new guest to the end of the list.
# for x in guest_list: # using for loop to output a new invite message for each guest
#     print(f"{x.title()}, you are invited to the bigger table!")
print(guest_list)
# message to inform guests that i'm shrinking the list to two people.
print("Unfortunately i've just been informed that i can only invite 2 people to the new table.")

removed_guest_no_4 = "Emeka" 
removed_guest_no_3 = "mercy"
removed_guest_no_2 = "femi"
removed_guest_no_1 = "Abu"
removed_guest_list = [removed_guest_no_1, removed_guest_no_2, removed_guest_no_3, removed_guest_no_4] # this list is arranged so that it the message outputed matches the item that was removed frrom the list.
for x in removed_guest_list:
    guest_list.pop() # using this method will drop names on the list starting with the last guest name.
    # guest_list.remove(x) # or use this method to remove the current item being iterated from the list. 
    print(f"sorry {x.title()}, I can't invite you for dinner.") # output a message to announce the guest that has been removed from the new list.

print(guest_list)
for x in guest_list: # printing an invite message t0 the remaining guests on the list.
    print(f"Hi {x}, you are invited to the bigger dining table")


del guest_list[:] # removes the remaining items in the list.
print(guest_list) # should output an empty list