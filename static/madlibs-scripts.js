
// Script to replace all the html in the form #msg-to-user, after Step #1.
    //Takes the name, and returns a greeting and asks to launch game.

function greetByName(evt){
    evt.preventDefault();
    console.log ("#1 is running");
    var url = "/greet?name=" + $("#name-field").val();
    $.get(url,function(result){
        $("#current-task").html(result + "<input type='radio' id='preference' name='play_yes' value='True' checked>Yes</input><input type='radio' name='play_yes' value='False'>No</input>");
        $("#hello").hide();
        $("#game").show();
    });
}
$("#hello").on('click',greetByName);



// Script to replace all the html in the form #msg-to-user, after Step #2.
    // Takes the user preference (to play or not to play), and then routes in 2 possible directions.
    // If gaming a game, will return the entire html text for the game in a string from the flask controller.

function toGameOrNot(evt){
    evt.preventDefault();
    console.log("#2 is running");
    // looks at both radio buttons, and filters by checked
    var user_preference = (jQuery("input[name=play_yes]")).filter(":checked");
    $.post("/gameURL", user_preference,function(result){
        console.log(result);
        $("#current-task").html(result);
    });
    $("#game").hide();
}

$("#game").on("click", toGameOrNot);



//TODO:  Script to replace all the html in the form #msg-to-user, after Step #3.
    //  take the inputs from the game, and return the complete Madlibs into the div #madlib.

