def main():
    age = input("Donnez votre age")
    age = int(age)
    ticket = 15000
    if age <= 3:
        print("Votre Ticket est gratuit")
    elif (age >= 4) and (age < 18):
        somme = (ticket * 25) / 100
        print("Votre ticket vous revient a " + str(somme) + " FCFA")
    elif age >= 65:
        somme = (ticket * 75) / 100
        print("Vous ticket vous revient a " + str(somme) + " FCFA")
    else:
        print("Vous n'avez pas de rabai payez " + str(ticket) + " FCFA pour voyager")


if __name__ == '__main__':
    main()