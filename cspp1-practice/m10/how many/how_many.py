#Exercise : how many
# write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary.


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count=0
    for i in aDict:
        count=count+len(aDict[i])
    return count
    

def main():
    aDict={}
    s=int(input())
    for i in range(s):
        l=input()
        l=l.split()
        if l[0][0] not in aDict:
            aDict[l[0][0]]=[l[1]]
        else:
            aDict[l[0][0]].append(l[1])
        
    print(how_many(aDict))


if __name__== "__main__":
    main()
