while True:
    parenthesize = []
    free = 0
    x = input("enter a code in python \n")
    for i in x:
        if i == '(':
            parenthesize.append(i)
        elif i == ')':
            if parenthesize:
                parenthesize.pop()
            else:
                parenthesize.append(i)
        elif i != '(' and i != ')':
            free += 1
    left = x.count('(')
    right = x.count(')')
    if not parenthesize:
        print(f'your code is correct has {left + right + free} characters with {right} ")" and {left} "(" ')
    else:
        print(f'your code has {left + right + free} characters with {right} ")" and {left} "(" and not correct')
