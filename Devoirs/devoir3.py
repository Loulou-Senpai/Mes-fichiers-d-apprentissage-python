from random import shuffle

mots = input("Entrer une  liste de mots separes par ce charactere: / ").split("/")
print(mots)

shuffle(mots)
print(mots)

words_len = len(mots)
if words_len < 10:
    print(mots[0], mots[1])

else:
    print(mots[words_len -1], mots[words_len -2], mots[words_len -3])