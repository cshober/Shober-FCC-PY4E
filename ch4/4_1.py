# Using the pay program from earlier, rewrite the program but use functions to have it complete the same task

def computePay(hours, rate):
    if hoursWorked < 40:
        grossPay = hoursWorked * payRate
    else:
        grossPay = ((hoursWorked - 40) * (payRate * 1.5)) + (40 * payRate)

    return grossPay # Returning explicit value from computations performed inside function

while True:
    hoursWorked = input('Enter Hours Worked: ')

    try:
        hoursWorked = int(hoursWorked)
        break # Breaks out of the current loop to whatever code is right outside
    except:
        print('Enter a numerical value!')
        continue # Directs code back to the top of the loop to run again

while True:
    payRate = input('Enter Pay Rate: ')

    try:
        payRate = float(payRate)
        break
    except:
        print('Enter a numerical value!')
        continue

print('Gross Pay:', computePay(hoursWorked, payRate))