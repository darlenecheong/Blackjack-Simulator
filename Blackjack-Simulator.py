#import random functions
import random

#create lists of cards and its values
cards  = ['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts', '5 of Hearts', '4 of Hearts', '3 of Hearts', '2 of Hearts', 'Ace of Hearts', 'King of Hearts', 'Queen of Hearts', 'Jack of Hearts', '10 of Diamonds', '9 of Diamonds', '8 of Diamonds', '7 of Diamonds', '6 of Diamonds', '5 of Diamonds', '4 of Diamonds', '3 of Diamonds', '2 of Diamonds', 'Ace of Diamonds', 'King of Diamonds', 'Queen of Diamonds', 'Jack of Diamonds', '10 of Clubs', '9 of Clubs', '8 of Clubs', '7 of Clubs', '6 of Clubs', '5 of Clubs', '4 of Clubs', '3 of Clubs', '2 of Clubs', 'Ace of Clubs', 'King of Clubs', 'Queen of Clubs', 'Jack of Clubs', '10 of Spades', '9 of Spades', '8 of Spades', '7 of Spades', '6 of Spades', '5 of Spades', '4 of Spades', '3 of Spades', '2 of Spades', 'Ace of Spades', 'King of Spades', 'Queen of Spades', 'Jack of Spades']
values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10]

#function: restart
#input: call function
#function: print header
#output: header after each game restarts
def restart():
    print("================================ START ================================")

#function: player
#input: call function
#function: player's turn = choose 2 random cards and delete them from decks, ask user to hit or stand
#output: results of player's hand and total card value
def player():

    #select random card from list 'cards'
    card1 = random.choice(cards)

    #find index of card1
    card1_index = cards.index(card1)

    #find value of card1 in list 'values'
    card1_value = values[card1_index]

    #delete card1 and card1 value from lists 'cards' and 'values', respectively
    del cards[card1_index]
    del values[card1_index]

    #select another random card from list 'cards'
    card2 = random.choice(cards)

    #find index of card2
    card2_index = cards.index(card2)

    #find value of card2 in list 'values'
    card2_value = values[card2_index]

    #delete card2 and card2 value from lists 'cards' and 'values', respectively
    del cards[card2_index]
    del values[card2_index]

    #create accumalator to track total value of player's cards
    total_value = 0

    #set end to "notyet"
    end = "notyet"

    #create empty list to store future cards
    playerhand = []

    #enter while loop to start game
    while end != "Bust!":

        #call 'restart' function
        restart()

        #update total value by adding to accumalator 'total_value"
        total_value += card1_value
        total_value += card2_value

        #append card1 and card2 to 'playerhand' list
        playerhand.append(card1)
        playerhand.append(card2)

        #print player's hand and the value of their hand
        print("Player hand: ", playerhand, "is worth", total_value)

        #if player's score is 21, player wins and exit loop
        if total_value == 21:
            print("Player got 21! Blackjack!")
            print("Player wins.")

        #if player score is above 21, computer wins and exit loop
        elif total_value > 21:
            print("Bust!")
            print("Computer wins!")
            end == "Bust!"

        #if player score is below 21, enter another while loop
        elif total_value < 21:
            while True:

                #promt user to see if they want to hit (another card) or stand (with their current hand)
                h_or_s = str.lower(input("(h)it or (s)tand? "))

                #if player chooses to hit:
                if h_or_s == "h":

                    #generate another random card from list 'cards'
                    newcard = random.choice(cards)

                    #find index of newcard
                    newcard_index = cards.index(newcard)

                    #find value of newcard in list 'values'
                    newcard_value = values[newcard_index]

                    #delete newcard and its value from the lists 'cards' and 'values', respectively
                    del cards[newcard_index]
                    del values[newcard_index]
                    
                    #update total_value by adding to the accumulator
                    total_value += newcard_value

                    #append newcard to 'playerhand' list
                    playerhand.append(newcard)

                    #print the newcard that player drew
                    print("You drew", newcard)

                    #print updated playerhand and total_value
                    print("Player hand: ", playerhand, "is worth", total_value)

                    #if resulting total_value is above 21, computer wins, exit loop
                    if total_value > 21:
                        print("Bust!")
                        print("Computer wins!")
                        end == "Bust!"
                        break

                    #if resulting total_value is 21, player wins, exit loop
                    elif total_value == 21:
                        print("Player got 21! Blackjack!")
                        print("Player wins.")
                        break

                    #if resulting total_value is below 21, continue loop
                    elif total_value < 21:
                        continue

                #if user chooses to stand:
                else:

                    #if total_value is above 21, computer wins, exit loop
                    if total_value > 21:
                        print("Bust!")
                        print("Computer wins!")
                        end == "Bust!"

                    #if total_value is 21, player wins, exit loop
                    elif total_value == 21:
                        print("Player got 21! Blackjack!")
                        print("Player wins.")

                    #if total_value is below 21, initiate computer's turn by breaking loop
                    elif total_value < 21:
                        break
        break


#function: computer
#input: call function
#function: computers's turn = choose 2 random cards and delete them from decks, continually hitting
#output: results of computer's hand and total card value, and winner
def computer():
    print()

    #generate random choice from list 'cards' and store it as a variable
    compcard1 = random.choice(cards)

    #locate index of compcard1
    compcard1_index = cards.index(compcard1)

    #find value of compcard1 in list 'values' using its index
    compcard1_value = values[compcard1_index]

    #delete compcard1 and its value from list 'cards' and 'values', respectively
    del cards[compcard1_index]
    del values[compcard1_index]

    #generate another random choice from list 'cards' and store it as a variable
    compcard2 = random.choice(cards)
    
    #locate index of compcard2
    compcard2_index = cards.index(compcard2)

    #find value of compcard2 in list 'values' using its index
    compcard2_value = values[compcard2_index]

    #delete compcard2 and its value from list 'cards' and 'values', respectively
    del cards[compcard2_index]
    del values[compcard2_index]

    #create accumalator to track total value of computer's cards
    comptotal_value = 0

    #set compend to "notyet"
    compend = "notyet"

    #create empty list to store computer's future cards
    comphand = []

    while compend != "Bust!":

        #update total value by adding to accumalator 'comptotal_value"
        comptotal_value += compcard1_value
        comptotal_value += compcard2_value

        #append compcard1 and compcard2 to list 'comphand'
        comphand.append(compcard1)
        comphand.append(compcard2)

        #print comphand and total_value of computer's cards
        print("Computer hand: ", comphand, "is worth", comptotal_value)

        #if computer's score is worth 21, computer wins, exit loop
        if comptotal_value == 21:
            print("Computer got 21! Blackjack!")
            print("Computer wins.")

        #if computer's score is above 21, player wins, exit loop
        elif comptotal_value > 21:
            print("Bust!")
            print("Player wins!")
            compend == "Bust!"

        #if computer's score is below 21, enter while loop
        elif comptotal_value < 21:
            while True:

                #generate another random choice from list 'cards' and store it as a variable
                compnewcard = random.choice(cards)

                #locate index of compnewcard
                compnewcard_index = cards.index(compnewcard)

                #locate value of compnewcard in list 'values' using its index
                compnewcard_value = values[compnewcard_index]

                #delete compnewcard and its value from lists 'cards' and 'values', respectively
                del values[compnewcard_index]
                del cards[compnewcard_index]

                #update computer total value by adding to accumalator comptotal_value    
                comptotal_value += compnewcard_value

                #print out result of new card drawn
                print("Computer drew", compnewcard)

                #append compnewcard to comphand
                comphand.append(compnewcard)

                #print out comphand and its total worth
                print("Computer hand :", comphand, "is worth", comptotal_value)

                #if computer's score is above 21, player wins, exit loop
                if comptotal_value > 21:
                    print("Bust!")
                    print("Player wins!")
                    compend == "Bust!"
                    break

                #if computer's score is 21, computer wins, exit loop
                elif comptotal_value == 21:
                    print("Computer got 21! Blackjack!")
                    print("Computer wins.")
                    break

                #if computer's score is below 21, continue loop (continually hitting)
                elif comptotal_value < 21:
                    continue

        break
    return

#call player() and computer() functions to start game
player()
computer()
