guest_list = ['goodnes', 'mercy', 'favour'] # list of people i want to invite for a dinner
# ouput and invite for each person inviting them for dinner.
print(f'{guest_list[0].title()}, you are invited for dinner')
print(f'{guest_list[1].title()}, you are invited for dinner')
print(f'{guest_list[2].title()}, you are invited for dinner')
print(f'unfortunately {guest_list[2].title()} could not make it!')
new_guest = 'femi' # name of the new guest
guest_list[2] = new_guest # swapping the position of the guest that didn't make it with the new guest.
# new set of invitation for the people still in my list 
print(f'{guest_list[0].title()}, you are invited for dinner')
print(f'{guest_list[1].title()}, you are invited for dinner')
print(f'{guest_list[2].title()}, you are invited for dinner')
