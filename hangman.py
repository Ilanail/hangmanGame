def hangman_photo(): #1
    """this function shows the opening screen of the game.
    :param hangman:HANGMAN_ASCII_ART
    :type hangman: str
    :return: hangman ascii art and max tries
    :rtype: str and int"""
    HANGMAN_ASCII_ART = ("""  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/""")

    MAX_TRIES = 6
    print(HANGMAN_ASCII_ART, MAX_TRIES)


def choose_word(file_path, index):#2
    """this function gets a file path to text file from the user and index that is an integer which representing a
    particular word placement in the file.
    :param file_path: file path to the text file
    :param index: the index number of a specific word in the file
    :type file_path: str
    :type index: int
    :return: the word the player has to guess
    :rtype:str"""
    int_index = int(index)
    reading_file = (open(file_path, "r")).read()
    word_list = reading_file.split(" ")
    final_index = (int_index-1) % len(word_list)
    secret_word = (word_list[final_index])
    return secret_word

def check_win(secret_word, old_letters_guessed):#8
    """the function checks if all the letters in the secret word already guessed.
    :param secret_word: the word to guess
    :param old_letters_guessed: the letters that already guessed
    :type secret_word:str
    :type old_letters_guessed:list
    :return: true of false
    :rtype: str
    """
    secret_word_list = list(secret_word)
    check_list = []
    for letter in old_letters_guessed:
        if letter in secret_word:
            check_list.append(letter)
    if len(check_list) == len(secret_word_list):
        return True
    else:
        return False



def hangman_photos(wrong_tries):#3
    """the function prints 7 different situations of hangman.
    :param wrong tries: the num of wrong guesses
    :type wrong_tries: num
    :return: Askii string
    :rtype: str"""

    HANGMAN_PHOTOS = {

            'picture_0': (r"x-------x"),

            'picture_1': (r"""

            x-------x
            |
            |
            |
            |
            |
            """),
            'picture_2': (r"""
            x-------x
            |       |
            |       0
            |
            |
            |
            """),

            'picture_3': (r"""

            x-------x
            |       |
            |       0
            |       |
            |
            |
            """),

            'picture_4': (r"""

            x-------x
            |       |
            |       0
            |      /|\
            |
            |
            """),

            'picture_5': (r"""
            x-------x
            |       |
            |       0
            |      /|\
            |      /
            |
            """),

            'picture_6': (r"""
            x-------x
            |       |
            |       0
            |      /|\
            |      / \
            |
            """)}
    if wrong_tries == 0:
        print(HANGMAN_PHOTOS['picture_0'])
    elif wrong_tries == 1:
        print(HANGMAN_PHOTOS['picture_1'])
    elif wrong_tries == 2:
        print(HANGMAN_PHOTOS['picture_2'])
    elif wrong_tries == 3:
        print(HANGMAN_PHOTOS['picture_3'])
    elif wrong_tries == 4:
        print(HANGMAN_PHOTOS['picture_4'])
    elif wrong_tries == 5:
        print(HANGMAN_PHOTOS['picture_5'])
    elif wrong_tries == 6:
        print(HANGMAN_PHOTOS['picture_6'])


def lines (secret_word):#4
    """the function replace letters of the secret word to a blank lines.
    :param secret_word: rhe secret word to guess
    :type secret_word: str
    :return: lines in len of the secret word
    :rtype: str"""

    one_word_string = secret_word
    correct_one_word_string=one_word_string[0:]
    lines_word=len(one_word_string)*('_ ')
    print(lines_word)



def show_hidden_word(secret_word, old_letters_guessed): #7
    """
    :param secret_word:the word the user need to guess
    :param old_letters_guessed:the letters the user already guessed
    :type secret_word: str
    :type old_letters_guessed: list
    :return: a string from letters and under scores according to the correct guesses.
    :rtype:str
    """
    list_secret = list(secret_word)
    secret_word_letters_list = []
    for letter in list_secret:
      if letter in old_letters_guessed:
          secret_word_letters_list.append(letter)
      else:
          secret_word_letters_list.append('_')
    secret_word_to_guess = ' '.join(secret_word_letters_list)
    print(secret_word_to_guess)
    if old_letters_guessed[-1] not in list_secret:
        return False


def check_valid_input(letter_guessed, old_letters_guessed):#5
    """the function is checking the letter input validation.
    :param letter_guessed: the present input letter
    :param old_letters_guessed: the letters that the user already guessed
    :type letter_guessed: str
    :type old_letters_guessed:list
    :return:the validation of the input, true or false
    :rtype: bool
    """
    if ((len(letter_guessed) > 1) or (not (letter_guessed.isalpha()))) or (old_letters_guessed.count(letter_guessed) >= 1):
        return (False)
    if ((len(letter_guessed) == 1) and (letter_guessed.isalpha()) and (old_letters_guessed.count(letter_guessed) == 0)):
        return (True)


def try_update_letter_guessed(letter_guessed, old_letters_guessed):#6
    """The function makes changes according to the correctness of the input.
    :param letter_guessed: user's input letter
    :param old_letters_guessed:list of letters that they are already guessed
    :return:true or false
    :rtype: bool
    """
    check_valid_input(letter_guessed, old_letters_guessed)
    if check_valid_input(letter_guessed, old_letters_guessed) == True:
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X\n"+'->'.join(sorted(old_letters_guessed)))
        return False


def main():
    """This function is for Hangman game.
    :return:win or lose
    :rtype: str
    """
    hangman_photo()
    file_path = input("Enter file path:" )
    index = input("Enter index:" )
    secret_word = choose_word(file_path, index)
    print("Let's start!")
    old_letters_guessed = []
    worng_tries = 0
    hangman_photos(worng_tries)
    lines(secret_word)#c
    while worng_tries < 6:
        letter_guessed = input("please enter a letter: ")
        if try_update_letter_guessed(letter_guessed, old_letters_guessed) == True:
            if show_hidden_word(secret_word, old_letters_guessed) == False:
                print(":(")
                worng_tries +=1
                hangman_photos(worng_tries)
        if check_win(secret_word,old_letters_guessed) == True:
            print("WIN")
            break
    if worng_tries == 6:
        print("LOSE")

if __name__ == '__main__':
 main()








