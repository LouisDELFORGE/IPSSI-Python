from random import randint

selected_num = []

def array_check(checkNum):
    for i in range(len(selected_num)):
        if (selected_num[i-1] == checkNum):
            return False
            break

    return True

def numberHandler():
    if (len(selected_num) <= 5):
        number = input("Choisissez vos numero: ")
        try:
            int(number)
        except:
            print("\n Numero invalide")
            numberHandler()
            return

        if array_check(int(number)) and int(number) <= 100 and int(number) >= 0:
            selected_num.append(int(number))
            numberHandler()
        else:
            print("Numero deja choisis \n")
            numberHandler()
    else:
        generatedNumber = randint(0,100)
        if (not array_check(generatedNumber)):
            print("\n You won")
        else:
            print("\n Womp womp you lost")
            print("Number was " + str(generatedNumber))

numberHandler()