a = input("Message: ")
b = input("Key: ")
binary_a = []
binary_b = []
for char in a:
    binary = bin(ord(char))[2:]
    binary_a.append(binary)
for char in b:
    binary = bin(ord(char))[2:]
    binary_b.append(binary)
if len(binary_a) == len(binary_b): #and binary_a == binary_b:
    print("Good!")
    c= binary_a + binary_b
    result = bin(с)[2:]
    print (result)
else:
    print("Oops!")







