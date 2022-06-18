# Find how many emails have been sent from different addresses and store them in a dictionary

import os

diffEmails = dict()

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
for i in curFile:
    i = i.rstrip()
    postSplit = i.split()

    if len(postSplit) < 2 or postSplit[0] != 'From':
        continue
    else:
        temp = postSplit[1]
        if temp not in diffEmails:
            diffEmails[temp] = 1
        else:
            diffEmails[temp] += 1

for k,v in diffEmails.items():
    print(k,v)