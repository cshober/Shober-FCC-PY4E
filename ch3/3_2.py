# Rewrite the pay program using 'try' and 'except' to handle non-numeric inputs

check = 0

while not check:
    hoursWorked = input('Enter Hours Worked: ')

    try:
        hoursWorked = int(hoursWorked)
        check = 1
    except:
        print('Enter a numerical value!')

check = 0

while not check:
    payRate = input('Enter Pay Rate: ')

    try:
        payRate = float(payRate)
        check = 1
    except:
        print('Enter a numerical value!')

if hoursWorked < 40:
    grossPay = hoursWorked * payRate
else:
    grossPay = ((hoursWorked - 40) * (payRate * 1.5)) + (40 * payRate)

print('Gross Pay:', grossPay)