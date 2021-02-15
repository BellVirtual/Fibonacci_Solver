def fib_solver(num):
    fib = [0]
    fibnum = 1
    if num != 1:
        for i in range(num):
            fibnum += fib[i - 1]
            fib.append(fibnum)
        return fibnum
    elif num == 0 or 1:
        return 1
    else:
        print("Error, not a positive number")
