## Anwesh Joshi
## HW 4
## life.py


###Helpful Functions::

## createBoard function creates a board of width and height from input
## with all it's elements 0. I simply used for loop to keep increasing
## height and used idea from createOneRow(width) to make the board

## Test:
##>>> createBoard(5,3)
##[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
##>>> createBoard(2,1)
##[[0, 0]]

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A +=[[0]*width]   # What do you need to add a whole row here?
    return A


## This is the function provided by Professor that prints the 2d
## lists of lists

##Test:
##>>> A=createBoard(5,3)
##>>> printBoard(A)
##00000
##00000
##00000

import sys
def printBoard( A ):
    """ this function prints the 2d list-of-lists
        A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )
        
## I used this innerCells(w,h) such that all the elements
## inside the 2d list of list are 1 but the border elements
## are all 0. For this I used the ideas from create Diagonal
## provided to us by the Professor. Simiply I will set the border
## elements 0 first and then check innercells.

##>>> A = innerCells(5,5)
##>>> printBoard(A)
##00000
##01110
##01110
##01110
##00000

def innerCells(w,h):
    """this function prints out a 2d list of lists with
    board of width "w" and height "h" such that all the
    inside elements of the list are 1 but border
    elements are 0"""
    A=createBoard(w,h)
    for row in range(h):
        if row==0 or row==h-1:
            for col in range(w):
                A[row][col]=0
        else:
            for col in range(w):
                if col==0 or col==w-1:
                    A[row][col]=0
                else:
                    A[row][col]=1
    return A

## I used this randomCells simply with the same idea as innerCells where
## the innerelements were random picked by using random function between
## 0 and 1.

## >>> A = randomCells(10,10)
##>>> printBoard(A)
##0000000000
##0011111100
##0101100110
##0001000110
##0001011110
##0110111110
##0011101110
##0011110110
##0110111010
##0000000000

import random
def randomCells(w,h):
    """randomCells(w,h) creates a board with dimension w,h such that
      inner elements are random picked between 1 and 0 by system"""
    A=createBoard(w,h)

    for row in range(h):
        if row==0 or row==h-1:
            for col in range(w):
                A[row][col]=0
        else:
            for col in range(w):
                if col==0 or col==w-1:
                    A[row][col]=0
                else:
                    A[row][col]=random.choice([0,1])
    return A

## This is a deepcopy Function such that the value of
## old board is allowed to change without changing the new
## board elements. Here I wanted to use the list array idea
## but that didn't work when I used printBoard which is 2d lists
## and hence I used list comprehension which worked fine later.
## Kyler helped me defintely to write this and defined why list array
## didn't work.

##Test:
##>>> A=randomCells(4,4)
##>>> printBoard(A)
##0000
##0000
##0100
##0000

##>>> B=copy(A)     ##Deepcopy
##>>> printBoard(B)
##0000
##0000
##0100
##0000

##>>> A[0][0]=1          ##changing the original element
##>>> printBoard(A)
##1000
##0000
##0100
##0000

##>>> printBoard(B) ##doesn't change the element in new list 
##0000
##0000
##0100
##0000

def copy( a ):
    """here "a" is a list which is to be deepcopied so that
     it's value change wont affect the new list"""
    b= [x[:] for x in a]
    return b


## innerReverse is a function which changes the value of
## inner elements of a 2d lists of lists
## such that 0 is changed into 1 and 1 is changed into 0. 

## Test:
##>>> A=randomCells(5,5)
##>>> printBoard(A)
##00000
##00010
##00010
##01000
##00000

##>>> A2=innerReverse(A)
##>>> printBoard(A2)
##00000
##01100
##01100
##00110
##00000

def innerReverse(A):
    """ A is a board that is created such that each of
        it's innerelements are changed between 0 and 1"""
    h=len(A)
    w=len(A[0])

    for row in range(h):
        if row==0 or row==h-1:
            for col in range(w):
                A[row][col]=0
        else:
            for col in range(w):
                if col==0 or col==w-1:
                    A[row][col]=0
                else:
                    if A[row][col]==0:
                        A[row][col]= 1
                    else:
                        A[row][col]=0
    return A
                        


### Conway's Game Of Life

## Starting to write the Conway's Game of Life, I first ahve to write
## a code such that I can find the neighbors for the elements in a
## board. Since I have to determine its life, I used for loop to go
## around that particular element, and increase the count if it finds
## a live cell. My code also checks the element itself (which is not
## a neighbor), I checked that particular element and changed te final
## result to be 1 or 0.

## >>> A=randomCells(5,5)
##>>> printBoard(A)
##00000
##01110
##00110
##00100
##00000
##>>> countNeighbors(2,2,A)
##5
##>>> countNeighbors(1,1,A)
##2

def countNeighbors(row,col,A):
    " 'row and col is the position of a particular element in board A\
    whose live neighbors are to be calculated '"
    count=0
    for i in range (row-1,row+2):
        for j in range (col-1,col+2):
            if A[i][j]==1:
                count +=1
            else:
                count+=0
    if A[row][col]==1:
        return count -1
    else:
        return count
     
## Now, I am writing a function next_life_generation which will
## print the upcoming next generation board such that elements with
## less than 2 or more than 3 neighbor are 0, 3 neighbors are 1 and 2
## neighbors stay the same. So, first I set the border elements 0 and
## then do the neighbor count on innerelements. I have to use copy here
##since I want to obtain the new board in A itself and so will carry
## my program on B which is copy o A.

##Test:
##>>> A=randomCells(5,5)
##>>> printBoard(A)
##00000
##00110
##00000
##00100
##00000

##>>> A2=next_life_generation(A)
##>>> printBoard(A2)
##00000
##00000
##00110
##00000
##00000
    
def next_life_generation( A ):
    """ makes a copy of A and then advanced one
        generation of Conway's game of life within
        the *inner cells* of that copy.
        The outer edge always stays 0.
    """
    B = copy ( A)
    h=len(B)
    w=len(B[0])

    for row in range(h):
        if row==0 or row==h-1:
            for col in range(w):
                A[row][col]=0
        else:
            for col in range(w):
                if col==0 or col==w-1:
                    A[row][col]=0
                else:
                    a=countNeighbors(row,col,B)
                    if a<2 or a>3:
                        A[row][col]=0
                    elif a==3 :
                        A[row][col]=1
    return A


### Interactive Game Part

## Here I have used the above two functions so that I can interact
## with the user to make the game user friendly. I have simply used
## all the instructions provided to me and used that to make the code
## to get next life generation and replaced the live cells with "@" and
## dead cells with " ". I had to use deepcopy so that I could change the
## value in that deepcopied since countNeighbors is not gonna run on
## "@" and " ". We need 1 and 0 for that, so we use copy.
## I take the command in line where the first letter is the command
## alphabet and after that I used "eval" to make the string-list into
## numerical list. 

def interact():
    """ Interact with a user to play Conway's Game of Life.
    """
    A = None
    line = raw_input("Enter Command: ")
    line = line.replace(" ", "")
    while line[0] != "q":   ## quit the program
        command = line[0]

        if command == 'n':  ## n[x,y] is the string where we make a  
                            ## board of dimension x=height and y=width
            numlist=eval(line[1:])
            width=numlist[1]
            height=numlist[0]
            A= createBoard(width,height) ##board created
            

        elif command == 'i': ## i[[x1,y1],[x2,y2]..] is a list with
                             ## coordinates of live elements
            line=line[1:]
            livelist=eval(line)
            for i in range(len(livelist)):
                h=livelist[i][0]
                w=livelist[i][1]
                if h==0 or h==len(A)-1 or\
                w==0 or w==len(A[0])-1: ##checking border for live cells
                    A[h][w]==0
                else:
                    A[h][w]=1 
            

        elif command=='p': ##prints the current generation
                           ##board with 1 and 0
            printBoard(A)

        elif command=='d': ## prints the current generation with
                           ## "@" and " " for 1 and 0 respectively
            C=copy(A)   ## using deepcopy to get value in C so that
                        ## we can change its values
            for row in range(width): 
                for column in range(height):
                    if C[column][row]==1:
                        C[column][row]="@"
                    elif C[column][row]==0:
                        C[column][row]=" "
            printBoard(C)           

        elif command=='r': ## r n where n is an integer and we will use
                           ## next_life_generation "n" times and print
                        ## the board with "@" and " " for each generation.
            line=line[1:]
            repeat=eval(line)
            for i in range(repeat):
                 A=next_life_generation( A )
                 E=copy(A)
                 for row in range(width):
                     for column in range(height):
                         if E[column][row]==1 :
                             E[column][row]= "@" 
                         elif E[column][row]==0 : 
                            E[column][row]=" "
                 printBoard(E)
            
           

        elif command=='h':   ## h is Help to show what commands we can
                             ## input and what it will do.
            HELP=  " Commands:\n\
                n [height,width] (Create a height * width board)\n\
                i  (initialize life) \n\
                p      (print the board) \n\
                d      (display the board)\n\
                r   (advance n generations, displaying each after)\n\
                h      (display this help reminder)\n\
                q      (quit)\n"
            print (HELP)

        line = raw_input("Enter Command: ") 
        line = line.replace(" ", "")
    print "Life is over\n"
            
            
## Test:
##interact()
##Enter Command: n[10,20]
##Enter Command: i[[1,1],[1,2],[2,3],[3,2],[4,7],[7,19],[8,18],[2,3]]
##Enter Command: d
                    
## @@                 
##   @                
##  @                 
##       @            
##                    
##                  
##                    
##                  @ 
##                    
##Enter Command: r2
##                    
##  @                 
## @ @                
##                    
##                    
##                    
##                    
##                    
##                    
##                    
##                    
##  @                 
##  @                 
##                    
##                    
##                    
##                    
##                    
##                    
##                    
##Enter Command: p
##00000000000000000000
##00100000000000000000
##00100000000000000000
##00000000000000000000
##00000000000000000000
##00000000000000000000
##00000000000000000000
##00000000000000000000
##00000000000000000000
##00000000000000000000
##Enter Command: h
## Commands:
##                n [height,width] (Create a height * width board)
##                i  (initialize life) 
##                p      (print the board) 
##                d      (display the board)
##                r   (advance n generations, displaying each after)
##                h      (display this help reminder)
##                q      (quit)
##
##Enter Command: q
##Life is over

            
            
        
       
                    
                        


                
    

    
    


                
