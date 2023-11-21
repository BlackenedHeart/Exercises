# Define the list
my_list = [17, 38, 10, 25, 72]

# Sort and display the list
sorted_list = sorted(my_list)
print("Sorted list:", sorted_list)

# Add element 12 to the list and display the list
my_list.append(12)
print("List after adding 12:", my_list)

# Reverse and display the list
reversed_list = list(reversed(my_list))
print("Reversed list:", reversed_list)

# Display the index of element 17
index_of_17 = my_list.index(17)
print("Index of 17:", index_of_17)

# Remove element 38 and display the list
my_list.remove(38)
print("List after removing 38:", my_list)

# Display the sublist of the 2nd and 3rd element
sublist_2_3 = my_list[1:3]
print("Sublist of 2nd and 3rd elements:", sublist_2_3)

# Display the sublist from the beginning to the 2nd element
sublist_beginning_2 = my_list[:2]
print("Sublist from beginning to 2nd element:", sublist_beginning_2)

# Display the sublist of the 3rd element at the end of the list
sublist_3_to_end = my_list[2:]
print("Sublist of 3rd element at the end of the list:", sublist_3_to_end)

# Display the complete sublist of the list
complete_sublist = my_list[:]
print("Complete sublist:", complete_sublist)

# Display the last element using a negative subscript
last_element = my_list[-1]
print("Last element using negative subscript:", last_element)
