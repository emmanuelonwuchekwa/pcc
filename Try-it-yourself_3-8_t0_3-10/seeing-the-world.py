visit_locations = ['United Kingdom','UAE', 'Japan', 'Ethiopia'] # list of places i'd like to visit.
print(visit_locations) # output the original list
print(sorted(visit_locations)) # to output the sorted list without modifying the original
print(visit_locations) # to show the list is still in the original order.
print(sorted(visit_locations, reverse=True)) # printing the sorted list in reverse from Z-A
print(visit_locations) # to show the original list is not modified.
visit_locations.reverse() # to modify the order of the original list from Z-A.
print(visit_locations) # to show the new order of the list.
visit_locations.reverse() # to reverse the order of the list back to its previous order.
print(visit_locations) # to show the order has changed again.
visit_locations.sort() # to permanently sort list in alphabetical order from A-Z.
print(visit_locations)
visit_locations.sort(reverse=True) # to to permanently sort list in alphabetical order from Z-A.
print(visit_locations)