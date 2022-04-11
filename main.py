"""
Projet Demineur
Eduardo Plaza Milhoranzap
Arthur Rousseau
"""

# Imports :
import random as r


# Les classes :


class Case:
    """
    Chaque Case est constitué d'une valeur qui determine le nb de bombes au tour d'elle, ou si elle est une bombe.
    Il y a aussi un boléen qui nous dit si la case à était trouvé ou non.
    """

    def __init__(self):
        self.valeur = 0
        self.trouvee = False

    def Affichage(self):
        affichage = str(self.valeur)  # Son affichage est simplement sa valeur.

        return affichage


class Grille:
    """
    Une grille est une liste qui contient d'autres listes et des cases, dont le nombre peux varier selon la longueur
    et la largeur choisie. On y determine aussi le nombre de bombes qui doivent être placées.
    """

    def __init__(self):
        self.tab = []
        # --------------------------#
        self.Facile = (6, 6, 5)
        self.Moyen = (9, 9, 8)
        self.Difficile = (9, 9, 12)
        #---------------------------#
        self.longueur = 6
        self.largeur = 6
        self.nbBombes = 5


    def demande(self):

        mode = input("Choissisez un mode de jeu : facile / moyen / difficile\n ")

        if mode == "facile":
            self.longueur = self.Facile[0]
            self.largeur = self.Facile[1]
            self.nbBombes = self.Facile[2]

        elif mode == "moyen":
            self.longueur = self.Moyen[0]
            self.largeur = self.Moyen[1]
            self.nbBombes = self.Moyen[2]

        elif mode == "difficile":
            self.longueur = self.Difficile[0]
            self.largeur = self.Difficile[1]
            self.nbBombes = self.Difficile[2]


        else:
            print("Recopiez exactement l'une des options proposées.")
            return self.demande()


    def uploader(self,idListe,idCase):
        """
        Renvoie la liste des coordonnées des cases qui doivent être modifiés.
        On vas vérifier d'abord si la ligne selectionnée est la première ou la dernière, et de même pour la case, car
        les cases dans ces coordonnées ne sont pas entièrement entourées d'autres cases et cela peux causer des erreurs.
        Sinon, on vas simplement ajouter +1 à toutes les cases au tour de la case selectionée.
        Ligne et colone sont des variables qui nous permettent de modifier les coordonnées.
        """

        liste = []

        if idListe == 0 : # Verif sur la 1er ligne
            ligne = idListe

            if idCase == 0 : # Vérifi de la Première Case

                for k in range(2): # Double Boucle pour parcourir le tableau
                    ligne += k
                    for i in range(2):
                        colone = idCase
                        colone += i
                        liste.append((ligne, colone)) # Ajout du tupple contenant les deux co à la liste.
                return liste

            elif idCase == len(self.tab[idListe])-1 : # Verif dernière case

                for k in range(2):
                    ligne += k
                    for i in range(2):
                        colone = idCase - 1
                        colone += i
                        liste.append((ligne,colone))
                return liste

            else : # Si la case n'est ni la 1er ni la dernière

                for k in range(2):
                    ligne += k
                    for i in range(3):
                        colone = idCase - 1
                        colone += i
                        liste.append((ligne,colone))
                return liste

        elif idListe == len(self.tab)-1 : # Verifi de la dernière ligne
            ligne = idListe - 1

            if idCase == 0 :

                for k in range(2):
                    ligne += k
                    for i in range(2):
                        colone = idCase
                        colone += i
                        liste.append((ligne, colone))
                return liste

            elif idCase == len(self.tab[idListe])-1 :

                for k in range(2):
                    ligne += k
                    for i in range(2):
                        colone = idCase - 1
                        colone += i
                        liste.append((ligne,colone))
                return liste

            else: # Si la case selectionnée ne se trouve pas dans les bordures.

                for k in range(2):
                    ligne += k
                    for i in range(3):
                        colone = idCase - 1
                        colone += i
                        liste.append((ligne, colone))
                return liste

        else :


            if idCase == 0:

                for k in range(3):
                    ligne = idListe - 1
                    ligne += k
                    for i in range(2):
                        colone = idCase
                        colone += i
                        liste.append((ligne, colone))
                return liste

            elif idCase == len(self.tab[idListe]) - 1:

                for k in range(3):
                    ligne = idListe - 1
                    ligne += k
                    for i in range(2):
                        colone = idCase - 1
                        colone += i
                        liste.append((ligne, colone))
                return liste

            else:

                for k in range(3):
                    ligne = idListe - 1
                    ligne += k
                    for i in range(3):
                        colone = idCase - 1
                        colone += i
                        liste.append((ligne, colone))
                return liste


    def bombes(self):
        """
        Bombes est la methode responsable pour le polacement aléatoire des bombes, et aussi pour la mise à jour des
        valeurs des cases qui les entourent.
        """
        idListe = r.randint(0, (len(self.tab) - 1))
        idCase = r.randint(0, (len(self.tab[idListe]) - 1))

        if self.tab[idListe][idCase].valeur != 9:
            self.tab[idListe][idCase].valeur = 9

            liste = self.uploader(idListe,idCase)
            for k in range(len(liste)):
                co1 = liste[k][0]
                co2 = liste[k][1]
                if self.tab[co1][co2].valeur != 9 :
                    self.tab[co1][co2].valeur += 1

        else:
            return self.bombes()

        return self.tab


    def creer(self):
        """
        Créer est la methode qui nous permet de créer le tableau qui matérialise la grille du jeu. On utilise une double
        boucle pour créer les lignes et les colones, et on y fait appel à la methode bombes.
        """
        for i in range(self.longueur):
            self.tab.append([])
            for k in range(self.largeur):
                case = Case()
                self.tab[i].append(case)

        for z in range(self.nbBombes):
            self.bombes()

        return self.tab


    def __str__(self):
        """
        Pour l'affichage de la grille, affecte à chaque case non affichée l'affichage : '| ' et à une case affichée on
        remplace l'espace par la valeur de la case en question. A chaque fin de ligne on ajoute une barre et un saut de
        ligne pour l'esthétique.
        """
        affichage = ""
        for k in range(self.longueur):
            for i in range(self.largeur):

                if self.tab[k][i].trouvee == False:
                    affichage += "| "

                else:
                    affichage += "|" + self.tab[k][i].Affichage()

            affichage += "|" + "\n"

        return affichage


class Jeu:

    def __init__(self,grille):
        self.grille = grille
        self.isPlaying = True
        self.compteur = 0

    def gameOver(self,ligne,colone):

        winCondition = self.grille.largeur * self.grille.longueur - self.grille.nbBombes
        if self.grille.tab[ligne][colone].valeur == 9 and self.grille.tab[ligne][colone].trouvee == True :
            self.isPlaying = False
            print("Vous avez percuté une bombe dommage !")
            return self.isPlaying


        if self.compteur >= winCondition:
            self.isPlaying = False
            print("Vous avez gagné bravo !")
            return self.isPlaying

        else :
            return self.isPlaying

    def jouer(self):

        l = [str(k) for k in range(self.grille.largeur)]
        coordonnee = [0,0]

        demande = input("Donnez le numéro de la ligne : ")


        if demande in l and len(demande) == 1:
            coordonnee[0] = int(demande)

        else :
            print("Donnez les bonnes coordonees")
            return self.jouer()

        demande1 = input("Donnez le numéro de la colone : ")

        if demande1 in l and len(demande1) == 1:
            coordonnee[1] = int(demande1)

            return coordonnee

        else :
            print("Donnez les bonnes coordonees")
            return self.jouer()

    def voisin(self,coordonnee):

        listeDesVoisins = []
        couple = [0,0]

        for idLigne in range(-1, 2):
            for idColone in range(-1, 2):
                if coordonnee[0] + idLigne == coordonnee[0] and coordonnee[1] + idColone == coordonnee[1]:
                    pass

                elif not coordonnee[0] + idLigne < 0 and not coordonnee[0] + idLigne > (len(self.grille.tab) - 1):
                    couple[0] = coordonnee[0] + idLigne
                    if not coordonnee[1] + idColone < 0 and not coordonnee[1] + idColone > (len(self.grille.tab[idLigne]) -1):
                        couple[1] = coordonnee[1] + idColone

                        listeDesVoisins.append((couple[0], couple[1]))

        return listeDesVoisins

    def decouverte(self,coordonnee):

        caseSelect = self.grille.tab[coordonnee[0]][coordonnee[1]]
        caseSelect.trouvee = True
        self.compteur += 1


        if self.gameOver(coordonnee[0],coordonnee[1]) == False :
            return self.grille

        if caseSelect.valeur > 0 and caseSelect.valeur < 9:
            if not caseSelect.trouvee:
                caseSelect.trouvee = True
        else:
            listeVoisin = self.voisin(coordonnee)
            for i in range(len(listeVoisin)):
                co2 = listeVoisin[i]
                caseAutour = self.grille.tab[co2[0]][co2[1]]

                if caseAutour.valeur > 0 and caseAutour.valeur < 9:
                    if not caseAutour.trouvee:
                        caseAutour.trouvee = True
                        self.compteur += 1
                else:
                    if not caseAutour.trouvee and caseAutour.valeur == 0:
                        caseAutour.trouvee = True
                        self.decouverte(co2)


def initialisation():

    grille = Grille()
    grille.demande()
    grille.creer()
    return grille


def Play(grille):
    game = Jeu(grille)
    print(grille)

    while game.isPlaying == True :
        coordonnee = game.jouer()
        game.decouverte(coordonnee)
        print(grille)

    demande = input("Voulez-vous rejouer ? (Yes/No)")
    if demande == "Yes" or demande == "yes" :
        return Play(grille)

    else :
        print("Merci d'avoir joué, à la prochaine !")

# Lancement du Jeu
Play(initialisation())

