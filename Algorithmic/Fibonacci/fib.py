# Uses python2
def calc_fib(n):
    if(type(n) != int):
        return
    i = 2
    fib = [0,1]
    while i <= n:
        fib.append(fib[i-1]+fib[i-2])
        i = i + 1

    return fib[n]

n = int(input())
print(calc_fib(n))
