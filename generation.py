import hashlib

class generation():
    def __init__(self, login, mdp_md5):
        self.login = login
        self.mdp_md5 = mdp_md5

    def choix1(self): #Un a mis une lettre devant son nom, avant de rajouter à la fin son année de naissance
        date = 1900
        while date <= 2020:
            for i in list_alpha:
                mdp_clear = i + self.login + str(date)
                mdp_hash = hash_md5(mdp_clear)
                if mdp_hash == self.mdp_md5:
                    return mdp_clear
                    exit()
            date += 1

    def choix2(self): #Les autres aiment les animaux et ont dérivés leurs mots de passe de ceux-ci
        for i in list_animaux:
            mdp_clear = i
            mdp_hash = hash_md5(mdp_clear)
            if mdp_hash == self.mdp_md5:
                return mdp_clear

    def choix3(self): #L'un est classique
        log = self.login
        new_log = ""
        for i in range(len(log)):
            maj = i
            lettre = log[i]
            if (maj % 2) == 0:
                lettre = lettre.upper()
            new_log = new_log + lettre
            if hash_md5(new_log) == self.mdp_md5:
                mdp_clear = new_log
                return mdp_clear

    def choix4(self): #d'autres ont rajoutés des nombres devant ou derrière (max 3), et mis la première lettre ou pas en majuscule.
        for i in list_animaux:
            for nbr in range(0, 1000):
                if hash_md5(str(nbr) + i) == self.mdp_md5:
                    mdp_clear = str(nbr) + i
                    return mdp_clear

                elif hash_md5(str(nbr) + i.capitalize()) == self.mdp_md5:
                    mdp_clear = str(nbr) + i.capitalize()
                    return mdp_clear

                elif hash_md5(i + str(nbr)) == self.mdp_md5:
                    mdp_clear = i + str(nbr)
                    return mdp_clear

                elif hash_md5(i.capitalize() + str(nbr)) == self.mdp_md5:
                    mdp_clear = i.capitalize() + str(nbr)
                    return mdp_clear


    def choix5(self): #Un autre est plus complexe : il a changé toutes les voyelles par un nombre et mis le tout en majuscule.
        for i in list_animaux:
            mot = i
            for letter in mot:
                if letter in list_voyelles:
                    mot = mot.replace(letter, "_")
            for nbr in list_chiffres:
                if hash_md5(str.upper(mot.replace("_", nbr))) == self.mdp_md5:
                    mdp_clear = str.upper(mot.replace("_", nbr))
                    return mdp_clear


    def choix6(self): #Le suivant a pris le nom d'un animal, l'a mis à l'envers, et l'a dédoublé
        for i in list_animaux:
            rev = ""
            for letter in reversed(i):
                rev += letter
            if hash_md5(rev + rev) == self.mdp_md5:
                mdp_clear = rev + rev
                return mdp_clear


    def choix7(self): #Le dernier a seulement concaténé 2 animaux
        for i in list_animaux:
            mot1 = i
            for j in list_animaux:
                mot2 = j
                if hash_md5(mot1 + mot2) == self.mdp_md5:
                    mdp_clear = mot1 + mot2
                    return mdp_clear


    def choix8(self): #Trois d'entre eux utilisent des règles simples basées sur leur nom, avec optionnellement des nombres rajoutés
        for i in list_digits:
            if hash_md5(self.login + i) == self.mdp_md5:
                mdp_clear = self.login + i
                return mdp_clear

            elif hash_md5(str.capitalize(self.login) + i) == self.mdp_md5:
                mdp_clear = str.capitalize(self.login) + i
                return mdp_clear


def hash_md5(hash):
    return hashlib.md5(hash.encode()).hexdigest()

list_alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

list_voyelles = ["a", "e", "i", "o", "u", "y"]

list_chiffres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

list_digits = ["%04d" % x for x in range(10000)]

list_animaux = []

fichier = open("dico_animaux.txt")
for i in range(0, 250):
    list_animaux.append(fichier.readline().rstrip())

#test_choix1 = Generation("titi", "3fbc7080bf8e718d4e8edd2eb596d3a7")
#test_choix2 = Generation("tito", "6b42d00c4ca6ddc33a604c54b8ce4adc")
#test_choix3 = Generation("tata", "d31259e2b584d457fa45c2c7bb58f89d")
#test_choix4 = Generation("tutu", "16b620e2a95347ef8f3030e52900e8c5")
#test_choix5 = Generation("tyty" , "d4488ccf0e5f906d1c55ad35379eaf4c")
#test_choix6 = Generation("tatu", "22b1235b36d51ff7a96527cbb9cdf2b7")
#test_choix7 = Generation("tota", "3eeca09a177fb06bf02e3291e72bdfe5")
#test_choix8 = Generation("tuti", "a7d349a1dab3727b7442ed4de450e091")
