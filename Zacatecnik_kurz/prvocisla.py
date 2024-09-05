# zjistit zda je to prvocislo
# je dělitelné 1 a ssebou samým

# bude list prvočísel 
# a nekonečná smyčka která zkusí vydělit číslo všemi z listu 
# a když to neprojde tak je to prvočíslo které se přidá do listu

# je dělitelné 2 (4,6,8)
# je dělitelné 3 (6,9,12,15)

prvocisla_list = ["1"]
pocet_prvocisel = int(input("kolik chceš prvočísel?"))

cislo = 1

while pocet_prvocisel != len(prvocisla_list):
    for each in range (0,len(prvocisla_list)):
        print(f"pruchod cislo {each}")
        print(f"testuji číslo {prvocisla_list[each]}")
        podminka1 = cislo//int(prvocisla_list[each])
        podminka2 = cislo/int(prvocisla_list[each])
        
        if podminka1 == 0 and podminka2 > 1:
            
            print (f"Prvocislo nalezeno {cislo}")
            prvocisla_list.append(cislo)
            break
        else:
            cislo +=1
            print (cislo)
            print (prvocisla_list)