
// Script to replace all the html in the form #content_form, after Step #1.
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



// Script to replace all the html in the form #content_form, after Step #2.
    // Takes the user preference (to play or not to play), and then routes in 2 possible directions.
    // If gaming a game, will return the entire html text for the game in a string from the flask controller.

function toGameOrNot(evt){
    evt.preventDefault();
    console.log("#2 is running");
    // looks at both radio buttons, and filters by checked
    var user_preference = (jQuery("input[name=play_yes]")).filter(":checked");
    $.post("/gameURL", user_preference,function(result){
        $("#current-task").html(result);
    });
    $("#game").hide();
    $("#madlibs_submit").show();
    $("#clear").show();
}

$("#game").on("click", toGameOrNot);



// Script to replace all the html in the form #content_form, after Step #3.
    //  take the inputs from the game, and return the complete Madlibs into the div #madlib.

function madlibs_submit(evt){
    evt.preventDefault();
    console.log("#3 is running");
    // get form values & serialize, send to flask, get returned Matlab.
    var data = $("#content_form").serialize();
    $.post("/madlib", data, function(result){
        $("#madlib").html(result);
    });
    $("#re_do").show();
}

$("#madlibs_submit").on("click", madlibs_submit);



// Script to play again, with new mablibs input.

function madlibs_again(evt){
    evt.preventDefault();
    console.log("#4 is running");
    $("#madlib").empty();
    // Hide the re-do button.  Initiate game form.
    // var user_preference = (jQuery("input[name=play_yes]")).value("True");
    $.post("/gameURL", {"play_yes":"True"},function(result){
        $("#current-task").html(result);
    });
    $("#re_do").hide();

}

$("#re_do").on("click", madlibs_again);
