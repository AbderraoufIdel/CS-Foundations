# Create a list containing the names: baby_names
baby_names = ['Ximena', 'Aliza', 'Ayden', 'Calvin']

# Extend baby_names with 'Rowen' and 'Sandeep'
baby_names.extend(["Rowen", "Sandeep"])

# Find the position of 'Rowen': position
position = baby_names.index("Rowen")

# Remove 'Rowen' from baby_names
baby_names.pop(position)

# Print baby_names
print(baby_names)

#########################################################################################

# Create the list comprehension: baby_names
baby_names = [name[3] for name  in  records]
    
# Print the sorted baby names in ascending alphabetical order
print(sorted(baby_names))


