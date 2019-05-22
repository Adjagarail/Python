def main():
    #Valeur de mon portfeuille
    wallet = 30000
    achat1 = 3000
    achat2 = 2000
    achat3 = 2500
    rabai = (achat1 + achat2 + achat3) * 25
    rabai_tot = rabai / 100
    reste = wallet - rabai_tot
    print("Vous avez depenser en tout " + str(rabai_tot) + " et il vous reste " + str(reste))


if __name__ == '__main__':
    main()