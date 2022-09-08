# store/write movies in .txt file

# f = open("movies.txt", "w")
# f.write(str(dict))
# f.close()
    
# Menu promt for user to select there option
MENU_PROMPT = "\n Please select an option \n 'a' to add a movie \n 'm' to see your movies \n 'f' to find a movie by title \n 'q' to quit: "

# Store new movies from user input
movies = []

# Functions for program 

# Function to add movies to movies list
def add_movie():
    title = input("\nEnter a movie title: ")
    director = input("Enter the directors name: ")
    year = input("Enter the year the movie came out: ")

    movies.append({
        'title': title, 
        'director': director, 
        'year': year
    })

# Function to show movies
def show_movie():
    for movie in movies:
        print_movie(movie)

# Function that prints movie details if user selects 'm'
def print_movie(movie):
    print(f"\nTitle: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Year Released: {movie['year']}")

# Function to find movies in the stored movies list        
def find_movie():
    search = input("\nEnter a movie to search for: ")
    
    for movie in movies:
        if movie['title'] == search:
            print_movie(movie)
        else:
            print("\nError. Movie not found... Please try again.")
            
 
 # User options
user_options = {'a': add_movie, 'm': show_movie, 'f': find_movie}


# Function defining the menu selections
def menu():
    selection = input(MENU_PROMPT)

    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print("\nUnknown command, please try again.")
        
        selection = input(MENU_PROMPT)


# main
menu()
