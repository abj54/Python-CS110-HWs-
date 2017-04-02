
# Anwesh Joshi
#functions.py -- Homework 1
 
 
## Question 1
# Here we will be converting the temperature given in fahrenheit to celcius. For this, we will simply be using the mathematical
#relation between fahrenheit and celcius such that we get the answer in decimal system
 
# I tested it as:
# >>>f2c(212)
# 100.0
# >>> f2c(100)
# 37.77777777777778
# >>> f2c(-40)
# -40.0
 
 
def f2c(f):
    "'f is the temperature in fahrenheit which will be changed to celcius"
    c=(f-32.0)*5/9.0     # mathematical relation for  fahrenheit to celcius
    return c
 
 
 
 
 
## Question 2
# In this problem, we find the dot products of two vectors L and K such that if they are empty we get 0.0 and
#if they are of different lengths, extra elements in the larger vector will be left out
 
# this is simply tested by:
# >>> dot([1,2],[2,3])
# 8.0
# >>> dot([1,2,3],[2,3])
# 8.0                      # here the extra element of vector L i.e. 3 is not considered giving result only for 1*2+2*3
 
def dot(L,K):
    "'L and K are two vectors whose dot product we will find'"
    if L==[] or K==[]:
        return 0.0
    else:
        return L[0]*K[0]+ dot(L[1:],K[1:])
 
print (dot([1,2,3],[2,3]))
 
 
## Question 3
# This program will separate all the strings from S and present them individually. For this program, I had to individualize
# each string of length 1 and put them in a list and then use recursion to obtain all the remainig strings which is our result
 
# to test this program, we simply enter a string in S and explode will return all the individualized strings
# >>> explode('apple')
# ['a','p','p','l','e']
# >>> explode('spam')
# ['s', 'p', 'a', 'm']
 
 
def explode(S):
    "'S is the string whose each characters are to be returned in a list'"
    if S!='':
        k=[S[0]]+explode(S[1:])  # after separating the first character in a list, we use recursion to do same to all remaining characters in string S
        return k                 # k has stored all the characters after recursion and we return it
    else:                        # if S has no strings in it,
        return[]                 # we return the empty list
 
 
 
## Question 4
# Here I defined an element e and sequence L and obtain the first position of e in L (starting from 0),
#if it exists there. If it doesnt, it will return the length of sequence L. L can be a string or a list.
# For this, I have assigned two variable k and m so that they will keep the program clear and help me obtain
# position of e as I have done below
 
# I tested this program as:
# >>> ind('s','sam')
# 0
# >>> ind(' ', 'outer exploration')
# 5
# >>> ind('hi', [ 'hello', 42, True ])
# 3                                      #here as e is not a member of L, so returned value is the lenghth of list L
 
 
def ind(e,L):
    "'e is the element whose position we determine in sequence L'"
    k=0                       #we define k and m as 0 to help us obtain the position of e by comparing e with all elements of L
    m=0
    if L=='' or L==[]:
        return m              # if L has no elements in it, we obtain length of L which is 0
    elif e!=L[0]:             # if e is not the first element of L
       m= 1+ k+ ind(e,L[1:])  # we use recursion to find first position of e in L, we also use m to obtain it's position in relation to k
       return m               # we return the value of m as it keeps increasing from 0 with every next element being checked for its position
    else:                     # when e is the first element of L, we return value of m that is being stored earlier through recursion
        return m
 
 
 
 
 
## Question 5
# Here I define an element e and a list L such that all the elements e are removed from L. In this case, I had to be careful so that I don't end
# the recursion just after finding the first element and removing it. But I had to use recursion to check all the elements and make sure all the
# similar same are removed from list L
# in the above program, we have to remove all the elements e from list L,
 
 
# so I have tested it as:
# >>> removeAll(42,[21,23,42,23,42])
# [21,23,23]
# >>> removeAll([77, 42], [ 55, [77, 42], [11, 42], 88 ])
# [55, [11, 42], 88]
# >>> removeAll(42, [ 55, [77, 42], [11, 42], 88 ])
# [55, [77, 42], [11, 42], 88]
 
def removeAll(e,L):
    "'e is the element which is completely removed from list L'"
    if L!=[]:                                          # if list L is not empty,
        if e==L[0]:                                    # and e is first element of L
            return removeAll(e,L[1:])                  # we remove that first element and use recursion to check all the other elements in L
        else:                                          # and if, e is not the first element of L
            return [L[0]]+removeAll(e,L[1:])           # we keep the first element and use recursion to check all the other elements in L
    else:                                              # But if L is an empty list or once it is empty,
        return []                                      # we return the empty list as well
 
 
 
 
 
## Question 6
# here i am creating my own function myFilter such that only the elements from the list that satisfies the Predicate will be the result
# for this particular case, the result list will be all the even numbers from list L. For that,I also define a function even so that
# we can check if individual member of L falls under even number or not
 
# here we will test the function as:
# >>>myFilter(even,[1,2,3,4,5])
#[2,4]
# >>>myFilter(even,[])
# []
 
 
def even(X):    # this function is used as a predicate in which the even numbers are only returned
    "'X is a number which is to be determined as even or not'"
    if X%2==0:                          # if a number X is divided by 2 and remainder is 0
        return True                     # we return true
    else:                               # if number is divided by 2 and remainder is not 0,
        return False                    # we return false
 
def myFilter(even,L):
    "'L is the list which will check all the elements in it with the condition provided and only the one which satify the conditions are returned'"
    if L==[]:               #if list L is empty
        return []           # the list we return will be empty as well
    elif even(L[0]):        #otherwise, we wil check the first element of L with the predicate provided which is even in this case, if it is true
        return [L[0]]+myFilter(even,L[1:])   # we will return the first element of L and then use recursion on all the remaining elements to obtain the even list
    else:                               # if the element is not even,
        return myFilter(even,L[1:])    # we will lost that first element and use recursion on the followig elements to check for even or not
 
 
 
 
## Question 7
# Here I define a function deepReverse(L) such that all the elements in list L are reversed. there might be
#  a list within a list as well whose elemenrs are to be reversed as well, for that I will use 'type' function to
# check if the element of list is a list or not.Then I will use recursion to deepReverse the elements or the list in list L
 
# I tested this function to make sure that the lists in the list are completely reversed as well:
#>>> deepReverse([1,2,3])
# [3,2,1]
#>>>deepReverse([1,2,[3,[4,5],6]])
# [[6, [5, 4], 3], 2, 1]
# >>>  deepReverse([1, [2, [3, 4], [5, [6, 7], 8]]])
# [[[8, [7, 6], 5], [4, 3], 2], 1]                  #here we can see that the list within list within list is reversed as well
 
 
def deepReverse(L):
    "'L is the list whose elements are to be completely reversed'"
    if L==[]:                                                 # if L is an empty list
        return []                                             # we return back an empty list
    elif type(L[0])==type([1,2,3]):                           # here we check if the first element of L is a list or not, and if it is
        return deepReverse(L[1:])+ [deepReverse(L[0])]        # we will use recursion on all the elements following the first one, while we
                                                              # use same deepReverse function on the first element to check if there is anymore list inside of it
    else:                                                     # if first element is not a list,
        return deepReverse(L[1:])+[L[0]]                      # we use recursion on the followinf elements but keep first element as a list in reversed order
 
 
 
 
 
 
## Question 8
# To find the intersection of s1 and s2, I had to check if any member of s1 is in s2 or not. For that I took help from different function
# member which checked if item i belongs to a list l or not. Using this function, I checked presence of each individual element from s1 in s2
# and then returned the final obtained list of common element.
 
# to test the above program, I defined two sets s1 and s2 as:
# >>> intersect([1,2,3],[2,3,4])
# [2,3]
# >>>intersect([1,2,3],[4,5,6])
# []
# >>> intersect([1, [2, [3, 4], [5, [6, 7], 8]]], [])
# []
# >>>intersect([1,[2,3],4],[[1,2],[2,3]])
# [[2,3]]
# >>> intersect([1, [2, 3], 4], [4, 2, [2, 3], 0])
# [[2, 3], 4]
 
 
def member( i, l ):
    "'l is a list where we will check if item i is a member of it or not'"
    if l == []:            #if list l is empty,
        return False       # element i doesn't exist in there
    elif l[0] == i:        # if i is the first element of list l,
        return True        # it return True as i exist in l
    else:                  # if i is not first element of l, we will use recursion to check until the list l is empty to get true or false
        return member( i, l[1:] )
 
def intersect(s1,s2):
    "'s1 and s2 are two sets with elements and we will return the intersection between two sets i.e. the common elements in these two sets'"
    if s1 == [] or s2==[]:                          # if one of the two sets are empty,
        return []                                   # we will return an empty set, which is the intersetction between two
    elif member(s1[0],s2):                          # here we apply member function to check if first element of s1 belongs to s2
        return [s1[0]] + intersect(s1[1:],s2)       # if it does, we will keep that element and use recursion on the remainder of the elements in s1
    else:                                           # if first element of s1 is not in s2,
        return intersect(s1[1:],s2)                 # we will lose that element and use recursion on remainder of s1 to check if they are on s2
 
 
 
 
 
 
## Question 9
# Here I have to be careful so that I check the first element in first list in the list 'scorelist'. The numerical value that has been paired with that string has
# to be returned. The letterscore function will hence check the letter in the list within list 'scorelist' and return the numerical value which is adjacent to
# the string letter in the list. For that purpose we will take a seperate list called scrabbleScores will has all the alphabets and has been paired with a numerical
# value.
 
scrabbleScores = [ ["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1],
                 ["f", 4], ["g", 2], ["h", 4], ["i", 1], ["j", 8],
                 ["k", 5], ["l", 1], ["m", 3], ["n", 1], ["o", 1], ["p", 3],
                 ["q", 10], ["r", 1], ["s", 1], ["t", 1], ["u", 1], ["v", 4],
                 ["w", 4], ["x", 8], ["y", 4], ["z", 10] ]
 
 
# I tested the above program as:
# >>>letterScore ("a",scrabbleScores)
# 1                                     # in the list scrabbleScores, we see "a" is paired up with 1 which is the result
# >>>letterScore("m",scrabbleScores)
# 3                                     # similarly, "m" is paired up with 3 and the result is 3
 
 
def letterScore(letter,scorelist):
    "'letter is the string whose numerical value associated in the scorelist will be obtained'"
    if letter==scorelist[0][0]:              # if first element of first list of scorelist is same as the letter provided,'"
        return scorelist[0][1]               # we can simply return the second element in that list which is it's numerical value'"
    else:                                    # if that is not the case i.e. the first element of list within scorelist is not letter,
        return letterScore(letter,scorelist[1:])     # we will use recursion to check the remainder list in the scorelist
 
 
 
 
 
## Question 10
# In this case, wordScore (S,scorelist) will be defined such that S is the combination of strings of length 1 and are lowercase letters and
# scorelist is a list with many lists in it which has a string and numerical value assigned to it. Then wordScore is supposed to return the sum
# of all the numerical value that has been paired up with all the single length character of string S from the list scorelist.
 
 
# I tested this program as
# >>> wordScore('spam',scrabbleScores)                  # here letter s,p,a and m in the scrabbleScores are paired
# 8                                                     # with numbers 1,3,1 and 3 respectively which gives result 8(1+3+1+3)
# >>> wordScore("adam",[["a",1],["d",5],["m",6]])
# 13                                                    # here the numbers associated with a,d,m are 1,5,6 respectively which yields out the result 13(1+5+1+6)
# >>> wordScore("wow", [['o', 10], ['w', 42]])
# 94
 
def wordScore(S,scorelist):
    "'S is the string whose individual numerical values are to be found from scorelist'"
    z=0                                                 # we define z=0 as a variable that will store the sum of all the strings
    if S!='':                                           # if the string S is not empty,
        z=letterScore(S[0],scorelist)              # we use letterScore function that we defined earlier to find the numerical value paired with the first letter of Z
        return z+ wordScore(S[1:],scorelist)        # then, we return the numerical value along with the
                                                        # recursion on remaining strings in S, such that they keep algebrically adding
                                                        # until a numerical value of z is obtained which is returned
    else:                                               # if S is empty,
        return 0                                        # we return the value 0
