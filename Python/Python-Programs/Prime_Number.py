a = int(input("Enter a number: "))
    
prime=True
for i in range(2,a):
    if a%i==0:
        prime=False
    break

if prime:
    print("Number is prime")
else:
    print("Not prime")    