
## Anwesh Joshi
## HW 3 Question 3
## recFibonacci.ha


## Input: N
## Output: Nth term from fibonacci sequence (1,1,2,3,5,...)

## In this problem, I had to use recursion to obtain the Nth fibonacci term such that I had 
## to do call the same function twice recursively, once to get N-1 th term and again to get
## N-2 th term. I then added both those terms to obtain the final result.

## Here, I have called the same function twice recursively such that I get two different 
## answers for the program that are to be added and obtain the fibonacci term.

0 read r1
1 setn r15 100
2 calln r14 9
3 copy r6 r2
4 nop
5 calln r14 13
6 add r5 r6 r2    ## Adding two earlier terms from fiboanacci series, to get final solution.
7 write r5
8 halt

## Checking for the best cases: 
## When N is negative or 0, we return 0 and when it is 1 0r 2, we return 1.
9 jltzn r1 37 
10 jeqzn r1 37  
11 addn r1 -1
12 jeqzn r1 33
13 addn r1 -1
14 jeqzn r1 33
15 jltzn r1 37

## Storing the values from r1, r2(which is the sum) and r14(memory address) in r15.
16 addn r15 1
17 storer r1 r15
18 addn r15 1
19 storer r2 r15
20 addn r15 1
21 storer r14 r15
22 calln r14 13        ## Calling the same function until the best condition is met.

## Here we start using the values that we stored earlier.
23 loadr r14 r15
24 addn r15 -1
25 loadr r2 r15
26 addn r15 -1
27 loadr r1 r15
28 addn r15 -1

29 add r2 r3 r4
30 copy r3 r4
31 copy r4 r2
32 jumpr r14

## Best case when N is 1 or 2. 
33 setn r2 1
34 setn r3 0
35 setn r4 1
36 jumpr r14

## Best case when N is negative or 0.
37 setn r2 0
38 jumpr r14
