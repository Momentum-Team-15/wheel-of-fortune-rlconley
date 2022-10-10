from webbrowser import get

def create_board(word):
    print(f"This is the create_board function and the value of `word` is {word}")
    board_list = []
    for letter in word:
        board_list.append("_")
    print(f"Here is your word to guess: {' '.join(board_list)}")
    return board_list


# def show_board(word):   
    # TODO display _ or letter depending on guesses
    # This will use the lists of guesses


def get_user_guess():
    print("This is the get_user_guess function.")
    guess = input("Guess your letter: ")
    return guess

def play_game():
    # computer picks a word to guess.
    # start with one word
    # TODO pick word from list
    word_to_guess = 'dream'
    # Let the user know how many letters the secret word contains. Make the board that shows a blank for each letter
    game_board = create_board(word_to_guess)
    print(f'The value of game_board is {game_board}')
    correct_guesses = []
    print(f'The value of correct_guesses is {correct_guesses}')
    incorrect_guesses = []
    print(f'The value of incorrect_guesses is {incorrect_guesses}')
    # show_board(word_to_guess)
    new_guess = get_user_guess()
    print(f'The value of new_guess is {new_guess}')
    # TODO assess whether the guess was right or wrong
    # and put it in the appropriate list





if __name__ == "__main__":
    play_game()
