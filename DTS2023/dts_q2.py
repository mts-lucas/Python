def isNumberInFibonacci(number):

    penult = 0
    last = 1
    fibo = [penult, last]

    while (last <= number):
        newlast = last + penult
        fibo.append(newlast)
        penult = last
        last = newlast

    if number not in fibo:
        return False

    return True


print(isNumberInFibonacci(8))
