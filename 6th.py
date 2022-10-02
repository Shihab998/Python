from math import factorial


num=int(input("Enter your numbr: "))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print(f"The factorial of {num} is {factorial}")    