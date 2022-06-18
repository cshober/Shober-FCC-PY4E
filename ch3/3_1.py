# Calculate gross pay under 40 hours with user input hours and rate, print gross pay (use float)
# CONDITION: Any work done over 40 hours, multiply 1.5x the rate

hoursWorked = int(input('How many hours did you work?\n'))
payRate = float(input('What is your pay rate?\n'))

if hoursWorked < 40:
    grossPay = hoursWorked * payRate

grossPay = ((hoursWorked - 40) * (payRate * 1.5)) + (40 * payRate)

print('Gross Pay:', grossPay)