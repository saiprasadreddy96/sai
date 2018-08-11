'''
Exercise : Assignment-1
implement the function get_available_letters that takes in one parameter -
a list of letters, letters_guessed. This function returns a string
that is comprised of lowercase English letters - all lowercase English letters
that are not in letters_guessed
'''
def get_available_letters(letters_guessed):
    '''
    :param letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    s_s = "abcdefghijklmnopqrstuvwxyz"
    l_l = []
    l_l = list(s_s)
    for char in letters_guessed:
        if char in l_l:
            l_l.remove(char)
    return ''.join(l_l)
def main():
    '''
    Main function for the given program
    '''
    user_input = input()
    user_input = user_input.split(" ")
    data = []
    for char in user_input:
        data.append(char)
    print(get_available_letters(data))
if __name__ == "__main__":
    main()