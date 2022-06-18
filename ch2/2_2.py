#Calculate gross pay with user input hours and rate, print gross pay (use float)

hoursWorked = int(input('How many hours did you work?\n'))
payRate = float(input('What is your pay rate?\n'))
grossPay = hoursWorked * payRate

print('Gross Pay:', grossPay)