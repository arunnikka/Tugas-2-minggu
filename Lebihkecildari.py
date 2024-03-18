a = float(input("Masukan Nilai Pertama : "))
b = float(input("Maskan Nilai Kedua : "))
c = float(input("Masukan Nilai Ketiga : "))

if a < b and a < c:
    print(f"Bilangan {a} lebih kecil dari bilangan {b} dan {c} ")
    
elif b < a and b < c:
    print(f"Bilangan {b} lebih kecil dari bilangan {a} dan {c} ")
    
else :
    print(f"bilangan{c} lebih kecil dari bilangan {a} dan {b} ")