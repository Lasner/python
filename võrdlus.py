from random import randint

check = randint(0,9)
        
def loto():
    number = input("Sisesta üks täisarv 0-9: ")
    if number.isdigit() and int(number) <= 9:
        number = int(number)
        if number < check:
            print("Sisestatud number on väiksem, kui kontrollarv")  
            loto()
        elif number > check:
            print("Sisestatud number on suurem, kui kontrollarv")    
            loto()
        else:
            print("Olete võitnud!, võidunumber on " + str(check) + ".")
        
        
    else:
        print("Viga, sisesta täisarv 0-9!")
        loto()

loto()
        


             