'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''

import re

# helper function to load the stop words from a file
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords

def remove_stop_words(word_list):
    stop_words = load_stopwords("stopwords.txt")

    temp_word_list = word_list[:]

    for each_word in temp_word_list:
        if each_word in stop_words:
            word_list.remove(each_word)

    return word_list

def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    text = text.lower()
    text_list = text.split(" ")
    count = 0
    while count < len(text_list):
        text_list[count] = re.sub("[^a-z]","",text_list[count])
        count += 1
    return text_list
    
def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''

    # initialize a search index (an empty dictionary)

    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop

        # clean up doc and tokenize to words list

        # add or update the words of the doc to the search index

    # return search index
    #index = {word: [(doc_id, frequency)]}
    index = {}
    for i in range(len(docs)):
        docs[i] = word_list(docs[i])
        
    for i in range(len(docs)):
        docs[i] = remove_stop_words(docs[i])
    
    for i in range(len(docs)):
        for j in range(len(docs[i])):
            if docs[i][j] not in index:
                index[docs[i][j]] = [(i,1)]
            else:
                flag = 0
                for k in range(len(index[docs[i][j]])):
                    if index[docs[i][j]][k][0] == i:
                        flag = 1
                        index[docs[i][j]][k][1] += 1
                        break
                if flag == 0:
                    index[docs[i][j]].append((i,1))
    return index
                    
                    
# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1

    # call print to display the search index
    print_search_index(build_search_index(documents))
if __name__ == '__main__':
    main()
