from math import ceil

pikkus = int(input("Sisesta pikkus tükkides: "))
laius = int(input("Sisesta laius tükkides: "))
kõrgus = int(input("Sisesta kõrgus tükkides: "))
tk_pakk = int(input("Mitu tükki on ühes pakis: "))

def pakke():
    tk_arv = pikkus*laius*kõrgus
    pakk_arv = tk_arv/tk_pakk
    #print("Sul on vaja " + str(round(pakk_arv + 0.49))+ " pakki.")
    print("Sul on vaja " + str(ceil(pakk_arv))+ " pakki.")
    

pakke()