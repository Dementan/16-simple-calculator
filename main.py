#write a simple calculator program

a = int(input("Enter Number1: "))
b = int(input("Enter Number2: "))
symbol = input("Enter the sign of the operation (+,-,/,*): ")
#set 4 functions for 4 operators(+,-,*,/)
if symbol == "+":
    print(a+b)
elif symbol == "-":
    print(a-b)
elif symbol == "*":
    print(a*b)
elif symbol == "/" and b != 0:
    print(a/b)
elif symbol == "/" and b == 0:
    print("Zero division error!")
