# Uses python2

def binary_search(a, x):
    left, right = 0, len(a)-1
    # write your code here
    while left <= right:
        m = (left + right)/2
        if x == a[m]:
            return m
        elif x < a[m]:
            right = m - 1
        else:
            left = m + 1

    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

# data = list(map(int, raw_input().split()))
data = [5, 1, 5, 8, 12, 13, 5, 8, 1, 23, 1, 11]
n = data[0]
m = data[n + 1]
a = data[1 : n + 1]
end = []
for x in data[n + 2:]:
    end.append(binary_search(a,x))

print end
    # replace with the call to binary_search when implemented
    # print(linear_search(a, x), end = ' ')
