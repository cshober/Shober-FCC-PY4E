import os

numDays = dict() # Declaring a 'dictionary'

fileName = input('Enter a file name to open: ')

# START FILE TEST LOOP
# ---------------------------------------------------------------

while True: # Default loop for opening file
    try:
        curFile = open(fileName,'r')
        break
    except:
        print("Can't open this file! Try again.")
        continue

# ---------------------------------------------------------------

# START STR MANIUPULATION
for i in curFile: # At this point, file should be open
    i = i.rstrip()
    postSplit = i.split()

    if len(postSplit) < 3 or postSplit[0] != 'From':
        continue
    else:
        temp = postSplit[2]
        if temp not in numDays:
            numDays[temp] = 1
        else:
            numDays[temp] += 1

print(numDays)