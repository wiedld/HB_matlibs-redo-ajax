from random import choice, randrange
from flask import Flask, render_template, request, session, jsonify
import json


app = Flask(__name__)



# Starting index.html asks for the user's name.
@app.route('/')
def start_here():
    return render_template("index.html")


# Greets the user by name, assign an AWESOME factor. 
# Ask if want to play game.
@app.route('/greet')
def greet_person():
    name = request.args.get("name")
    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']
    greeting =  """Hi %s! I think you're %s! \n 
        Do you want to play a game?""" % (name,choice(AWESOMENESS))
    return greeting


# based on user response, gives either goodbye or AJAX in the game.
@app.route('/gameURL', methods=['POST'])
def show_game_question():
    answer = request.form.get("play_yes")
    if answer == "True":
        file_obj = open("./static/game.txt")
        game_list=[]
        for row in file_obj.readlines():
            game_list.append(row.rstrip("\n"))
        game_string = "</br>".join(game_list)
        game_or_goodbye = game_string
    else:
        game_or_goodbye = '<p>Sorry to see you go :( <br/> Come back and play soon, k?</p>'
    return game_or_goodbye


# Takes the posted data (serialized in js file), places in dict 
#  and returns with Madlib text + a button to refresh with new dict.
@app.route('/madlib', methods=['POST'])
def show_madlibs():
    name = request.form.get("person")
    col = request.form.get("favcolor")
    adj = request.form.get("adjective")
    noun = request.form.get("noun")
    num = request.form.get("number")
    print ("this should be the color:",col)

    madlib_dict = {
        "MLname": name,
        "MLcolor": col, 
        "MLadjective": adj, 
        "MLnoun": noun,
        "MLnum": num
        }
    
    madlib = "<p>There once was a l33t programmer named "+ madlib_dict['MLname'] +",<br /> who had "+ madlib_dict['MLnum'] +" cats and a dog. <br /> Although many found her "+ madlib_dict['MLadjective'] +", she was <br /> better described as the "+ madlib_dict['MLnoun'] +". <br /> Fortunately, this was not a problem.  Because the <br /> instructor, who had a "+ madlib_dict['MLcolor'] +" nose, was <br /> even more extremely "+ madlib_dict['MLadjective'] +".</p>"

    return madlib



if __name__ == '__main__':
    app.run(debug=True)

