"""
A system that will tell you what to watch next based on the 
word vector similarity of the description of movies.
"""

import spacy

# Load the en_core_web_md model
nlp = spacy.load('en_core_web_md')


def similar_movie(description):
    """ This function takes an NLP processed description as input and returns the movie title
    and description of the most similar movie in the `movies` dictionary.

    Parameters:
    description: An NLP processed description to compare with movie descriptions.

    Returns:
    str: max_similarity_movie title
    str: max_similarity_description
    """
    # cast using the NLP model
    nlp_description = nlp(description)

    max_similarity = 0
    max_similarity_movie = ""
    max_similarity_description = ""

    # loop through each movie title and description in the movies dictionary
    # movie_title being the key and movie_description being the value
    for movie_title, movie_description in movies.items():
        # calculate the similarity score between the input description and the movie description
        similarity = nlp(movie_description).similarity(nlp_description)
        # if the current similarity score is higher than the previous max, update the max values
        if similarity > max_similarity:
            max_similarity = similarity
            max_similarity_movie = movie_title
            max_similarity_description = movie_description

    # return movie name and description with highest similarity
    return max_similarity_movie, max_similarity_description


# Create a dictionary to store movie titles (keys) and descriptions (values)
movies = {}

# open the movies.txt file and parse its contents into the 'movies' dictionary
with open('movies.txt', 'r') as file:
    for line in file:
        # remove whitespace and split via the colon
        parts = line.strip().split(":")
        # assign the key as the first part (i.e. Movie A)        
        key = parts[0].strip()
        # assign the description after colon as value
        value = parts[1].strip()
        # attach to dictionary
        movies[key] = value

# a movie description
description = """ Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.
"""

# call the function to find the most similar movie description
similar_movie_result = similar_movie(description)

# display the results of recommended movie and it's description
print(f"Movie title: {similar_movie_result[0]}")
print(f"Movie description: {similar_movie_result[1]}")
