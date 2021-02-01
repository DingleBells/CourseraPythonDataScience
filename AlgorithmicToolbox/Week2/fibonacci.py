def recursiveFibonacci(n):
    if n <= 1:
        return n
    else:
        return recursiveFibonacci(n-1) + recursiveFibonacci(n-2)

def fibList(n):
    numlist = [0, 1]
    for i in range(2, n+1):
        numlist.append(numlist[i-1] + numlist[i-2])
    return numlist[-1]

