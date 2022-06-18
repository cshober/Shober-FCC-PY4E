# Initial time test - "11:06 PM" / "2:02"

# AM/PM is set inside this function as well
def setStartPieces(start):
  global startTime
  startTime = start.split(':')

  tempMin = startTime[1].split(' ')
  startTime[1] = tempMin[0]

  global period
  period = tempMin[1].lower()

  # Putting into 24 hour time
  if period == 'pm':
    startTime[0] = int(startTime[0]) + 12

# Duration pieces are set here
def setDurationPieces(duration):
  global durationTime
  durationTime = duration.split(':')

  return durationTime

# Change day of week
def getDay(day, daysPassed):
  arrDays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
  dayIndex = arrDays.index(day.lower())

  easyDay = daysPassed % 7
  newIndex = easyDay + dayIndex

  if newIndex < 7:
    return arrDays[newIndex].capitalize()
  else:
    newIndex -= 7
    return arrDays[newIndex].capitalize()

# Adds Duration to Start - calculates days passed, returns a string with all data
def add_time(start, duration, day=-1):
  # Initializing and defining global variables
  setStartPieces(start)
  setDurationPieces(duration)
  daysPassed = 0
  
  # Add Duration to Start
  totalHours = int(startTime[0]) + int(durationTime[0])
  totalMins = int(startTime[1]) + int(durationTime[1])

  # Calculating number of days passed
  while totalHours >= 24:
    totalHours -= 24
    daysPassed += 1

  # Calculating extra hours to add on if totalMins >= 60 
  while totalMins >= 60:
    totalMins -= 60
    totalHours += 1

    if totalHours == 24:
      daysPassed+=1

  # Get FINAL AM/PM Value
  if totalHours < 12 or totalHours == 24:
    period = 'AM'
  elif totalHours >= 12 and totalHours < 24:
    period = 'PM'
  else:
    print('something went horribly wrong')

  # Change back to 12 hour time
  if period == 'PM' or totalHours == 24:
    totalHours -= 12

    # Sets total hours back to 12 if time is 12pm (which would be 0 after the subtraction above)
    if totalHours == 0:
      totalHours = 12

  # Cast back to strings for later
  if totalMins < 10:
    totalMins = '0' + str(totalMins)
  
  totalMins = str(totalMins)
  totalHours = str(totalHours)
  strDays = str(daysPassed)
  
  # Store FINAL Time - all calculations done, put all data into a single concatenated string
  if day == -1:
    if daysPassed == 0:
      new_time = totalHours + ':' + totalMins + ' ' + period
    elif daysPassed == 1:
      new_time = totalHours + ':' + totalMins + ' ' + period + ' (next day)'
    else:
      new_time = totalHours + ':' + totalMins + ' ' + period + ' (' + strDays + ' days later)'
  else:
    if daysPassed == 0:
      new_time = totalHours + ':' + totalMins + ' ' + period + ', ' + getDay(day, daysPassed)
    elif daysPassed == 1:
      new_time = totalHours + ':' + totalMins + ' ' + period + ', ' + getDay(day, daysPassed) +' (next day)'
    else:
      new_time = totalHours + ':' + totalMins + ' ' + period + ', ' + getDay(day, daysPassed) +' (' + strDays + ' days later)'
    

  return new_time
  
  getDay(day, daysPassed)
