# Pair up the girl and boy names: pairs
pairs = zip(girl_names, boy_names)

# Iterate over pairs
for rank, pair in enumerate(pairs):
    # Unpack pair: girl_name, boy_name
    girl_name, boy_name = pair
    # Print the rank and names associated with each rank
    print(f'Rank {rank+1}: {girl_name} and {boy_name}')

##########################

# Create the normal variable: normal
normal = "simple"

# Create the mistaken variable: error
error = "trailing comma",

# Print the types of the variables
print(normal)
print(error)