# Uses python2
# Given two integers a and b, find their greatest common divisor
import sys

def gcd(a, b):
    if(type(a)!=int or type(b)!=int):
        return
    while a%b!=0:
        c = a%b
        a = b
        b = c

    return b

# if __name__ == "__main__":
# input = sys.stdin.read()
# a, b = map(int, input.split())
inputNumber = raw_input()
a = int(inputNumber.split()[0])
b = int(inputNumber.split()[1])
print(gcd(a, b))
