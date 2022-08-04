
def main():
    # Recolter premier note
    note1 = int(input("Entrer la premiere note"))
    # Recolter deuxieme note
    note2 = int(input("Entrer la deuxieme note"))
    # Recolter troisieme note
    note3 = int(input("Entrer la troisieme note"))
    # calculer la moyenne
    result = (note1 + note2 + note3) / 3
    #afficher resultat
    print("La moyenne est de " + str(result))


if __name__ == '__main__':
    main()