
usernames = ["Loulou-Senpai", "ZeyaTsu", "Ruina_Last", "Sacul", "PewPew"]
print("List of online players:", usernames[0], usernames[1], usernames[2], usernames[3], usernames[4])

usernames[3:5] = ["A_Peanut", "TbhILuvH"]
print("De nouveaux joueur sont connectes!")
print("List of online players:", usernames[0], usernames[1], usernames[2], usernames[3], usernames[4])

# Extend (multi) or Append (one) works
usernames.append("Banana")
print("Un autre utilisateur s'est connecté")
print("List of online players:", usernames[0], usernames[1], usernames[2], usernames[3], usernames[4], usernames[5])

usernames.remove("A_Peanut")
print("Un utilisateur s'est déconnecté.")
print("List of online players:", usernames[0], usernames[1], usernames[2], usernames[3], usernames[4])

usernames.clear()
print("Tout le monde s'est déconnecté.")