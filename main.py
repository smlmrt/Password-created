import random
import string

def genel_sifre(uzunluk,seviye, output = []):
    karakter = string.ascii_letters
    if seviye > 1:
        karakter = "{} {}".format(karakter,string.digits)
    if seviye > 2:
        karakter = "{} {}".format(karakter,string.punctuation)

    for i in range(uzunluk):
        output.append(random.choice(karakter))

    return "".join(output)

print(("-" * 30) + "\nPassword Generator\n" + ("-" * 30))

sifre_uzunlugu = int(input("uzunluk: "))
sifre_seviye = int(input("seviye: "))

sifre = genel_sifre(sifre_uzunlugu , sifre_seviye)
print("\nYour password is: {}".format(sifre))