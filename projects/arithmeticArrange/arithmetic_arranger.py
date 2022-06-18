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
    if '*' in operator or '/' in operator:
        return "Error: Operator must be '+' or '-'."

    # Check the digits
    for i in range(len(opOne)):
        if not (opOne[i].isdigit() and opTwo[i].isdigit()):
            return "Error: Numbers must only contain digits."

    # Check the length
    for i in range(len(opOne)):
        if len(opOne[i]) > 4 or len(opTwo[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    first_line = []
    second_line = []
    third_line = []
    fourth_line = []

    for i in range(len(opOne)):
        if len(opOne[i]) > len(opTwo[i]):
            first_line.append(" "*2 + opOne[i])
        else:
            first_line.append(" "*(len(opTwo[i]) - len(opOne[i]) + 2) + opOne[i])

    for i in range(len(opTwo)):
        if len(opTwo[i]) > len(opOne[i]):
            second_line.append(operator[i] + " " + opTwo[i])
        else:
            second_line.append(operator[i] + " "*(len(opOne[i]) - len(opTwo[i]) + 1) + opTwo[i])

    for i in range(len(opOne)):
        third_line.append("-"*(max(len(opOne[i]), len(opTwo[i])) + 2))

    if answer:
        for i in range(len(opOne)):
            if operator[i] == "+":
                ans = str(int(opOne[i]) + int(opTwo[i]))
            else:
                ans = str(int(opOne[i]) - int(opTwo[i]))

            if len(ans) > max(len(opOne[i]), len(opTwo[i])):
                fourth_line.append(" " + ans)
            else:
                fourth_line.append(" "*(max(len(opOne[i]), len(opTwo[i])) - len(ans) + 2) + ans)
        arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line) + "\n" + "    ".join(fourth_line)
    else:
        arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line)
    return arranged_problems