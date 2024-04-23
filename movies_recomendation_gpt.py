import openai

# Make sure to set up your API key
openai.api_key = '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'

# USING AI TO GET RESPONSE
def get_chatgpt_response(user_input,reco_num_gpt, completions:int):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",    # choosing model of openai's AI
        prompt=user_input,                  # choosing what to use for prompting
        max_tokens=80*reco_num_gpt,                     # limit the maximum response tokens - taking 50 word for recomended movie
        temperature=1.0,                    # choosing temperature (more random/creative here)
        n=completions,                      # modifiable completion number
        echo=False,                         # Return the user's input in the response if set to True
        presence_penalty=0.5,               # higher value = more likely to introduce new topics
        frequency_penalty=0.5               # higher value = more likely to repeat information
    )
    choices = []
    for i in range(completions):
        choices.append(response.choices[i].text.strip())
    return choices

def select_movies_liked(list_movies_user,list_user_rating,movies_num):
     indices_of_5 = [i for i, x in enumerate(list_user_rating) if x == 5] # considerinf that list_user_rating are integer
     list_movies_liked = [list_movies_user[i] for i in indices_of_5]
     if len(indices_of_5) < movies_num:
        indices_of_4 = [i for i, x in enumerate(list_user_rating) if x == 4] # considerinf that list_user_rating are integer
        list_movies_liked += [list_movies_user[i] for i in indices_of_4]  
     return list_movies_liked

# running the whole thing (explain name main thing?)
if __name__ == '__main__':
    list_movies_user = ['the Grand Budapest Hotel', 'Wall-E', 'Armageddon', 'The Lobster', 'No', 'Parasite', 'Mad Max: Fury Road','Roma', 'The devil wears Prada']
    list_user_rating = [4, 4, 1, 3, 5, 5, 2,4, 1]
    movies_num = 10             # number of movies in my list of liked movies, in this case, the top 10 (just take note 4 and 5). If movies rating 5 is bigger that 10 it just collect the rating 5, otherwise also take the movies rating 4
    reco_num_gpt = 3            # number of recomended movies fromchat GPT
    
    list_movies_liked = select_movies_liked(list_movies_user,list_user_rating,movies_num)
    text_input = f"""
    Can you recommend me a list of {reco_num_gpt} new movies that I should watch based on the movies that I liked or loved?
    And also explain a little the reason, why should I like the recommended movies.
    This are the movies that I liked: {list_movies_liked}
    And this are all the movies that I already watched, so you do not give a recommended movie that I watched: {list_movies_user}

    """
    for i in get_chatgpt_response(text_input,reco_num_gpt, 1):
            print(i)
    #print(get_chatgpt_response(text_input, 1))