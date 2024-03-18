import math

a = float(input("Masukan nilai sisi a : "))
b = float(input("Masukan nilai sisi b : "))
c = float(input("Masukan nilai sisi c : "))

s = (1 / 2) * (a + b + c)
L = math.sqrt((s* (s-a) * (s-b) *  (s-c)))
K = a + b + c

print ("Luas segitiga Heron :", L)
print( "Keliling segitga Heron :", K)