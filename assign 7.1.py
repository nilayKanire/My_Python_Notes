# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname, 'r')

total = 0
count = 0
for line in fh:
    if not line.startswith('X-DSPAM-Confidence: '):
        continue
    tk = line.find("0")
    number = float(line[tk:])
    count = count + 1
    total = total + number


average = total/count
print("Average spam confidence:", average)


# average = (0.8475  )/ count
# print("Average spam confidence: ")


'''
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    t=line.find("0")
    number= float(line[t:])
    count = count + 1
    total = total + number
    print(count)

average = total/count
print("Average spam confidence:",average)
'''