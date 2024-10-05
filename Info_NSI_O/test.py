def triangle(n):
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end =" ")
        print("")

def triangle_2(n):
    for i in range (1, n + 1):
        print("*" * i)

def triangle_3(n):
    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            print(" ", end="")
        for j in range(1, i + 1):
            print("*", end="")
        print("")
        
def triangle_isocele(n):
    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            print("  ", end="")
        for j in range(1, 2*i - 1 + 1):
            print("* ", end="")
        print("")
    
def tronc(x, n):
    for i in range(1, n + 1):
        for j in range(1, x - 1 ):
            print(" ", end="")
        for j in range(1, n + 1):
            print("|", end="")
        print("")



if __name__ == "__main__":
    #triangle(3)
    #triangle_2(4)
    #triangle_3(4)
    triangle_isocele(12)
    #tronc(12, 9)