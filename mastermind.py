print "Content-type:text/html"
print ""


import cgi
import random
form = cgi.FieldStorage()



reds = 0
whites = 0


if "answer" in form:
    answer = form.getvalue("answer")
else:
    answer = ""
    for i in range(4):
        answer += str(random.randint(0,9))

if "guess" in form:
    guess = form.getvalue("guess")
    for key, digit in enumerate(guess):
        if digit == answer[key]:
           reds += 1
        else:
             for answerDigit in answer:
                 if answerDigit == digit:
                      whites += 1
                      break                      
    
else:
    guess = "" 
    
        
if "numberOfGuesses" in form:
    numberOfGuesses = int(form.getvalue("numberOfGuesses")) + 1
else: 
    numberOfGuesses = 0    
    

if numberOfGuesses == 0:
     message = "I've chosen a 4 digit number. Can you guess it?"
    
elif reds == 4:
     message = "Well done! You got in " + str(numberOfGuesses) + " guesses. <a href=''>Play again</a>"  
   
else:
    message = "You have " + str(reds) + " correct digit(s) in the right place, and " + str(whites) + " correct digit(s) in the wrong place. You have had " + str(numberOfGuesses) + " guess(es)."  

    
print '<body style="background-color:#fbe0c5"></body>'
print '<h1 style="font-size:30px; padding-left:15px">Mastermind Game</h1>'
print "<p style='font-size:18px; padding-left:15px'>" + message + "</p>" 
print '<form method="post">'
print '<input style="height:40px; width:150px; font-size:20px; margin-left:15px" type="text" name="guess" value="' + guess + '">'
print '<input type="hidden" name="answer" value="' + answer + '">'
print '<input type="hidden" name="numberOfGuesses" value="' + str(numberOfGuesses) + '">'
print '<input  style="height:40px; width:90px; font-size:20px" type="submit" value="Guess!">'
print '</form>'
print '<br></br>'
print '<h2 style="padding-left:15px">Instructions</h2>'
print '<p style="font-size:18px; padding-left:15px">Mastermind or Master Mind is a code-breaking game for two players.</p>'
print '<p  style="font-size:18px; padding-left:15px">Creating this game in python will be pretty simple. The computer will randomly create a 4 digit number(0-9 digits) and the player will try to guess the number untill he correctly guesses it.</p>'
print '<p style="font-size:18px; padding-left:15px">Rules:</p>'
print '<p style="font-size:18px; padding-left:15px">Player 1(Computer) sets a number.</p>'
print '<p style="font-size:18px; padding-left:15px">Player 2 starts guessing the number. It his first guess is correct, he is the mastermind.</p>'
print '<p style="font-size:18px; padding-left:15px">If the player 2 cannot guess the number, the game will continue until he guess the number correct.</p>'
print '<p style="font-size:18px; padding-left:15px">Depending on the efforts to find the numbers, a message appears above the form telling you how many correct digits (s) are in the right place, and how many correct digits (s) are in the wrong place.</p>'
print '<p style="font-size:18px; padding-left:15px">Enjoy !</p>'
print '<br></br>'
print '<a href="images/mastermind.png" target="_blank"> <img width="350px" src="images/mastermind.png" alt="mastermind" data-position="25% 25%" style="max-width: 100%;height: auto;vertical-align:middle;border-style: none;margin-left:50px"></a>'
print '<br></br>'
print '<a  style="font-size:15px; padding-left:100px" href="https://en.wikipedia.org/wiki/Mastermind_(board_game)" target="_blank">Mastermind (board game) - Wikipedia</a>'
print '<br></br>'