# store/write movies in .txt file

# f = open("movies.txt", "w")
# f.write(str(dict))
# f.close()
    
# Menu promt for user to select his option

MENU_PROMPT = "\n Please select an option \n 'a' to add a movie \n 'm' to see your movies \n 'f' to find a movie by title \n 'q' to quit: "

# Store new movies from user input
movies = []

title = input("Enter a movie title: ")
director = input("Enter the directors name: ")
year = input("Enter the year the movie came out: ")

movies.append({
    'title': title, 
    'director': director, 
    'year': year
})


# Functions for program 

def add_movie():
    pass


# main

selection = input(MENU_PROMPT)

while selection != 'q':
    if selection == 'a':
        pass
    elif selection == 'm':
        pass
    elif selection == 'f':
        pass
    else:
        print("\nUnknown command, please try again.")
        
    selection = input(MENU_PROMPT)

