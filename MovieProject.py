# store/write movies in .txt file

# f = open("movies.txt", "w")
# f.write(str(dict))
# f.close()
    
# Menu promt for user to select there option
MENU_PROMPT = " \n 'a' to add a movie \n 'm' to see your movies \n 'f' to find a movie by title \n 'y' to see all movies in given year \n 'q' to quit \n Please select an option: "

# Store new movies from user input
movies = []

# Read from movies.txt the current stored movies
with open('movies.txt') as f:
    lines = f.readlines()

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
    search = input("Enter a movie to search for: ")
    
    for movie in movies:
        if movie['title'] == search:
            print_movie(movie)
        else:
            print("\nError. Movie not found... Please try again.")
            

# Function to select all movies within a given year
def movie_years():
    search_movie_years = input("Input a year to see all movies from given year: ")
    
    for movie in movies:
        if movie['year'] == search_movie_years:
            print_movie(movie)
        else:
            print("\nNo movies found for given year.")
    
 
 # User options
user_options = {'a': add_movie, 'm': show_movie, 'f': find_movie, 'y': movie_years}


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
#Fix this next update
with open('movies.txt', 'wb') as f:
    for wd in movies:
        f.write(wd)

