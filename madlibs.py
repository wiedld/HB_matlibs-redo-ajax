from random import choice, randrange
from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module; Flask wants
# to know this to know what any imported things are relative to.
app = Flask(__name__)

#  TRYING TO MAKE A GLOBAL VARIABLE, to use in routes.  NOT WORKING!!!
#       use correct dictionary get method, based if request.method is "GET" or "POST".
# dict_process = {"GET": request.args.get, "POST": request.form.get}


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


@app.route('/greet', methods=["GET","POST"])
def greet_person():
    print "running greet_person"
    #use correct dictionary get method, based if request.method is "GET" or "POST".
    dict_process = {"GET": request.args.get, "POST": request.form.get}
    player = dict_process[request.method]("person")
    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']
    compliment = choice(AWESOMENESS)
    return render_template("game_question.html", person=player, compliment=compliment)


@app.route('/gameURL', methods=["GET","POST"])
def show_game_question():
    print "show_game_question running"
    dict_process = {"GET": request.args.get, "POST": request.form.get}
    if (dict_process[request.method])("play_yes") == "True":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")


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
