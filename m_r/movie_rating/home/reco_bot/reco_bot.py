
dic_movies = {'Wall-E':4, 'Armageddon':1, 'The Lobster':3, 'No':5, 'Parasite':5,'Mad Max: Fury Road':2,'Roma':4, 'The devil wears Prada':2, 'the Grand Budapest Hotel':5}
import openai

# Make sure to set up your API key

openai.api_key = '' # NEED TO PUT A KEY

# USING AI TO GET RESPONSE
def get_chatgpt_response(user_input, completions:int):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",    # choosing model of openai's AI
        prompt=user_input,                  # choosing what to use for prompting
        max_tokens=300,                     # limit the maximum response tokens
        temperature=1.0,                    # choosing temperature (more random/creative here)
        n=completions,                      # modifiable completion number
        best_of=3,                          # Generates n * best_of completions and returns the best n.
        echo=False,                         # Return the user's input in the response if set to True
        presence_penalty=0.5,               # higher value = more likely to introduce new topics
        frequency_penalty=0.5               # higher value = more likely to repeat information
    )
    choices = []
    for i in range(completions):
        choices.append(response.choices[i].text.strip())
    return choices

# running the whole thing (explain name main thing?)
if __name__ == '__main__':
    list_movies_liked = ['No', 'the Grand Budapest Hotel', 'Wall-E', 'Parasite']
    list_all_movies_user =['the Grand Budapest Hotel', 'Wall-E', 'Armageddon', 'The Lobster', 'No', 'Parasite', 'Mad Max: Fury Road','Roma', 'The devil wears Prada']
    movies_num = 3
    text_input = f"""
    Can you recommend me a list of {movies_num} new movies that I should watch based on the movies that I liked or loved?
    And also explain a little the reason, why should I like the recommended movies.
    This are the movies that I liked: {list_movies_liked}
    And this are all the movies that I already watched, so you do not give a recommended movie that I watched: {list_all_movies_user}

    """
    for i in get_chatgpt_response(text_input, 1):
            print(i)
    #print(get_chatgpt_response(text_input, 1))
