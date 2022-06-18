import os

incomplete = True
# fileName = 'balls.txt'

while incomplete:
    fileName = input('Enter file name: ')

    if fileName == 'done':
        quit()
    else:
        try:
            fileOpen = open(fileName, 'r')
        except:
            print('File "' + fileName +  '" not found! Try again.')
            continue

    incomplete = True
    break

for i in fileOpen:
    print(i.strip())