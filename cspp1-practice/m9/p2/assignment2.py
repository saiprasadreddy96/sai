'''
Exercise: Assignment-2
Next, implement the function getGuessedWord that takes in two parameters
a string, secret_word, and a list of letters, letters_guessed. This function
returns a string that is comprised of letters and underscores, based on what
letters in letters_guessed are in secret_word. This shouldn't be too different from isWordGuessed!
'''
def get_guessed_word(secret_word, letters_guessed, i, var_l):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    if i == var_l:
        return secret_word
    if secret_word[i] not in letters_guessed:
        secret_word = secret_word[:i] + '_' + secret_word[(i+1):]
    return get_guessed_word(secret_word, letters_guessed, i+1, var_l)

def main():
    '''
    Main function for current assignment
    '''
    user_input = input()
    if user_input != "":
        data = user_input.split()
        secret_word = data[0]
    else:
        data = []
        secret_word = ""
    list1 = []
    for j in range(1, len(data)):
        list1.append(data[j])
    print(get_guessed_word(secret_word, list1, 0, len(secret_word)))

if __name__ == "__main__":
    main()
