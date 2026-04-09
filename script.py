import math

a = int(input("Nhập độ dài cạnh a: "))
b = int(input("Nhập dộ dài cạnh b: "))
c = int(input("Nhập độ dài cạnh c: "))

if pow(a,2) + pow(b,2) == pow(c,2) or pow(a,2) + pow(c,2) == pow(b,2) or pow(b,2) + pow(c,2) == pow(a,2):
    print(f"Chu vi tam giác =  {a+b+c}")
    print(f"Diện tích tam giác = {0.5*a*b}")
else:
    print("KHÔNG PHẢI TAM GIÁC VUÔNG!!!")

