
secret_word = "Giraffe"
Guess = ""
Guess_count = 0
Guess_limit = 3
out_of_guesses = False

while Guess != secret_word and not (out_of_guesses):
    if Guess_count < Guess_limit:
       Guess = input ("Enter Guess:  ")
       Guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print ("Out Of Guesses, YOU LOSE! ")

else:
    print ("YOU WIN! ")
