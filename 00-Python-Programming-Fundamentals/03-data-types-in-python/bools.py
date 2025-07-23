# Create an empty list
my_list = []

# Check the truthiness of my_list
print(bool(my_list))

# Append the string 'cookies' to my_list
my_list.append('cookies')

# Check the truthiness of my_list
print(bool(my_list))

#####################

# Use a for loop to iterate over the penguins list
for penguin in penguins:
  # Check the penguin entry for a body mass of more than 3300 grams
  if penguin["body_mass"] > 3300:
  	# Print the species and sex of the penguin if true
    print(f"{penguin['species']} - {penguin['sex']}")

#####################


# Check the truthiness of penguin_305_details sex key
if penguin_305_details["sex"]:
	# If true, check if sex is True and store it as sex_is_true
    sex_is_true = penguin_305_details["sex"] is True
    # Print the sex key's value and sex_is_true
    print(f"{penguin_305_details['sex']}: {sex_is_true}")

# Check the truthiness of penguin_305_details tracked key
if penguin_305_details["tracked"]:
	# If true, check if tracked is True and store it as tracked_is_true
    tracked_is_true = penguin_305_details["tracked"] is True
    # Print the tracked key and tracked_is_true
    print(f"{penguin_305_details['tracked']}: {tracked_is_true}")