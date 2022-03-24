# Create a Python list to store your grocery list
grocery_list = ["milk", "eggs", "bread", "peanut butter", "jelly" ]
# Print the grocery list

# Change "Peanut Butter" to "Almond Butter" and print out the updated list
grocery_list[grocery_list.index("peanut butter")] = "almond butter"
# Remove "Jelly" from grocery list and print out the updated list
grocery_list.remove("jelly")
# Add "Coffee" to grocery list and print the updated list
grocery_list.append("Coffee")
print(grocery_list)