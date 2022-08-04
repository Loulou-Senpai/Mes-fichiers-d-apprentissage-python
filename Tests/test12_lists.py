
text = input("Entrer une chaine de la forme (email-pseudo-motdepass)").split("-")
print(text)

print("Salut {}! Ton email est: {} et ton mot de passe est: {}".format(text[1], text[0], text[2]))