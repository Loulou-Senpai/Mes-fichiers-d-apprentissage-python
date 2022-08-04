
# DOESN'T WORK FOR A SHIT REASON THAT IDK WHAT IT IS
password = input("Entrer votre mot de passe")
password_lenght = len(password)

# Verifier si mdp + de 8 characteres
if password_lenght <= 8:
    print("Mot de passe trop court")
    print("Il devrait y avoir entre 8 et 16 characteres dans votre mot de passe")

elif password_lenght > 8 and password_lenght <= 12:
    print("Mot de passe moyen")

else:
    print("Mot de passe Parfait!")

print(password_lenght)