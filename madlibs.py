from random import choice
from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module; Flask wants
# to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    print "loading index page"
    # return "Hi! This is the home page."
    return render_template("index.html")

# route to display a simple web page
@app.route('/hello')
def say_hello():
    print "running say_hello"
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    print "running greet_person"
    player = request.args.get("person")
    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']
    compliment = choice(AWESOMENESS)
    return render_template("game_question.html", person=player, compliment=compliment)

@app.route('/gameURL')
def show_game_question():
    print "show_game_question running"
    if request.args.get("play_yes") == "True":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")

@app.route('/madlib')
def show_madlibs():
    print "show_game_form running"
    nam = request.args.get("person")
    col = request.args.get("favcolor")
    adj = request.args.get("adjective")
    nou = request.args.get("noun")
    return render_template("madlibs.html", 
        MLname=nam, 
        MLcolor=col, 
        MLadjective=adj, 
        MLnoun=nou)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
