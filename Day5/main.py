import random_word_generator

def change_current_word_state(selected_word,current_word_state,character):
    modified_word_state = ""

    for i in range(len(selected_word)):
        if current_word_state[i] == "_" and selected_word[i] == character:
            modified_word_state += character
        else:
            modified_word_state += current_word_state[i]    

    return modified_word_state        


def input_character_in_word(selected_word, input_char, current_word_state, attempts_remaining):
    if input_char in selected_word:
        current_word_state = change_current_word_state(selected_word, current_word_state, input_char)
    else:
        attempts_remaining -= 1
    return current_word_state, attempts_remaining        

def print_current_state(current_word_state,attempts_remaining):

    """ printing current condition of user """
    
    print("Current State: ",end=" ")

    for i in current_word_state:
        print(i,end=" ")

    print("\tAttempts Remaining : {}".format(attempts_remaining))    

def check_game_status(selected_word,current_word_state,attempts_remaining):
    """ IF game has ended or not """

    if current_word_state == selected_word:
        print("You Won :D")
        return True
    elif attempts_remaining <= 0:
        print("You Loose :( Please! Try Again")
        print("Word was : {}".format(selected_word))
        return True

    return False        

def play_game(attempts=5):
    """ Main logic of our program """

    # generating a random word
    selected_word = random_word_generator.pick_random_word()

    # generating current state of the word
    current_word_state = "_"*len(selected_word)

    # attemps that are allowed
    attempts_remaining = attempts

    print_current_state(current_word_state,attempts_remaining)

    while True:
        input_char = input("Guess a charcter: ")
        print("")
        # check whether the input character is in selected word or not
        current_word_state, attempts_remaining = input_character_in_word(selected_word, input_char, current_word_state, attempts_remaining)
        
        print_current_state(current_word_state,attempts_remaining)

        game_ended = check_game_status(selected_word,current_word_state,attempts_remaining)

        if game_ended:
            break


if __name__ == "__main__":
    play_game()