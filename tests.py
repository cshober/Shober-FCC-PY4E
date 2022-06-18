# n = 5

# while n != 0:
#     print(n)
#     n -= 1

# (--) and (++) are not operators in Python. Use (-= n) and (+= n) to iterate

# ---------------------------------------------------------------

# smallest = None
# print("Before:", smallest)
# for itervar in [67, 3, 41, 12, 9, 74, 15, 2, -67]:
#     if smallest is None or itervar < smallest:
#         smallest = itervar
#         break # This break makes it so that only the first number in the sequence is outputted. Without this, the code will run normally
#     print("Loop:", itervar, smallest)
# print("Smallest:", smallest)

# WITHOUT BREAK (OUTPUT)

# Before: None
# Loop: 67 67
# Loop: 3 3
# Loop: 41 3
# Loop: 12 3
# Loop: 9 3
# Loop: 74 3
# Loop: 15 3
# Loop: 2 2
# Loop: -67 -67
# Smallest: -67

# ---------------------------------------------------------------

# Was just trying to figure out casting, pretty stupid if you ask me

# word = ' '
# newWord = str(word)
# print(newWord)

# ---------------------------------------------------------------

# SPLIT FUNCTION ATTEMPT

# def split(intc[]):
#     numba1 = bunchaTings[1]
#     numba2 = bunchaTings[2]
#     numba3 = bunchaTings[3]
#     numba4 = bunchaTings[4]

# split(bunchaTings[])

# Initiating a string (same as how 'ifstream myFile' fills a string when reading a line)
# str = 'penis, balls, poo, taint tickler, bootyhole, pomade, one fucking single lightbulb'
# arr = str.split(', ') # split() parameters: (delimeter (for example: ','),  maxsplit (most splits it will make, default value is -1))
# counter = len(arr)

# for i in range(counter):
#     print(arr[i])

# print('Array Length: ', counter)


# At this point, I found out there's a split funtion built in (above)

# Example of use:
    # void Game::readItems(string file) {
    #     ifstream myFile;
    #     myFile.open(file);
    #     string line;
    #     string arr[4];
    #     int count = 0 ;

    #     if (myFile.is_open()){
    #         while(getline(myFile, line)){
    #             split(line, ',', arr, 4);
    #             items[count].setIName(arr[0]);
    #             items[count].setIRarity(arr[1]);
    #             items[count].setIDescription(arr[2]);
    #             items[count].setIPrice(stoi(arr[3]));
    #             count++;
    #         }
    #     }
    #     else{
    #         return;
    #     }
    # }

# ---------------------------------------------------------------

# from asyncore import read
# from fileinput import filename
# import os

# fileName = 'boobs.txt'
# lineCount = 0
# openF = open(fileName, 'r')
# arr = []

# for i in openF:
#     line = i
#     lineCount+=1
#     arr = line.split(', ')

# size = range(len(arr))

# for x in size:
#     print(arr[x])

# print('Line Count: ' + str(lineCount) + '\nSplit Count: ' + str(len(size)))

# ---------------------------------------------------------------

# Dictionary practice

# dict = dict()

# dict['Name'] = input('Enter Name: ')
# dict['Age'] = input('Enter Age: ')
# print(dict)

# VS array[] (list)

# peopleName = [] # Array to hold names
# peopleAge = [] # Array to hold ages associated with names
# peopleAdded = 0 # Keeps track of number of people added, helpful for getting information from arrays
# # Instead of initializing value of 0 here, can use len(peopleName) or len(peopleAge) after 'done'

# while True:
#     peopleName.append(input('Enter Name: ')) # Adds name to end of the dynamic array
#     peopleAge.append(input(peopleName[peopleAdded] + "'s Age: ")) # Adds age to end of dynammic array
#     peopleAdded+=1

#     addMore = input('Would you like to add another person? (y/n): ') # Choice to end the program

#     if addMore == 'y' or addMore == 'Y':
#         continue
#     elif addMore == 'n' or addMore == 'N':
#         break

# print('Number of People added: ', peopleAdded) # Total people in the list

# print('List of names added:')
# for i in range(peopleAdded):
#     print(' ' + str((i+1)) + '. ' + str(peopleName[i]))

# choice = int(input('Which person would you like to view?: '))

# print('Name: ' + peopleName[choice-1])
# print('Age: ' + peopleAge[choice-1])

# ---------------------------------------------------------------

# TESTING XML TREES

# import xml.etree.ElementTree as ET

# data = '''<person>
#     <name>Colin</name>
#     <phone type="int1">
#         908 380 5327
#     </phone>
#     <email hide="yes"/>
# </person>'''

# tree = ET.fromstring(data)
# print('Name: ', tree.find('name').text)
# print('Attr: ', tree.find('email').get('hide'))

# ---------------------------------------------------------------

# Trying to figure out different operators (mainly confused on **)

x = 3
y = 2

print(x**y)

# output is 9, (**) is EXPONENTS