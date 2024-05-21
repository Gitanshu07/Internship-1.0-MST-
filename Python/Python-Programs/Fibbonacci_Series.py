n = int(input("Enter length of fibonacci series!!"))

def fibnacci(n):
    a = 0
    b = 1
    for i in range(n):
        c = a+b
        a = b
        b = c
        print(a,b,c)
        
    fibnacci(n)