# python 2
name = raw_input("Enter File:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

senders = dict();
for line in handle:
    if not line.startswith('From '): continue
    words = line.rstrip().split()
    sender = words[1]
    senders[sender] = senders.get(sender, 0) + 1

winner = "";
count = 0
for key,value in senders.items():
    if count < value:
        count = value
        winner = key

print winner, count
