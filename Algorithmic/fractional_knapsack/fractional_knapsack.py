# Uses python2
def get_optimal_value(capacity, weights, values):
    value = 0.
    units = map(getUnits,values,weights)
    # write your code here
    for i in range(len(values)):
        if capacity == 0:
            return value
        maxUnit = max(units)
        maxIndex = units.index(maxUnit)
        addWeight = min(capacity,weights.pop(maxIndex))
        value = value + addWeight*units.pop(maxIndex)
        capacity = capacity - addWeight

    return value

def getUnits(a,b):
    return float(a)/b

inputData = raw_input()
# print(inputData)
data = list(map(int, inputData.split()))
n, capacity = data[0:2]
values = data[2:(2 * n + 2):2]
weights = data[3:(2 * n + 2):2]
print(n,capacity)
print(values)
print(weights)
opt_value = get_optimal_value(capacity, weights, values)
print("{:.10f}".format(opt_value))