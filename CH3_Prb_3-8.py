# Chapter 3 problem 3.8 - practice
places = ['Germany', 'Finland', 'Ireland', 'philippines', 'switzerland']
print(places)

#printing the list without modifying the actual list
print(sorted(places))
print(f"actual list {places}")

#printing reverse order using sorted:
print(sorted(places,reverse=True))
print(f"list is not mutilated. here actual list: \n{places}")

#using reverse :
places.reverse()
print(f"reversed list: {places}")

#using reverse again:
places.reverse()
print(f"back to normal list: {places}")

#using sort:
places.sort()
print(f"sorted list: {places}")

#using sort to reverser alphabetical order:
places.sort(reverse=True)
print(f"Reverse alphabetical order: \n{places}")
