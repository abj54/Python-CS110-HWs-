## Anwesh Joshi
## HW 2
## scrabble.py

import sys
 
sys.setrecursionlimit(10000)  # Allows up to 10000 recursive calls;
                 #the maximum permitted ranges from system to system

scrabbleScores = [ ["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1],
                 ["f", 4], ["g", 2], ["h", 4], ["i", 1], ["j", 8],
                 ["k", 5], ["l", 1], ["m", 3], ["n", 1], ["o", 1], ["p", 3],
                 ["q", 10], ["r", 1], ["s", 1], ["t", 1], ["u", 1], ["v", 4],
                 ["w", 4], ["x", 8], ["y", 4], ["z", 10] ]


## Question 1
## Here we simply use "filter" to make our job easier from HW 1 to
## get a numeric value for the provided string from scorelist. And we
## also have to make sure that letter is in srabbleScores, if it's not
## we return 0


## I tested this function as:
## >>> letterScore("c", scrabbleScores)
## 3
## letterScore("a", scrabbleScores)
## 1
## >>> letterScore("2",scrabbleScores)
## 0
## >>> letterScore(42,scrabbleScores)
0

def letterScore(letter,scoreList):
    "'letter is the alphabet whose paired up numeric value is to be \
obtained from the scorelist'"
    if scoreList==[]:
        return 0
    elif letter in [x[0] for x in scoreList]:  #checking if letter is in
                                               # scoreList or not
        lettervalue=filter(lambda d: d[0]==letter,scoreList)
        return lettervalue[0][1]
    else:
        return 0





## Question 2
## Here I have used "map" and "reduce" to use the letterScore function
## even vastly so that the sum of all the paired up number of all the
## string from the word is returned. And we have to make sure that the
## word is not a number so we use typr function here.

## I tested this function as:
## wordScore('spam', scrabbleScores)
## 8
## wordScore("wow", [['o', 10], ['w', 42]])
## 94
## wordScore("538",scrabbleScores)
##0
## wordScore(538,scrabbleScores)
## 0


def wordScore(word,scoreList):
    "' word is a combination of strings from the list within scorelist \
such that the sum of all the numeric values paired up with those \
    strings are returned'"
    if  scoreList==[] or word=="":
        return 0
    elif type(word)==type(1): # if word is a interger, we return 0
        return 0
    else:
        val= map(lambda m:letterScore(m,scoreList),word)
        plus= reduce( lambda y,z: y+z,val)
        return plus
   
    
 




Dictionary = ["a", "am", "at", "apple", "bat", "bar", "babble", "can",
              "foo", "spam", "spammy", "zzyzva"]

## Question 3
## Here I am using List Comprehension to define terms variables and I have
## defined a length function two determine the length of word

def length(x):
    "'length will determine length of x, which might be string or list'"
    "'x is a word whose length is returned by this function'"
    if x:
        return 1 + length(x[1:])
    else:
        return 0

## for this length testing:
##length("sam")
## 3
##length([1,2,3])
## 3
    
## words is a list comprehension which will return all the words
## from list Dictionary
##>>> words
##['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo', 'spam',
##   'spammy', 'zzyzva']


words = [x for x in Dictionary]

## twoLetterWords will return all the words from Dictionary whose
## length is two
## >>> twoLetterWords
## ['am', 'at']

twoLetterWords= [x for x in Dictionary if length(x) == 2]

## lengths will return a list with length of all the words in list
## Dictionary
## lengths
##[1, 2, 2, 5, 3, 3, 6, 3, 3, 4, 6, 6]

lengths = [length(x) for x in Dictionary]




# Question 4
## for this problem, I had to take help from a lot of other functions including
## the ones I used in earlier homework with some modifications. I had to make sure
## that all the strings from the Rack made the possible strings and also returned
## the wordScore value for it


## rem function is simply used by me so that I can remove same letter x from any
## list to prevent any chance of letter repetition

## This function will work as:
## >>> rem("a",["a","b"])
## ['b']

def rem(x,list):
    "'x is any value which is to be removed from list just once'"
    if list==[]:
        return[]
    elif list[0]==x:
        return list[1:]
    else:
        return [list[0]]+rem(x,list[1:])




# this ind function is simply used to check how many letters from the given
# word matches in any list and keep a count of it as v, as soon as any letter
# from the word S is not in the list, value of v will know it

## I tested it as:
## >>> ind(["a","p","p","l","e"],"apple")
## 5
## >>> ind(["a","p","p","l","e"],"aple")
## 4
##>>> ind(["a","p","p","l","e"],"sapple")
## 0


def ind(LIST, S):
    "'LIST is a set of characters whereas S is a word and here we will find \
the total number of continious letters from S that matches in the list and \
is stored in parameter 'v''"
    v=0
    if S:
        if S[0] in LIST:
            return 1+v+ind(rem(S[0],LIST),S[1:]) # here rem is used to remove
                                     # the first letter found in the list from it
        else:
            return 0   #if any letter from word is not in list, we don't need that word
    else:
        return 0



##Question 4 (1)
## This is the main scoreList function that I have been working for.
## In this function, I have taken help from ind function above to check if that
## word is in dictionary or not. I compared the value of v with the length of word
## in Dictionary and if they match, they are truewords from Dictionary. Then I used
## map to list out those truewords with their wordScore from scrabbleScores

## I tested this function as:
## With the small Dictionary:
## >> scoreList(["a", "s", "m", "t", "p"])
## [['a', 1], ['am', 4], ['at', 2], ['spam', 8]]
## >>> scoreList(["a", "s", "m", "o", "f", "o"])
## [['a', 1], ['am', 4], ['foo', 6]]

## from dict import *
## With the slightly bigger Dictionary
##>>> scoreList(['w', 'y', 'l', 'e', 'l', 'o'])
##[['leo', 3], ['low', 6], ['lowly', 11], ['ow', 5], ['owe', 6], ['owl', 6],
## ['we', 5], ['well', 7], ['woe', 6], ['yell', 7], ['yo', 5]]

##from bigdict import *
## With even bigger Dictionary:
## scoreList(['a', 'b', 'v', 'x', 'y', 'y', 'z', 'z', 'z'])
## [['ab', 4], ['aby', 8], ['ax', 9], ['ay', 5], ['ba', 4], ['bay', 8],
##['by', 7], ['ya', 5], ['yay', 9], ['za', 11], ['zax', 19], ['zyzzyva', 43],
##['zzz', 30]]


def scoreList(Rack):
    "'Rack is the list of words which are to be checked if they can form a \
    word from Dictionary or not'"
    trueword = filter(lambda x: ind(Rack,x)==length(x), [a for a in Dictionary])
    return map(lambda x: [x]+[wordScore(x,scrabbleScores)],trueword)





## Then to obtain the word from dictionary which has greatest wordScore value,
## I have made my own maximum function whuch used reduce so that the largest
## number from a list is obtained.

## Testing this function as:
##>>> maximum([1,2,1,2])
##2
##>>> maximum([100,1,0,100])
##100


def maximum(L):
    "'L is the list with numbers from where we obtain the largest number'"
    if L==[]:   ## if empty, return empty
        return L
    else:
        return reduce(lambda x,y: x if x>y else y, L)



##Question 4 (2)
## Here I simply used the above mentioned maximum fuction such that it makes
## a List with the wordScore value of all the scoreLisr(Rack) function and then
## compare that number with the scoreList(Rack) and returns the first list with
## bestnumber

## I tested the function as:
## For small dictionary:
## bestWord(["a", "s", "m", "t", "p"])
## ['spam', 8]
## bestWord(["a", "s", "m", "o", "f", "o"])
## ['foo', 6]

## for slightly bigger dictionary:
## from dict import*
## bestWord(['w', 'y', 'l', 'e', 'l', 'o'])
## ['lowly', 11]
## bestWord(["s", "p", "a", "m", "y"])
##['may', 8]
## bestWord(["s", "p", "a", "m", "y", "z"])
## ['zap', 14]

## for even bigger Dictionary:
## from bigdict import*
##bestWord(['a', 'b', 'v', 'x', 'y', 'y', 'z', 'z', 'z'])
## ['zyzzyva', 43]


def bestWord(Rack):
    "'Rack is a list of letters in which we will use scoreList function \
to determine the word with largest wordScore value'"
    if Rack==[]:
        return []
    else:
        bestnumber= maximum([a[1] for a in scoreList(Rack)])
        bestinlist=filter (lambda x: x[1]==bestnumber, scoreList(Rack))
        return bestinlist[0]















