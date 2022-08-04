
print("Bonjour et bienvenue au cinema!")

age = input("Premierement, quel age avez-vous? ")
popcorn = 15

if age <= str(17):
    print("Parfait, donc un forfait pour jeune.")
    reponse = input("Voulez-vous du pop-corn avec cela? ")
    if reponse == "oui" or "Oui":
        print("D'accord! Le prix totale est de 12$!")
    else:
        print("D'accord! Le prix totale est de 7$!")
elif age >= str(18):
    print("Parfait, donc un forfait pour adulte.")
    reponse = input("Voulez-vous du pop-corn avec cela? ")
    if reponse == "oui" or "Oui":
        print("D'accord! Le prix totale est de 17$!")
    else:
        print("D'accord! Le prix totale est de 12$!")