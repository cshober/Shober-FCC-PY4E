# Add to 9_3.py, figure out who has the most messages in the file

import os

diffEmails = dict()
max = 0
maxAddress = ''

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

# First iteration to get MAX
for address in diffEmails:
    if diffEmails[address] > max:
        max = diffEmails[address]
        maxAddress = address
    else:
        continue

# Second iteration through dictionary to find DUPLICATES of MAX
# for dupes in diffEmails:
    # if diffEmails[dupes] != diffEmails[maxAddress]:
        # diffEmails[]