# Uses python2
def get_change(n):
    x = [10,5,1]
    coinNum = 0
    remains = n
    i = 0
    while remains != 0:
        coinNum = coinNum + remains/x[i]
        remains = remains % x[i]
        i = i + 1
    return coinNum

n = int(input())
print(get_change(n))
