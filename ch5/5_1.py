# Write program that repeatedly reads numbers until the user enters 'done'. after, print out {total, count, average of the numbers}
# If user enters != number, detect and use try and except

def average(sum, count):
    totAverage = sum / count
    return totAverage

sumTotal = 0
countTotal = 0
avg = 0.0
intInput = 0
complete = False

while not complete: # done loop
    while True: # constant
        temp = input('Enter a number: ') # Used to take temporary user inputs

        if temp == 'done':
            if countTotal == -1:
                print("You haven't entered a number!")
                continue
            else:
                complete = True
                break
        else:
            try:
                intInput = int(temp) 
                break
            except:
                print('do better')
                continue

    if not complete:
        # if all tests are passed and not 'done'
        sumTotal += intInput
        countTotal += 1
        continue
    else:
        break

# After 'done'
avg = average(sumTotal, countTotal)
print(sumTotal, countTotal, avg)