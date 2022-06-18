# Completed
class Category:
    # Constructor
    def __init__(self, name):
        self.ledger = []
        self.amount = 0.0
        self.name = name
        print('weiner')

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for i in range(len(self.ledger)):
            items += f"{self.ledger[i]['description'][0:23]:23}" + f"{self.ledger[i]['amount']:>7.2f}" + '\n'
            total += self.ledger[i]['amount']

        output = title + items + "Total: " + str(total)
        return(output)

    # Returns 'FALSE' if amount is greater than the balance of the budget category and returns 'TRUE' otherwise
    def check_funds(self,amount):
        if self.amount < amount:
            return False
        else:
            return True

    # Method should append ledger in form of {'amount' : amount, 'description' : description}
    # If description is not included in CALL, leaves blank
    def deposit(self,amount,description=''):
        self.ledger.append({'amount' : amount, 'description' : description})
        self.amount += amount
    
    # Number passed to this method should be a negative number. If funds cannot be withdrawn, return "FALSE". Else, return "TRUE"
    def withdraw(self,withdrawAmt,description=''):
        if self.check_funds(withdrawAmt) == True:
            self.amount -= withdrawAmt
            self.ledger.append({"amount":-withdrawAmt,"description":description})
            return True
        else:
            # print('Not enough funds to perform the withdraw.')
            return False

    # Returns the balance in the ledger
    def get_balance(self):
        return self.amount

    # Accepts amt and new budget category
    def transfer(self, amount, transCategory):
        if self.check_funds(amount) != True:
            # print('Not enough funds to transfer.')
            return False
        else:
            self.withdraw(amount, 'Transfer to ' + transCategory.name)
            transCategory.deposit(amount, 'Transfer from ' + self.name)
            return True

def truncate(n):
    multiplier = 10
    return int(n * multiplier) / multiplier

def getWithdrawls(self):
    total = 0
    for item in self.ledger:
        if item['amount'] < 0:
            total += item['amount']
    return total

def getTotals(categories):
    total = 0
    breakdown = []
    for category in categories:
        total += getWithdrawls(category)
        breakdown.append(getWithdrawls(category))
    rounded = list(map(lambda x: truncate(x / total), breakdown))
    return rounded

def create_spend_chart(categories):
    res = "Percentage spent by category\n"
    i = 100
    totals = getTotals(categories)
    while i >= 0:
          cat_spaces = " "
          for total in totals:
              if total * 100 >= i:
                  cat_spaces += "o  "
              else:
                  cat_spaces += "   "
          res+= str(i).rjust(3) + "|" + cat_spaces + ("\n")
          i-=10
      
    dashes = "-" + "---"*len(categories)
    names = []
    x_axis = ""
    for category in categories:
          names.append(category.name)

    maxi = max(names, key=len)

    for x in range(len(maxi)):
        nameStr = '     '
        for name in names:
              if x >= len(name):
                  nameStr += "   "
              else:
                  nameStr += name[x] + "  "
        
        if(x != len(maxi) -1 ):
          nameStr += '\n'

          
        x_axis += nameStr

    res+= dashes.rjust(len(dashes)+4) + "\n" + x_axis
    return res