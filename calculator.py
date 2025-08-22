import addition
import subtraction
import multiplication

#function calling
choice=int(input("choice:"))
if choice == 1:
    print("addition operation")
    a,b=map(int,input().split())
    add=addition.add(a,b)
    print(add)

choice=int(input("choice:"))
if choice == 2:
    print("substraction operation")
    a,b=map(int,input().split())
    sub=subtraction.sub(a,b)
    print(sub)

choice=int(input("choice:"))
if choice == 3:
    print("multiplication operation")
    a,b=map(int,input().split())
    mul=multiplication.mul(a,b)
    print(mul)





