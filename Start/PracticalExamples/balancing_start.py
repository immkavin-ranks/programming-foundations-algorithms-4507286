# Example file for Programming Foundations: Algorithms by Joe Marini
# Use a stack to see if a programming statement is balanced


def is_balanced(thestr):
    # TODO: Your code goes here
    stack = []
    checker = {"}": "{", "]": "[", ")": "("}
    for c in thestr:
        if c in checker.values():
            stack.append(c)
        elif c in checker.keys():
            if len(stack) == 0:
                return False
            test = stack.pop()
            if checker[c] != test:
                stack.append(test)

    return len(stack) == 0


test_statements = [
    "print('Hello World!')",
    "a(x[i]) == b(x[i])",
    "{c for c in a(x)}",
    "Hello!)",
    "(This is not [balanced)",
    "{{{[[(())]}}",
    "(",
    "}",
]

for statement in test_statements:
    print(f"{statement} balanced: {is_balanced(statement)}")
