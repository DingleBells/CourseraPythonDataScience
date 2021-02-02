def naiveGCD(a, b):
    best = 0
    for number in range(1, a + b):
        if a % number == 0 and b% number == 0:
            best = number
    return best

def EuclidGCD(a, b):
    if b == 0:
        return a
    newa = a%b
    return EuclidGCD(b, newa)

print(EuclidGCD(3918848, 1653264))