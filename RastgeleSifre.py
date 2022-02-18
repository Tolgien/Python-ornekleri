import random

low="abcdefghijklmnopqrstuvwxyz"
upp="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="0123456789"
sym="!@#$%^&*"

all=low+upp+num+sym
uzunluk=8 #Yazılan rakam doğrultusunta rastgele şifre oluşturur.
sifre="".join(random.sample(all,uzunluk))
print(sifre)
