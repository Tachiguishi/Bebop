# Uses python2
# Given an integer n, find the last digit of the nth Fibonacci number Fn
import sys

def get_fibonacci_last_digit(n):
    if(type(n) != int):
        return
    i = 2
    fib = [0,1]
    while i <= n:
        fib.append((fib[i-1]+fib[i-2])%10)
        i = i + 1

    return fib[n]

#if __name__ == '__main__':
#input = sys.stdin.read()
n = int(input())
print(get_fibonacci_last_digit(n))
