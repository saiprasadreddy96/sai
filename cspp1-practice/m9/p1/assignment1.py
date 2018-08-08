'''
Exercise: Assignment-1
First, implement the function isWordGuessed that takes in two parameters -
a string, secret_word, and a list of letters, letters_guessed. This function
returns a boolean - True if secret_word has been guessed (ie, all the letters of
secret_word are in letters_guessed) and False otherwise.
'''
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    if secret_word == "":
        return 1
    if secret_word[0] in letters_guessed:
        return 1 * is_word_guessed(secret_word[1:], letters_guessed)
    return 0 * is_word_guessed(secret_word[1:], letters_guessed)
def main():
    '''
    Main function for the program
    '''
    user_input = input()
    if user_input != "":
        data = user_input.split(" ")
        secret_word = data[0]
    else:
        data = []
        secret_word = ""
    list1 = []
    for j in range(1, len(data)):
        list1.append(data[j])
    if is_word_guessed(secret_word, list1):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()
