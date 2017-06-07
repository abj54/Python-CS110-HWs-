##Anwesh Joshi
## HW 3  Question 1
## average.ha

## Input numbers: a,b,c...(nth terms)
## Output numbers: their Average and the remainder

## In this program, we used three registers: r1, r2 and r5. We take input 
## in r1 and r2 and use r5 as counter. We set the conditions such that 
## we keep taking the input and adding them and at the end we divide it by
##the counter so that we get the quotient and remiander and write 
## it. If the first input is 0, we stop the program straight away. 
## And any input of 0 stops the  program such that the last input 0 is not counted. 

0 read r1       ## Get the first number in r1                 
1 jeqzn r1 12  ## if first number is 0, we go to step 12 and halt it
2 setn r5 1    ## we set a register r5 as 1

3 read r2       ## Input second number in r2
4 jeqzn r2 8    ## If second number is 0, we print the final value obtained in r1 and r2
5 add r1 r1 r2      ## we store the sum of r1 and r2 in r1
6 addn r5 1       ## then we keep track of numbers we are getting in r5 by adding r5 and r6
7 jumpn 3         ## to input other numbers, we go to step 4

8 div r2 r1 r5    ## here we divide the sum of all the numbers by their count 

9 mod r1 r1 r5    ##The remainder is stored in r2
10 write r2        ## we print the average 
11 write r1        ## we print the remainder
12 halt            ## and the process is stopped

