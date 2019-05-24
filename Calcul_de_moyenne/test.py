def main():
    #Demander premiere note
    note1 = int(input("Veuillez entrez votre premiere note"))
    #Demander seconde note
    note2 = int(input("Veuillez entrez votre seconde note"))
    #Demander troisieme note
    note3 = int(input("Veullez entrez votre troisieme note"))
    #Calcul de la moyenne de l'eleve
    resultat = (note1 + note2 + note3) / 3
    print("Apres calcul vous avez une moyenne de" + str(resultat))


if __name__ == '__main__':
    main()