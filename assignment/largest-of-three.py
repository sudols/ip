n1 = float(input("Enter first num: "))
n2 = float(input("Enter second num: "))
n3 = float(input("Enter third num: "))

if n1 >= n2 and n1 >= n3:
   largest = n1
elif n2 >= n1 and n2 >= n3:
   largest = n2
else:
   largest = n3

print("largest is: ", largest)
