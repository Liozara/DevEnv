def factorielle(n):
    if (n == 1):
        return 1
    else:
        return n * factorielle(n - 1)

def puissance(a, b):
    if b == 0:
        return 1
    else:
        return a * puissance(a, b - 1)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
if __name__ == "__main__":
    #print(factorielle(5))
    #print(puissance(5,2))
    for i in range(10):
        print(fibonacci(i))