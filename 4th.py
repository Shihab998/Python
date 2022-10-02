num=int(input("Enter your numbr: "))
prime=True
for i in range(2,num):
    if(num%i==0):
        prime=False
        break
if prime:
    print("This is prime number")
else:
    print("This is not a prime number")