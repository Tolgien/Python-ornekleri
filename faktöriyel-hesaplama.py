import sys


def faktoriyel(num: int):
    if num >= 1:
        return num * faktoriyel(num - 1)

    else:
        return 1


try:
    n = int(input("Lütfen bir sayı girin: "))

except ValueError:
    print("Lütfen tam sayı girin!")
    sys.exit()

if n < 0:
    print("Lütfen pozitif bir tam sayı girin:")
else:
    print(f"Girdiğiniz {n} sayısının faktoriyeli: {faktoriyel(n)}")
