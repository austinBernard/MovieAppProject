# Menu promt for user to select there option
MENU_PROMPT = " \n 'a' to add a movie \n 'm' to see your movies \n 'f' to find a movie by title \n 'y' to see all movies in given year \n 'l' load past saved movies \n 's' to save current movies \n 'q' to quit \n Please select an option: "


movies = []


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
    
    
# Function to save movies into a .txt file
def save_movies():
    with open('movies.txt', 'a') as f:
        f.write(str(movies))
        print('\nSucessfully saved to movies.txt!')


# Function to load movies from a stored .txt file
def load_movie():
    with open('movies.txt', 'r') as f:
        pass
        
        
    
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
user_options = {'a': add_movie, 'm': show_movie, 'f': find_movie, 'y': movie_years, 's': save_movies, 'l': load_movie}


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


# Main
menu()


