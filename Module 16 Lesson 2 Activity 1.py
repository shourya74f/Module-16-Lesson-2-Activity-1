input("Set a bit - OR turns it on. Press Enter: ")
print("5= ", bin(5)[2:])
print("5|2= ", 5|2, "Binary: ", bin(5|2)[2:])
input("0 a bit - AND turns it on. Press Enter: ")
print("7= ", bin(7)[2:])
print("7&5= ", 7&5, "Binary: ", bin(7&5)[2:])
n=int(input("Enter a number: "))
g=input("Is it a power of 2: ")
input("Power of 2 - Power is on. Press Enter: ")
if n>0 and n&(n-1)==0:
    print(n, "Binary: ", bin(n)[2:], "Power of 2, your guess: ", g)
else:
    print(n, "Binart: ", bin(n)[2:], "Not a power of 2, your guess: ", g)