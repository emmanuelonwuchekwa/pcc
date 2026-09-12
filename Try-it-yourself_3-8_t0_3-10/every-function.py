Languages = ['French', 'German', 'Spanish', 'Swahili', 'English']
newList = []
mountains = ['Mount Olive', 'Mount Camel', 'Mount Zion', 'Mount Eevereste.']
rivers = ['Niger', 'Benue', 'Atlantic']
for x in Languages:
    newList.append(x) # adds each item to the newList
print(newList) # prints the list with all the items from the list of languages.
for i in mountains:
    newList.append(i) # adds each item from the mountains list to the newList.
print(newList) # shows the items from mountains has been added.
for r in rivers:
    newList.append(r) # appends every value in the rivers list.
print(newList) # shows the current state of the list.
print(sorted(newList)) # shows a temporary sorted version of the list.
print(sorted(newList, reverse=True)) # shows the list in reverse.
