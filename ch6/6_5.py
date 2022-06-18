# Take the included code that has a string in it and find the portion of the string after the ':'
# Then, convert to float point var

str = 'X-DSPAM-Confidence: 0.8475'

colPos = str.find(':') # Finds the colon
confNum = float(str[colPos+1:]) # changes it to a float point var, removing the space between the colon and numbers
print(confNum)