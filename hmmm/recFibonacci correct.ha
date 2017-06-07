0 read r1                ##Take input to be the Nth number which is also the counter
1 setn r15 100           ## stack pointer
2 setn r2 1              ## setting a register r2 as 1 (1st element)
3 setn r3 0              ## setting register r3 as 0(0th element)
4 setn r4 1              ## setting register r4 as 1 which we will use later
5 copy r5 r1             ## then we simply set register r5,r6,r7,r8 with the value same as r1,r2,r3,r4
6 copy r6 r2 
7 copy r7 r3
8 copy r8 r4
9 calln r14 14            ##this is called to obtain (n-2)th term
10 calln r13 36           ## this will obtain (n-1)th term
11 add r9 r2 r6           ## we add them to obtain the nth term fibonacci series.
12 write r9
13 halt                 ## stop

##Calling the first function:
## Checking the case when Nth term is negative,0,1 or 2 (using the counter r1) so that we give 0,0,1 or 1 respectively.

14 jltzn r1 34
15 jeqzn r1 34
16 addn r1 -1
17 jeqzn r1 35
18 addn r1 -1
19 jeqzn r1 35

## then we use the function such that (n-1)th term is obtained. For that, we use stack to store the value of the r2, which is storing the upcoming value of ## the series by being 1 behind such that it is the (n-1)th term of series.

20 addn r15 1     ## adding to stack
21 storer r2 r15  ## storing the values of fibonacci series
22 addn r15 1     ## adding to stack
23 storer r14 r15 ## storing the values of the position in memory
24 addn r1 -1     ## Decrease the counter
25 calln r14 19   ## recursilvely call the function to obtain (n-1)th term in series.

26 loadr r14 r15  ## load the position in memory
27 addn r15 -1    ## get the ealier stack
28 loadr r2 r15   ## load the (n-1)th term, at the end
29 addn r15 -1    ## decrease the stack
30 add r2 r4 r3   ## add r2 so that we get the upcoming value which is (n-1)th term
31 copy r3 r4     ## transfer the values to other registers such that the upcoming terms can be calculated
32 copy r4 r2
33 jumpr r14      ## go back to caller

## Final case:

34 copy r2 r3  ##when r1 is 0 or negative, we change r2 to 0
35 jumpr r14   ## go back to callet

## Calling the second function:
## Here we use the same strategy as before but we store the r8 value which is the sum of the number upcoming and move on with the value of r7 which has the (n-2)th term of the sequence to add with (n-1)th term.

## here we can simply return 0 when r5(input) number is negative,0,1 or 2 since here we only need (n-2)th term.
36 jltzn r5 58
37 jeqzn r5 58
38 addn r5 -1
39 jeqzn r5 58
40 addn r5 -1
41 jeqzn r5 58
42 addn r5 -1
43 jeqzn r5 59

44 addn r15 1     
45 storer r6 r15
46 addn r15 1
47 storer r13 r15
48 addn r5 -1
49 calln r13 43

50 loadr r13 r15
51 addn r15 -1
52 loadr r6 r15
53 addn r15 -1
54 add r6 r8 r7
55 copy r7 r8     ##the only difference is that r7 here is getting the desired number which we will later use in the function i.e. (n-2)th term
56 copy r8 r6
57 jumpr r13

58 copy r6 r7          
59 jumpr r13     ## end the function

