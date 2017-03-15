number1 = float(input("Sisesta esimene number: "))
number2 = float(input("Sisesta teine number: "))
tehe = input("Vali tehe(+,-,*,/): ")
if tehe == "+":
    print(str(number1) + " ja " + str(number2) + " summa on " + str(number1+number2))
    print("summa")
elif tehe == "-":
    print(str(number1) + " ja " + str(number2) + " vahe on " + str(number1-number2))
elif tehe == "*":
    print(str(number1) + " ja " + str(number2) + " korrutis on " + str(number1*number2))
elif tehe == "/":
    print(str(number1) + " ja " + str(number2) + " jagatis on " + str(number1/number2))
else:
    print("Ei ole õige tehe.")

