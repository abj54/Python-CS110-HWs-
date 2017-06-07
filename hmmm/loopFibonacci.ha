
## Anwesh Joshi
## Hw 3 Question 2
## loopFibonacci.ha


## Input: N
## Output: Nth fibonacci number (1,1,2,3...)

## Take an input in register r1 and set register r2 and r3 as 0 and 1 which
## we will use as 0th and 1st element in the series. Then we will use loop so that
## those 2 elements keep adding each other unless r1 is set 0. We keep getting 
## result in r2 and r3 and if counter sets to 0 and solution is in r2, we print 
## r2 straight away but if solution is in r3 when counter sets to 0, we copy r3 to r2 and write r2.  


0 read r1      ##Get N 
1 setn r2 0     ## set r2 as 0
2 setn r3 1     ## set r3 as 1 (1st number in series)
3 jltzn r1 15    ## If N is negative, go straight to 15 and print 0
4 jeqzn r1 15    ## If N is 0, go straight to 15 and print 0
5 addn r1 -1    ## Decrease the count of N so that if N reaches 0 now, give result "1"
6 jeqzn r1 14   ## If N reaches 0, quit the process and print the result
7 add r2 r2 r3   ## sum of first two number in series 
8 addn r1 -1     ## Decrease the count of N
9 jeqzn r1 15    ## If N reaches 0, quit to obtain the result
10 add r3 r2 r3    ## Keep follwing the sum of numbers by adding the earlier 2
11 addn r1 -1     ## Decrease the count of N
12 jeqzn r1 14    ## If N reaches 0, quit to obtain the result
13 jumpn 7      ## If not, jump to step 7 and starting adding the last two numbers 
14 copy r2 r3   ## copy value of r3 into r2 to print it
15 write r2     ## write the value of r2
16 halt      ## stop



