'''
- Enter 'a' to add a movie, 'l' to see movie list, 'f' to find a movie, and 'q' to quit.

Tasks:
[x]: Decide where to store movies
[x]: what is the format of a movie?
[x]: Show the user the main interface and get their input
[x]: Allow users to add movies
[x]: Find a movie
[x]: stop running the program when they type 'q'

'''

def menu():
    user_input  = input("Enter 'a' to add a movie, 'l' to see movie list, 'f' to find a movie, and 'q' to quit.")
    while(user_input!= 'q'):
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            list_movie()
        elif user_input == 'f':
            find_movie()
        user_input  = input("Enter 'a' to add a movie, 'l' to see movie list, 'f' to find a movie, and 'q' to quit.")  
    else:
        print('Thank You :)')

my_movie_list = ['Gadar','Indian','GOT','F&F']

def add_movie():
    movie_name = input('Please, Enter the name of movie to add: ')
    my_movie_list.append(movie_name)
    print(f'Sucessfully added {movie_name}')
    #menu()

def list_movie():
    print(my_movie_list)

def find_movie():
    finder = input('Please, enter a movie name to find ? ')
    if finder in my_movie_list:
        print(f'{finder} is present in your collection!!')
    else:
        print(f'{finder} isn\'t present in your collection.')

if __name__ == '__main__':
    menu()
