# Create a dictionary for a film
film = {
    "Title": "Inception",
    "Director": "Christopher Nolan",
    "Year": 2010,
    "Genre": "Science Fiction",
    "Rating": 8.8
}

# Display film details using a loop
print("Film Details:")
for key, value in film.items():
    print(f"{key}: {value}")
