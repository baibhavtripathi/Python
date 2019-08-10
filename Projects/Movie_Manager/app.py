# Project // Movie Manager // Summer 2k19
"""
- Enter 'a' to add a movie, 'l' to show all movies, 'f' to find a movie, 'q' to quit:
- Add movies
- See movies
- Find a movie
- Stop running the program

Tasks:
[x]: Decide where to store movies
[x]: What is the format of a movie?
[x]: Show the user the main interface and get their input
[x]: Allow user to add movies
[x]: Show all their movies
[x]: find a movie
[x]: Stop running the program when they type 'q'

"""

movie_list = [
    {
        'Movie_Name':'Sanju',
        'Year':2018,
        'Type':'Biography'
    },
    {
        'Movie_Name':'Race 3',
        'Year':2018,
        'Type': 'Action'
    },
    {
        'Movie_Name':'Aladdin',
        'Year':2019,
        'Type': 'Comedy'
    },
    {
        'Movie_Name':'Avengers',
        'Year':2018,
        'Type':'Action'
    },
    {
        'Movie_Name':'Mama',
        'Year':2014,
        'Type':'Horror'
    },
    {
        'Movie_Name':"Harry Potter",
        'Year':2003,
        'Type':'Drama'
    },
]

def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to show all movies, 'f' to find a movie, 'q' to quit : ")
    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movie_list(movie_list)
        elif user_input == 'f':
            find_a_movie()
        else:
            print('Invalid input, try again')
        user_input = input("Enter 'a' to add a movie, 'l' to show all movies, 'f' to find a movie, 'q' to quit : ")
    else:
        print('\n Thank You for using. \n')

def add_movie():
    movie_list.append(
                {
                    'Movie_Name': input('Movie name : '),
                    'Year': int(input('Enter year : ')),
                    'Type': input("Movie Type : ")
                }
            )

def show_movie_list(movie_coll):
    for movie in movie_coll:
        print(movie)


def find_a_movie():
    findby = input('Enter a movie\'s property :: "Movie_Name" , "Year" or "Type" to get the movie : ')
    looking_for = input('What you\'r searching for : ')

    found_movies = finder_by_attribute(movie_list, looking_for, lambda x : x[findby])
    show_movie_list(found_movies)



def finder_by_attribute(movies,expected,finder):
    found = []

    for movie in movies:
        if finder(movie) == expected:
            found.append(movie)
    
    return found

# Driver 
if __name__ == '__main__':
    menu()
