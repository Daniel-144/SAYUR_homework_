"""
############## Problem  1 ####################
#Ask first friend the movies they like. Save it in a list
#Ask another friend the same question. If the movie is in the first friend's list,
#Print "You both like "name of the movie"
#Continue until there is at least 3 movies they both like
"""
# initializing a variable for storing a list
common_movies = []
movie_list = []
movie_count=0
i = False
while i is False:
    print("enter 1 to add movies in list else press any other keys")
    choice = int(input('enter your choice: '))

    # minimum number of movies should be 3 to check so if movie count is less than 2 then they have to add a movie even if their choice is no.
    if choice == 1 or movie_count <= 2:
        # ask for their favourite movie and store it in a list
        movies = input('enter any movie: ')
        movies = movies.lower()
        # use append to store the input of the user to the list
        movie_list.append(movies)
        movie_count+=1
    else:
        i = True
j = False
# initialize a variable to store the number of same movies
same_movies = 0
while j is False:
    # ask for  his/her favourite movie
    movie = input('enter any movie: ')
    movie = movie.lower()
    # check if the movie is present in the movie list
    if movie in movie_list:
        common_movies.append(movie)
        # increment the same_movie by 1
        same_movies += 1
    if same_movies >= 3:
        # print the common movies
        print(f'wow,you have {common_movies[0]},{common_movies[1]},{common_movies[2]} movies in common')
        j = True
    else:
        print(f'you have  {same_movies} movies in common ')
        print('try again')
print(f'common movies are {common_movies[0]},{common_movies[1]},{common_movies[2]}')

"""
OP
enter 1 to add movies in list else press any other keys
enter your choice: 1
enter any movie: YOUR NAME
enter 1 to add movies in list else press any other keys
enter your choice: 2
enter any movie: CHARLIE
enter 1 to add movies in list else press any other keys
enter your choice: 1
enter any movie: JERSEY
enter 1 to add movies in list else press any other keys
enter your choice: 1
enter any movie: PURSUIT OF HAPPYNESS
enter 1 to add movies in list else press any other keys
enter your choice: 2
enter any movie: SAW
you have  0 movies in common 
try again
enter any movie: shawshank redemption
you have  0 movies in common 
try again
enter any movie: charlie
you have  1 movies in common 
try again
enter any movie: jersey
you have  2 movies in common 
try again
enter any movie: pursuit of happyness
wow,you have charlie,jersey,pursuit of happyness movies in common
common movies are charlie, jersey, pursuit of happyness
"""