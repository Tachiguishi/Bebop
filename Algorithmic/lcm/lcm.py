# Uses python2
# The least common multiple of two positive integers a and b
# is the least positive integer m that is divisible by both a and b.
import sys

def gcd(a, b):
    if(type(a)!=int or type(b)!=int):
        return
    while a%b!=0:
        c = a%b
        a = b
        b = c
    return b

def lcm(a, b):
    if(type(a)!=int or type(b)!=int):
        return

    return a*b/gcd(a,b)

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     a, b = map(int, input.split())
inputNumber = raw_input()
a = int(inputNumber.split()[0])
b = int(inputNumber.split()[1])
print(lcm(a, b))

