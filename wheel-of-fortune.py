import random

def wheel_spin():
    wheel_values = ["LOSE A TURN", "BANKRUPT", 800, 350, 450, 700, 300, 600, 5000, 600, 500, 300, 500, 800, 550, 400, 300, 900, 500, 300, 900, 600, 400, 300]
    choose_value = random.randrange(0,len(wheel_values))
    wheel_value = wheel_values.pop(choose_value)
    return wheel_value

with open("words_alpha.txt") as words:
    word_list = words.read().split()

print("Welcome to Wheel of Fortune!")

player_overall = {1:0, 2:0, 3:0}
vowels = "AEIOU"
round = 1

while round < 3:

    random_word = random.randrange(0,len(word_list))
    word = word_list.pop(random_word).upper()
    letters = list(word)
    current_word = list('_' * len(word))

    correct_guesses = []

    player_round = {1:0, 2:0, 3:0}

    solved = False
    while solved == False:

        for i in player_round:

            if solved == True:
                break

            print("-------- Player " + str(i) + " --------")

            print("Here is the word that needs to be guessed:")
            print(*current_word)
            print(word)

            turn = True
            while turn == True:

                main_prompt = input("Would you like to guess a word (W) or a consonant (C)? ").upper()

                if main_prompt == "WORD" or main_prompt == "W":
                    word_guess = input("What is the word? ").upper()

                    if word_guess == word:
                        print("Correct! You have won the round.")
                        max_bank = max(player_round, key=player_round.get)
                        player_overall[max_bank] += player_round[max_bank]
                        round += 1
                        turn = False
                        solved = True
                        break
                    
                    else:
                        print("That is not correct. Your turn is over.")
                        turn = False

                elif main_prompt == "CONSONANT" or main_prompt == "C":
                    spin_wheel = wheel_spin()
                    print("Spin amount: " + str(spin_wheel))

                    if spin_wheel == "BANKRUPT":
                        print("BANKRUPT! You lose all money from this round.")
                        player_round[i] = 0
                        print(player_round)
                        turn = False

                    elif spin_wheel == "LOSE A TURN":
                        print("You lose a turn!")
                        turn = False

                    else: 
                        consonant_guess = input("Choose a consonant: ").upper()
                            
                        if consonant_guess in vowels:
                            print("That is a vowel, you must buy vowels!")
                            
                        elif consonant_guess in word:
                            correct_guesses.append(consonant_guess)
                            current_word = [letter if letter in correct_guesses else '_' for letter in letters]
                            print(*current_word)
                            multiplier = word.count(consonant_guess)
                            player_round[i] += spin_wheel * multiplier
                            print("Scores: " + str(player_round))

                            blank_counter = current_word.count("_")
                            if blank_counter == 0:
                                max_bank = max(player_round, key=player_round.get)
                                player_overall[max_bank] += player_round[max_bank]
                                round += 1
                                turn = False
                                solved = True
                                break
                                
                            buy_vowel = input("Would you like to buy a vowel? Yes (Y) or No (N): ").upper()
                            if buy_vowel == "Y" or buy_vowel == "YES":
                                vowel = True

                                while vowel == True:

                                    if player_round[i] >= 250:
                                        vowel_guess = input("Choose a vowel: ").upper()
                                        player_round[i] -= 250

                                        if vowel_guess in word and vowels:
                                            correct_guesses.append(vowel_guess)
                                            current_word = [letter if letter in correct_guesses else '_' for letter in letters]
                                            print(*current_word)
                                            print("Scores: " + str(player_round))

                                            blank_counter = current_word.count("_")
                                            if blank_counter == 0:
                                                max_bank = max(player_round, key=player_round.get)
                                                player_overall[max_bank] += player_round[max_bank]
                                                round += 1
                                                vowel = False
                                                turn = False
                                                solved = True
                                                break

                                            buy_vowel = input("Good guess! Would you like to buy another vowel? Yes (Y) or No (N): ").upper()
                                            if buy_vowel == "N":
                                                vowel = False

                                        else:
                                            print("That letter is not in the word. Your turn is over.")
                                            vowel = False
                                            turn = False

                                    elif player_round[i] < 250:
                                        print("You do not have enough money to buy a vowel. You can guess the word or another consonant.")
                                        vowel = False

                            elif buy_vowel == "N" or buy_vowel == "NO":
                                vowel = False

                            else:
                                print("Please input Y or N!")
                                vowel = True
                            
                        else:
                            print("That letter is not in the word. Your turn is over!")
                            turn = False

                else:
                    print("Please type 'W' or 'C'.")

while round == 3:
    
    random_word = random.randrange(0,len(word_list))
    word = word_list.pop(random_word).upper()
    letters = list(word)

    vowels = "AEIOU"
    
    final_player = max(player_overall, key=player_overall.get)
    final_player_bank = player_overall[final_player]

    print("The player moving on to the final round is: " + str(final_player))
    print("The prize for winning the final round is an additional $10,000!")

    correct_guesses = ['R', 'S', 'T', 'L', 'N', 'E']
    current_word = [letter if letter in correct_guesses else '_' for letter in letters]
    print(*current_word)

    guess = 1
    while guess < 4:
        consonant_guess = input("Guess a consonant: ").upper()

        if consonant_guess in vowels:
            print("You cannot guess a vowel yet. Try again with a consonant!")

        elif consonant_guess in word:
            print("Nice job! Take another guess.")
            correct_guesses.append(consonant_guess)
            current_word = [letter if letter in correct_guesses else '_' for letter in letters]
            print(*current_word)
            guess += 1

        else:
            print("That letter is not in the word. Take another guess!")
            guess +=1

    while guess == 4:
        vowel_guess = input("Guess a vowel: ").upper()
        
        if vowel_guess in word:
            print("Nice job! That was your last letter guess.")
            correct_guesses.append(vowel_guess)
            current_word = [letter if letter in correct_guesses else '_' for letter in letters]
            print(*current_word)
            guess += 1
        
        else:
            print("That letter is not in the word.")
            guess += 1

    while guess == 5:
        word_guess = input("You now have 1 chance to guess the word: ").upper()
        
        if word_guess == word:
            print("You won the Wheel of Fortune! You win: $" + str(final_player_bank + 10000))
            guess +=1
            round +=1

        else:
            print("You did not guess correctly, you win: $" + str(final_player_bank))
            guess +=1
            round +=1
