a = float(input("Masukan Nilai Pertama : "))
b = float(input("Maskan Nilai Kedua : "))
c = float(input("Masukan Nilai Ketiga : "))

if a > b and a > c:
    print(f"Bilangan{a} lebih besar dari bilangan {b} dan {c} ")
    
elif b > a and b > c:
    print(f"Bilangan{b} lebih besar dari bilangan {a} dan {c} ")

elif c > a and c > b:
    print(f"bilangan {c} lebih besar dari {a} dan {c}") 

elif a == b and a > c and b > c:
    print(f"bilangan {a} dan {b} sama besar, namun lebih besar dari {c}")

elif a == c and a > b and c > b:
    print(f"bilangan {a} dan {c} sama besar, namun lebih besar dari {b}")

elif b == c and b > a and c > a:
    print(f"bilangan {b} dan {c} sama besar, namun lebih besar dari {a}")
    
else :
     print (f"bilangan {a}, bilangan {b} dan bilangan {c} sama besar")