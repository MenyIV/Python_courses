import math

def spotreba(vyska,sirka,vydatnost):
    obsah = vyska * sirka
    pocet_baleni = obsah / vydatnost
    print(f"Bude potřeba {math.ceil(pocet_baleni)}Ks plechovek")
    return pocet_baleni

vyska = int(input("Zadej výšku zdi"))
sirka = int(input("Zadej šířku zdi"))
vydatnost = 10

spotreba(vyska,sirka,vydatnost)





