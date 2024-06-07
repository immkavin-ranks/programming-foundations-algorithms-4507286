# Example file for Programming Foundations: Algorithms by Joe Marini
# use recursion to implement a countdown counter


def countdown(x):
    if x == 0:
        print("done")
        return
    else:
        print(x, "...")
        countdown(x - 1)
        print(x, "hey") # after call stack returns

countdown(5)
