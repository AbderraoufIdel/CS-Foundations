# Import the Counter object
from collections import Counter

# Create a Counter of the penguins sex using a list comp
penguins_sex_counts = Counter(penguin["Sex"] for penguin in penguins)

# Print the penguins_sex_counts
print(penguins_sex_counts)


#################

# Import the Counter object
from collections import Counter

# Create a Counter of the penguins list: penguins_species_counts
penguins_species_counts = Counter(penguin["Species"] for penguin in penguins)

# Find the 3 most common species counts
print(penguins_species_counts.most_common(3))

#################