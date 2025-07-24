# Import namedtuple from collections
from collections import namedtuple

# Create the namedtuple: SpeciesDetails
SpeciesDetails = namedtuple('SpeciesDetails', ['species', 'sex', 'body_mass'])

# Create the empty list: labeled_entries
labeled_entries = []

# Iterate over the weight_log entries
for species, sex, body_mass in weight_log:
    # Append a new SpeciesDetails namedtuple instance for each entry to labeled_entries
    labeled_entries.append(SpeciesDetails(species, sex, body_mass))
    
print(labeled_entries[:5])


####################


# Iterate over the first twenty entries in labeled_entries
for entry in labeled_entries[:20]:
    # if the entry's species equals Chinstrap
    if entry.species == 'Chinstrap':
      # Print each entry's sex and body_mass seperated by a colon
      print(f'{entry.sex}:{entry.body_mass}')


####################