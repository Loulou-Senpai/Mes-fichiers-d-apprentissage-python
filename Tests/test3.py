
# variable de base
wallet = 5000
price = 4000

# Le prix est inférieur à 1000?
if price <= wallet:
    wallet -= price
    print("Vous avez acheté l'ordinateur et avez maintenant", wallet, "dollars!")
else:
    print("L'achat est impossible, vous n'avez que {} dollars et l'ordinateur vaut".format(wallet), price, "dollars.")