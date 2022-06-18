def arithmetic_arranger(problems, answer=False):
    # Check the number of problems
    if len(problems) > 5:
        return "Error: Too many problems."
    
    opOne = []
    opTwo = []
    operator = []

    for problem in problems:
        pieces = problem.split()
        
        opOne.append(pieces[0])
        operator.append(pieces[1])
        opTwo.append(pieces[2])

    # Check for * or /
    if "*" in operator or "/" in operator:
        return "Error: Operator must be '+' or '-'."

    # Check digits
    for i in range(len(opOne)):
        if not (opOne[i].isdigit() and opTwo[i].isdigit()):
            return "Error: Numbers must only contain digits."

    # Check length
    for i in range(len(opOne)):
        if len(opOne[i]) > 4 or len(opTwo[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    firstNum = []
    secondNum = []
    divider = []
    solution = []

    for i in range(len(opOne)):
        if len(opOne[i]) > len(opTwo[i]):
            firstNum.append(" "*2 + opOne[i])
        else:
            firstNum.append(" "*(len(opTwo[i]) - len(opOne[i]) + 2) + opOne[i])

    for i in range(len(opTwo)):
        if len(opTwo[i]) > len(opOne[i]):
            secondNum.append(operator[i] + " " + opTwo[i])
        else:
            secondNum.append(operator[i] + " "*(len(opOne[i]) - len(opTwo[i]) + 1) + opTwo[i])

    for i in range(len(opOne)):
        divider.append("-"*(max(len(opOne[i]), len(opTwo[i])) + 2))

    if answer:
        for i in range(len(opOne)):
            if operator[i] == "+":
                ans = str(int(opOne[i]) + int(opTwo[i]))
            else:
                ans = str(int(opOne[i]) - int(opTwo[i]))

            if len(ans) > max(len(opOne[i]), len(opTwo[i])):
                solution.append(" " + ans)
            else:
                solution.append(" "*(max(len(opOne[i]), len(opTwo[i])) - len(ans) + 2) + ans)
        finalSol = "    ".join(firstNum) + "\n" + "    ".join(secondNum) + "\n" + "    ".join(divider) + "\n" + "    ".join(solution)
    else:
        finalSol = "    ".join(firstNum) + "\n" + "    ".join(secondNum) + "\n" + "    ".join(divider)
    return finalSol