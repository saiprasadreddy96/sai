'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
def dict_fun(hand):
    d = {}
    for i in range(len(hand)):
        if hand[i][0] in d:
            d[hand[i][0]] +=1
        else:
            d[hand[i][0]] = 1
    return d
def is_fourofakind(hand):
    dict_four = {}
    dict_four = dict_fun(hand)
    return len(dict_four) == 2 and 1 in dict_four.values() and 4 in dict_four.values()
def is_fullhouse(hand):
    dict_full = {}
    dict_full = dict_fun(hand)
    return len(dict_full) == 2 and 2 in dict_full.values() and 3 in dict_full.values()
def is_threeofakind(hand):
    dict_three = {}
    dict_three = dict_fun(hand)
    return len(dict_three) == 3 and 3 in dict_three.values() 
def is_twopair(hand):
    dict_twopair = {}
    dict_twopair = dict_fun(hand)
    return len(dict_twopair) == 3 and 2 in dict_twopair.values()
def is_onepair(hand):
    dict_onepair = {}
    dict_onepair = dict_fun(hand)
    return len(dict_onepair) == 4 and 2 in dict_onepair.values()
def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    
    my_dict = {'T':10,'J':11,'Q':12,'K':13,'A':14}
    l = []
    for i in range(len(hand)):
        if hand[i][0] in my_dict:
            l.append(int(my_dict[hand[i][0]]))
        else:
            l.append(int(hand[i][0]))
    minimum = min(l)
    for i in range(len(l)):
        if minimum not in l:
            return 0
        minimum += 1
    return 1
def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    face_val=[]
    count=0
    for i in range(len(hand)-1):
        if hand[i][1]==hand[i+1][1]:
            count=count+1
    if count==len(hand)-1:
        return 1
    else:
        return 0


def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    if is_straight(hand) and is_flush(hand):
        return 9
    if is_fourofakind(hand):
        return 8
    if is_fullhouse(hand):
        return 7
    if is_flush(hand):
        return 6
    if is_straight(hand):
        return 5
    if is_threeofakind(hand):
        return 4
    if is_twopair(hand):
        return 3
    if is_onepair(hand):
        return 2
    return 1

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    #return max(hands,key=hand_rank)
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
    #print(is_straight(['8D', '9D', 'TS', 'JC']))
    #print(is_fourofakind(['AD', 'AH', 'AC', '2S', 'TD']))

            

    
