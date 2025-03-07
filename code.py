# # We want you to calculate the sum of squares of given integers, excluding any negatives.
# # The first line of the input will be an integer N (1 <= N <= 100), indicating the number 
# of test cases to follow.
# # Each of the test cases will consist of a line with an integer X (0 < X <= 100), 
# followed by another line consisting of X number of space-separated integers Yn (-100 <= Yn <= 100).
# # For each test case, calculate the sum of squares of the integers, 
# excluding any negatives, and print the calculated sum in the output.
# # Note: There should be no output until all the input has been received.
# # Note 2: Do not put blank lines between test cases solutions.
# # Note 3: Take input from standard input, and output to standard output.
# You may only use standard library packages. In addition, extra point is awarded
# if solution does not declare any global variables.

# # Your source code must be a single file, containing at least a main function
# # Do not use any for loop, while loop, or any list / set / dictionary comprehension
# # Your solution will be tested against Python 3.13 (as of January 2025) or higher

import sys
import functools 


def main():
    print(decodeString(['1 2', '3 4']))


    arr = []
    N = int(input())
    ReadN(N, arr)
    print(arr)
    print(SumOfSquares(arr))

def ReadN(N, arr): #reads # of test cases
    if N == 0:
        return arr
    elif N > 0: 
        ReadX(int(input()), arr)
        ReadN(N-1, arr) 

def ReadX(X, intarr): #reads # of integers and line of integers
    return intarr.append(input())

def SumOfSquares(arr):
    #Implement decoding (parsing) '1 2' strings into nubmers 
    return list(map(SquareNumber, arr))

def SquareNumber(num):
    if num > 0:
        return num*num

def decodeString(arr):
    decodedStr = list(map(lambda x: x.split(' '), arr)) #returns [['1', '2'], ['3', '4']]
    #return list(map(int, decodedStr))


#TODO:
#implement decoding function that would pare strings of integers into a list of integers 
#implement output function 
if __name__ == "__main__":
    main()
    
