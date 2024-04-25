# https://excalidraw.com/#room=2307c59c384fd1f6acab,EUbwlMw3WMLAxozWJZ2LYg
from flask import Flask, render_template, request, redirect, url_for
import csv
from openai import OpenAI

client = OpenAI(api_key='')

app = Flask(__name__)

#--------------------------OPEN AI--------------------------------#
# Make sure to set up your API key

 # NEED TO PUT A KEY

# USING AI TO GET RESPONSE
def get_chatgpt_response(user_input, completions:int):
    response = client.completions.create(engine="gpt-3.5-turbo-instruct",    # choosing model of openai's AI
    prompt=user_input,                  # choosing what to use for prompting
    max_tokens=150,                     # limit the maximum response tokens
    temperature=1.0,                    # choosing temperature (more random/creative here)
    n=completions,                      # modifiable completion number
    best_of=3,                          # Generates n * best_of completions and returns the best n.
    echo=False,                         # Return the user's input in the response if set to True
    presence_penalty=0.5,               # higher value = more likely to introduce new topics
    frequency_penalty=0.5               # higher value = more likely to repeat information)
    choices = []
    for i in range(completions):
        choices.append(response.choices[i].text.strip())
    return choices

def info_about_movie(movie):
    user_input = 'Give me the following information about the movie '+movie+' in this way. director: director of the movie; year: year of movie, genre: genres of movie separete by come when there is more then one; rating: rating of the movie acordinng rotten tomatoes in percentage. If you do not know some of the answer, just put "None" in the corresponind subitem.'
    response = get_chatgpt_response(user_input, 1)
    movie_answer = [movie,0] 
    for answer in response[0].split('\n'):
        answer
        if 'director' in answer.lower():
            movie_answer.append(answer.split(':')[1].strip())
            movie_answer[1] = 1
        if 'year' in answer.lower():
            movie_answer.append(answer.split(':')[1].strip())
            movie_answer[1] = 1
        if 'genre' in answer.lower():
            movie_answer.append(answer.split(':')[1].strip())
            movie_answer[1] = 1
        if 'rating' in answer.lower():
            movie_answer.append(answer.split(':')[1].strip())
            movie_answer[1] = 1
    if movie_answer[1] == 1:
        user_input = 'Give me a short explanation about the movie '+movie+' maximo 100 words'
        response = get_chatgpt_response(user_input, 1)
        text_movie = response[0]
    return movie_answer, text_movie

 #--------------------------OPEN AI--------------------------------#  


@app.route('/')
def index():
    return render_template('index.html')    # call the website indesx.html

@app.route('/submit', methods=['POST'])     # return the input from the website index.html and call the function submit
def submit():
    name = request.form['name']
    name_error = True

    info_movie, text = info_about_movie(name)
    if info_movie[1] == 1:
        name_error = False
        return redirect(url_for('info', name=name, director=info_movie[2], year=info_movie[3], genre=info_movie[4], tomatoes=info_movie[5], text=text))

    return "Name not found"  # Return a response in case the movie information is not found


@app.route('/info/<name>/<director>/<year>/<genre>/<tomatoes>/<text>')
def info(name, director, year, genre, tomatoes, text):

    return render_template('info.html', name=name, director=director, year=year, genre=genre, tomatoes=tomatoes, text=text)  # call the website info.html and give it two variable entries (name, other_info)

if __name__ == '__main__':
    app.run(debug=True)


