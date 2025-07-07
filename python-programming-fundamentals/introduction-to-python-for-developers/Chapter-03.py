## Chapter 03 ##

# Check if September inflation is less than August inflation
if "inflation_september" < "inflation_august":
  print("Inflation decreased")

# Check if September inflation is more than August inflation
elif "inflation_september" > "inflation_august":
	print("Inflation increased")

# Confirm that they are equal
else:
    print("Inflation remained stable")

print("######END######")

min_num_beds = 2
min_sq_foot = 750
max_rent = 1900

# Check the number of beds
if "num_beds" < min_num_beds:
    print("Insufficient bedrooms")

# Check square feet
elif "sq_foot" <= min_sq_foot:
    print("Too small")

  
# Check the rent
elif "rent" > max_rent:
    print("Too expensive")

  
# If all conditions met
else:
    print("This looks promising!")

print("######END######")

user_ids = ["T42YG4KTK", "VTQ39IDQ0", "CRL11YUWX", 
            "K6Y5URXLR", "V4XCBER7V", "IOGQWC61K"]

# Loop through user_ids
for id in user_ids:
  # Print the user_id
  print(id)

print("######END######")

# Create the tickets_sold variable
tickets_sold = 0

# Create the max_capacity variable
max_capacity = 30

# Loop through a range up to and including max_capacity's value
for tickets in range(0, max_capacity):
  
  # Add one to tickets_sold in each iteration
  tickets_sold += 1
  
print("Sold out:", tickets_sold, "tickets sold!")

print("######END######")

# Loop through the dictionary's keys and values
for key, value in courses.items():
  
  # Check if the value is "AI"
  if value is "AI":
    print(key, "is an AI course")
  
  # Check if the value is "Programming"
  elif value is "Programming":
    print(key, "is a Programming course")
  
  # Otherwise, print that it is a "Data Engineering" course
  else:
    print(key, "is a Data Engineering course")

print("######END######")

tickets_sold = 0
max_capacity = 10

# Create a while loop
while tickets_sold < max_capacity:
  
  # Add one to tickets_sold in each iteration
  tickets_sold += 1

# Print the number of tickets sold
print("Sold out:", tickets_sold, "tickets sold!")

print("######END#######")

release_date = 26
current_date = 22

# Create a conditional loop while current_date is less than or equal to the release_date
while current_date <= release_date:
  
  # Promote purchases
  if current_date <= 24:
    print("Purchase before the 25th for early access")
  
  # Check if the date is equal to the 25th
  elif current_date == 25:
    print("Coming soon!")
  else:
    print("Available now!")
  
  # Increment current_date by one
  current_date += 1

print("######END#######")

authors = {"abderraouf": 26 , "idel" : 20}

# Create an empty list
authors_below_twenty_five = []

# Loop through the authors dictionary
for key, value in authors.items():
  
  # Check for values less than 25
  if value < 25:
    
    # Append the author to the list
    authors_below_twenty_five.append(key)
    
print(authors_below_twenty_five)

print("######END#######")

for genre, average_sale in genre_sales.items():
    
    # Filter for the maximum sales value
    if average_sale == 5166000000:
      
      # Print the genre
      print("Most popular genre: ", genre)
      print("Average sales: ", average_sale)
    
    # Filter for the minimum sales value
    elif average_sale == 80000000:
      
      # Print the genre
      print("Least popular genre: ", genre)
      print("Average sales: ", average_sale)

print("######END#######")

# Loop through the dictionary
for genre, sale in genre_sales.items():
  
  # Check if genre is Horror or Mystery
  if genre == "Horror" or genre == "Mystery":
    print(genre, sale)
  
  # Check if genre is Thriller and sale is at least 3 million
  elif genre == "Thriller" and sale >= 3000000 :
    print(genre, sale)