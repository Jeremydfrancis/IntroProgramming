"""
Jeremy Francis
2026_03_23
List Practice
"""

my_list = "A B C D E F G H".split()
# print out just the F
print(my_list[5])
# Print out the D E F G
print(my_list[3:7])
# print out the list in reverse order
print(my_list[::-1])
new_list = "J K L".split()
# Add new_list to my_list
my_list.extend(new_list)
# Insert the missing I
my_list.insert(8, "I")
print(my_list)
# Remve the letter E and assign it to a var named letter
letter = my_list.pop(4)
# Print the list without quotes commas and brackets
for i in my_list:
    print(i, end=" ")
