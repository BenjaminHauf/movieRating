import openai
from .models import Rating


openai.api_key = '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'


# USING AI TO GET RESPONSE
def get_chatgpt_response(user_input, reco_num_gpt, completions:int):
    openai.api_key = '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 ' #'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'
    response = openai.Completion.create(engine="gpt-3.5-turbo-instruct", 
    prompt=user_input,
    max_tokens=80*reco_num_gpt,
    temperature=1.0,
    n=completions,
    echo=False,
    presence_penalty=0.5,
    frequency_penalty=0.5,
    stream = False)
    choices = []
    for i in range(completions):
        choices.append(response.choices[i].text.strip())
    return choices

def select_movies_liked(user):
    ratings = Rating.objects.filter(user=user, stars__gte=4)
    movies_liked = [rating.movie for rating in ratings]
    return movies_liked

def generate_recommendations(user, reco_num_gpt):
    movies_liked = select_movies_liked(user)
    movies_str = ', '.join([movie.title for movie in movies_liked])
    text_input = f"""
    Can you recommend me a list of {reco_num_gpt} new movies that I should watch based on the movies that I liked or loved?
    And also explain a little the reason, why should I like the recommended movies.
    This are the movies that I liked: {movies_str}
    """
    response = get_chatgpt_response(text_input, reco_num_gpt, 1)
    response_gpt = response[0].split('\n')
    return response_gpt

