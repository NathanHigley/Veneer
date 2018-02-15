print ("IP = [a, b, c, d]")
print ("NetMask = [A, B, C, D]")
print("Inputs cannot be negative.")

print("IP")
a = input("\ta; ")
b = input("\tb; ")
c = input("\tc; ")
d = input("\td; ")

print("NetMask")
A = input("\tA; ")
B = input("\tB; ")
C = input("\tC; ")
D = input("\tD; ")

IP = [0, 0, 0, 0]
NMASK = [0, 0, 0, 0]


NMASK[0] = A
NMASK[1] = B
NMASK[2] = C
NMASK[3] = D

IP[0] = IP[0] + a
IP[1] = IP[1] + b
IP[2] = IP[2] + c
IP[3] = IP[3] + d

print NMASK #Can change
print IP #Can change
