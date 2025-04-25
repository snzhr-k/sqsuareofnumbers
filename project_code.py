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

def ReadN(N, arr): 
    if N == 0:
        return arr
    elif N > 0: 
        ReadX(int(input()), arr)
        ReadN(N-1, arr) 

def ReadX(X, intarr):
    return intarr.append(input())

def SumOfSquares(arr):
    squaredInts = list(map(SquareNumber, arr))
    sumInts = list(map(sum, squaredInts))
    return sumInts

def SquareNumber(Ints): 
    filteredInts = list(filter(lambda x: x>0, Ints)) 
    squaredInts = list(map(lambda x: x*x, filteredInts))
    squaredInts = list(filter(lambda x: x>0, squaredInts))

    return squaredInts
    

def decodeString(arr):
    split_strs = list(map(lambda x: x.split(' '), arr))
    int_lists = list(map(lambda lst: list(map(int, lst)), split_strs))
    
    return int_lists

def main():
    test_case_lines = []
    N = int(input())
    ReadN(N, test_case_lines)

    decoded = decodeString(test_case_lines)
    sum_of_squares = SumOfSquares(decoded)
    
    print(*sum_of_squares, sep="\n")

if __name__ == "__main__":
    main()


