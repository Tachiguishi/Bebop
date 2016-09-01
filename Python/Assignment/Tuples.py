# python 2
name = raw_input("Enter File:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hours = dict();
for line in handle:
    if not line.startswith('From '): continue
    words = line.rstrip().split()
    time = words[5]
    hour = time.split(':')[0];
    hours[hour] = hours.get(hour, 0) + 1

hoursList = hours.items()
hoursList.sort();
print hoursList
for hour, count in hoursList:
    print hour, count
