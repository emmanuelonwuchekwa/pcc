guest_list = ['goodnes', 'mercy', 'femi']
print("Hello everyone, i've just been informed that a bigger table is available for the guests.")
guest_list.insert(0, 'john') # adding a new guest to the beginning of the list.
guest_list.insert(2, 'Emeka') # adding a new guest to the middle of the list.
guest_list.append('Abu') # adding a new guest to the end of the list.
for x in guest_list: # using for loop to output a new invite message for each guest
    print(f"{x.title()}, you are invited to the bigger table!")

