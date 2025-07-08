## Chapter 02 ##

# Create review_one
review_one = """I really enjoy the courses,
and they are easy to fit into my busy schedule. 
I wish I had started using your platform sooner.
I'll be recommending you to my friends!!"""

# Create review_two
review_two = """One year ago, I was unsure of how to make progress in my career. 
Now, I work as a Prompt Engineer, and I can't thank you enough! 
Keep up the great work."""

# Print the two reviews individually
print(review_one)
print(review_two)

print("######END######")

most_popular_course = "Intro to Embeddings with the OpenAI API"

# Update the first word
most_popular_course = most_popular_course.replace("Intro", "Introduction")

# Swap spaces for underscores
most_popular_course = most_popular_course.replace(" ", "_")

# Change to lowercase
most_popular_course = most_popular_course.lower()

print(most_popular_course)

print("######END######")

# Create the playlist variable
playlist = [1, "Blinding Lights", 2, "One Dance", 3, "Uptown Funk"]

# Print the list
print(playlist)

print("######END######")

# Find the second song
print(playlist[3])

print(playlist[1::2])

print("######END######")

# Create the playlist dictionary
playlist = {"The Weeknd": "Blinding Lights", "Drake": "One Dance"}

# Print the playlist
print(playlist)

print("######END######")

# Print the song by Coldplay
print(playlist["The Weeknd"])

# Add a new song
playlist["Usher"] = "Yeah!"

# Print the songs in the playlist
print(playlist.values())

print("######End######")

# Create a tuple
q3_financials = (325780, 1041, 4271599)

# Print the tuple
print(q3_financials)

print("######End######")

hip_hop = ["Drake", "JAY-Z", "50 Cent", "Drake"]
hippy_set = {"dude","bruh"}
# Create a set
indie_set = set(hip_hop) 
print(indie_set, hippy_set)