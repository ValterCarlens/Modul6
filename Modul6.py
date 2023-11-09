import os
os.system('cls')

#uppgift1
"""
def my_function(x):
    return 5 + x

print(my_function(3))

"""
#uppgift2
"""
def namn(x):
    print(x)

namn("Valter")
"""

#uppgift3
"""
def tal(x):
    return 5 * x

tal = (tal(4)) 

for x in range (0,10):
    print(tal)
"""

#uppgift 4
"""
1.skapa lista "deklarera"
2.printa namnen och fråga om man vill ändra namn och vilket namn man vill ändra och ger alternativen: ändra,ta bort,lägg till  ja/nej(print) 
3.input(nytt namn) eller input(ta bort namn) namn.remove
4.lägger till nytt namn och printar nya namnenoch vilket namn man har lagt till
5.frågar igen vad man vill göra och rep
"""
"""
list_names = ["Valter", "David", "Abdi"]

def list_name():
    number=1
    for name in list_names:
        print(f"{number}) {name} ")
        number+=1
    


def add_name(name):
    list_names.append(name)

while True:
    list_name()

    val=int(input("1.lägg till , 2.ändra , 3.ta bort "))

    if val == 1:
        name=input("Nytt namn: ")
        add_name(name)

    elif val == 2:
        name=int(input("Vilket namn vill du ändra? "))
        print(name)
        new_name=(input("Vad ska det nya namnet vara? "))
        list_names[name]=new_name
        print(name)
        

    

    elif val == 3:
        ta_bort_bil=input("Vilket namn vill du ta bort? ") 
        list_names.remove(ta_bort_bil)

    print(list_names)

    val_avsluta=input("vill du avsluta?  (Ja/Nej)")

    if val_avsluta ==("Ja"):
        print("Färdig med listan!")
        exit()

    elif val_avsluta ==("Nej"):
        continue
"""

#uppgift 5

import os
os.system("cls")

def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y

print("1,Addition")
print("2,subtraction")
print("3,multiplikation")
print("4.divition")

while True:
    svar=input("Vilket räknesätt? 1/2/3/4" )

    if svar in("1", "2", "3", "4", ):
        try:
            nummer1 = float(input("Första nummer:"))
            nummer2 = float(input("Andra nummer"))
        except ValueError:
            print("Ogiltig input, använd nummer")
            continue

        if svar == "1":
            print(nummer1 + nummer2)

        elif svar == "2":
            print(nummer1 - nummer2)
        
        elif svar == "3":
            print(nummer1 * nummer2)

        elif svar == "4":
            print(nummer1 / nummer2)

        ny_calculation=input("Vill du göra en till räkning? (Ja/Nej) ")

        if ny_calculation =="Nej":
            print("Tack för att du spelade!")
            break

        else:
            print("ogiltig input")
