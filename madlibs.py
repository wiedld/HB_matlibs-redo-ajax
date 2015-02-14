from random import choice, randrange
from flask import Flask, render_template, request, session, jsonify


# "__name__" is a special Python variable for the name of the current module; Flask wants
# to know this to know what any imported things are relative to.
app = Flask(__name__)



# route to handle the landing page of a website.
@app.route('/')
def start_here():
    # return "Hi! This is the home page."
    return render_template("index.html")



@app.route('/greet')
def greet_person():
    name = request.args.get("name")
    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']
    greeting =  """Hi %s! I think you're %s! \n 
        Do you want to play a game?""" % (name,choice(AWESOMENESS))
    return greeting


@app.route('/gameURL', methods=['POST'])
def show_game_question():
    answer = request.form.get("play_yes")
    print answer
    if answer == "True":
        game_or_goodbye = "play game!"
    else:
        game_or_goodbye = '<p>Sorry to see you go :( <br/> Come back and play soon, k?</p>'
    return game_or_goodbye


@app.route('/madlib', methods=["GET","POST"])
def show_madlibs():
    print "show_game_form running"
    # use correct dictionary get method, based if request.method is "GET" or "POST".
    dict_process = {"GET": request.args.get, "POST": request.form.get}
    name = dict_process [request.method] ("person")
    col = dict_process [request.method] ("favcolor")
    adj = dict_process [request.method] ("adjective")
    noun = dict_process [request.method] ("noun")
    num = dict_process [request.method] ("number")
    IDnum = str( randrange(1,4) )
    print IDnum
    print type(IDnum)
    return render_template("madlibs.html", 
        MLname=name, 
        MLcolor=col, 
        MLadjective=adj, 
        MLnoun=noun,
        MLnum=num,
        MLtemplateID = IDnum)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
