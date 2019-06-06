#!/usr/bin/python

import sys



# Python3 Program to convert decimal to  
# any given base 
  
# To return char for a value. For example  
# '2' is returned for 2. 'A' is returned  
# for 10. 'B' for 11 
def reVal(num): 
  
    if (num >= 0 and num <= 9): 
        return chr(num + ord('0')); 
    else: 
        return chr(num - 10 + ord('A')); 
  
# Utility function to reverse a string 
def strev(str): 
  
    len = len(str); 
    for i in range(int(len / 2)): 
        temp = str[i]; 
        str[i] = str[len - i - 1]; 
        str[len - i - 1] = temp; 
# Function to convert a given decimal  
# number to a base 'base' and 
def fromDeci(base, inputNum): 
  
    res = ""
    index = 0; # Initialize index of result 
  
    # Convert input number is given base  
    # by repeatedly dividing it by base  
    # and taking remainder 
    while (inputNum > 0): 
        res+= reVal(inputNum % base); 
        inputNum = int(inputNum / base); 
  
    # Reverse the result 
    res = res[::-1]; 
  
    return res


def rock_paper_scissors(n):
    r = []
    ro = [('rock', 0), ('paper', 1), ('scissors', 2)]
    l3n = len(str(fromDeci(3,3**n))) - 1 # max number is 1 less
    # print('l3n', l3n)
    for i in range(3 ** n):
        b3 = str(fromDeci(3, i)).zfill(l3n)
        # print('b3', b3)
        lr = []
        for j in range(n):
            lr.append(ro[int(b3[j])][0])
        r.append(lr)
    return r


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
