#Uses python3

def min_dot_product(a, b):
    #write your code here
    res = 0
    n = len(a)
    for i in range(n):
        res += a.pop(a.index(max(a))) * b.pop(b.index(min(b)))
    return res

inputData = raw_input()
data = list(map(int, inputData.split()))
n = data[0]
a = data[1:(n + 1)]
b = data[(n + 1):]
print(min_dot_product(a, b))