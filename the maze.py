while True :

    nombre_de_dents = 30
    print("Bienvenue dans le labyrinthe, trois ouvertures se présente à vous, vous pouvez aller : tout droit, gauche ou droite")
    print()
    print("_|^|_")
    print("< ¤ >")
    print("-- --")
    print()
    direction =input("->")

    def centre ():
        print("vous êtes revenu au point de départ, voulez vous trouner à gauche, à droite ou aller tout droit ?")
        print()
        print("| \_|^|_")
        print("|  < ¤ >")
        print("----- --")
        print()



    if direction == "gauche" :
        print ("bien choisi maintenant, deux choix s'offrent à vous, voulez vous aller tout droit ou à gauche ?")
        print()
        print("|^|_| |_")
        print("|¤ >    ")
        print("----- --")
        direction = input("->")

        while direction != "tout droit" and direction != "droite":

            if nombre_de_dents > 0:
                print("vous venez de vous cogner contre un mur et perdez une dents, bravo")
                nombre_de_dents = nombre_de_dents - 1
                direction = input("->")
            else:
                print("vous navez plus de dents et vous vous fracturez un os")
                direction = input("->")

        if direction == "droite":
            centre()
            direction = input("->")
            if direction == "gauche":
                print("vous êtes revenu ici mais à cause de tout les mouvement, une parois c'est effondré et vous avez failli perde une jambe, vous ne pourez plus revenir en arrière")
                print()
                print("|^|_| |_")
                print("|¤|    ")
                print("----- --")
                direction = input("->")

                while direction != "tout droit":

                    if nombre_de_dents > 0:
                        print ("vous venez de vous cogner contre un mur et perdez une dents, bravo")
                        nombre_de_dents=nombre_de_dents-1
                        direction = input("->")
                    else :
                        print("vous navez plus de dents et vous vous fracturez un os")
                        direction = input("->")

            elif direction == "tout droit":
                print ("bug du système, il ne faux pas être indecie dans ce labyrinthe !")
                print("vous mourrez sans explication (probablement un bug)")
                exit(0)
            elif direction == "droite":
                print("bug du système, il ne faux pas être indecie dans ce labyrinthe !")
                print("vous mourrez sans explication (probablement un bug)")
                exit(0)

            else:
                print("vous n'avez pas la capacité mentale nessessaire pour faire ce labyrinthe et vous mourez tandis que vous essayez de faire fonctionner votre cerveau")

            print("")
        elif direction == "tout droit":
            print ("")
            print("vous continuez et entendez un tremblement venir de la gauche")
            print()
            print("__|^|")
            print(" < ¤|")
            print("--| |_| |_")
            print("  | |     ")
            print("------- --")
            direction = input("->")
            while direction != "tout droit" and direction !="gauche":

                if nombre_de_dents > 0:
                    print("vous venez de vous cogner contre un mur et perdez une dents, bravo")
                    nombre_de_dents = nombre_de_dents - 1
                    direction = input("->")
                else:
                    print("vous navez plus de dents et vous vous fracturez un os")
                    direction = input("->")

            if direction == "gauche":
                print("")
                print ("un monstre vous avale brutalement")
                exit(0)

            elif direction == "tout droit":
                print("Vous avez trouver la fin du labyrinte bravo !")
                print("  ___  ")
                print(" [ Δ ]")
                print("__| |")
                print("__  |")
                print("  | |_| |_")
                print("  | |     ")
                print("------- --")
                exit(0)

    elif direction == "en arrière":
        print ("FUILLARD")
        print ("vous faite face à l'eclaire de clolère du narateur et mourrez")
        exit (0)

    elif direction == "tout droit":
        print("vous vous retrouvez face à un bug du labirinthe, retournez sur vos pas !")
        print()
        print("| # |")
        print(" \¤/ ")
        print("_| |_")
        print("     ")
        print("-- --")
        print()

        direction=input("->")

        while direction != "tout droit" and direction != "en arrière":

            if nombre_de_dents > 0:
                print("vous venez de vous cogner contre un mur et perdez une dents, bravo")
                nombre_de_dents = nombre_de_dents - 1
                direction = input("->")
            else:
                print("vous navez plus de dents et vous vous fracturez un os")
                direction = input("->")

        if direction == "tout droit":
            print ("je n'ai pas fini cette partit du code n'avance plus")
            print()
            print(".")
            print("..")
            print("...")
            print ("vous avancez guidé par votre intuition")
            print()
            print("je t'ai dis de ne pas avancé !")
            rep=input("calmez le -> ")
            print ("je ne veux rien savoir tu à choisi ton sort !")
            print ()
            print("vous mourez carbonizé par de la lave divine")
            exit(0)

        elif direction == "en arrière":
            print ("merci de m'avoir écouté")

    elif direction == "droite":

        print ("un long chemin continue à perte de vue")
        print()
        print("_| |____")
        print("     ¤ >")
        print("-- -----")
        print()
        direction = input("->")

        while direction != "droite" and direction != "gauche":

            if nombre_de_dents > 0:
                print("vous venez de vous cogner contre un mur et perdez une dents, bravo")
                nombre_de_dents = nombre_de_dents - 1
                direction = input("->")
            else:
                print("vous navez plus de dents et vous vous fracturez un os")
                direction = input("->")

        if direction == "droite":
            print("un long chemin continue à perte de vue")
            print()
            print("_| |__________________________")
            print("                           ¤ >")
            print("-- ---------------------------")
            print()
            direction = input("->")
            while direction != "droite" and direction != "gauche":

                if nombre_de_dents > 0:
                    print("vous venez de vous cogner contre un mur et perdez une dents, bravo")
                    nombre_de_dents = nombre_de_dents - 1
                    direction = input("->")
                else:
                    print("vous navez plus de dents et vous vous fracturez un os")
                    direction = input("->")

            if direction == "droite":
                print("un long chemin continue à perte de vue")
                print()
                print("_| |________________________________________________")
                print("                                                 ¤ >")
                print("-- -------------------------------------------------")
                print()
                direction = input("->")
                while direction != "droite" and direction != "gauche":

                    if nombre_de_dents > 0:
                        print("vous venez de vous cogner contre un mur et perdez une dents, bravo")
                        nombre_de_dents = nombre_de_dents - 1
                        direction = input("->")
                    else:
                        print("vous navez plus de dents et vous vous fracturez un os")
                        direction = input("->")

                if direction == "droite":
                    print("un long chemin continue à perte de vue")
                    print()
                    print("_| |_____________________________________________________________________________________________________")
                    print("                                                                                                      ¤ >")
                    print("-- ------------------------------------------------------------------------------------------------------")
                    print()
                    direction = input("->")

                    while direction != "droite" and direction != "gauche":

                        if nombre_de_dents > 0:
                            print("vous venez de vous cogner contre un mur et perdez une dents, bravo")
                            nombre_de_dents = nombre_de_dents - 1
                            direction = input("->")
                        else:
                            print("vous navez plus de dents et vous vous fracturez un os")
                            direction = input("->")

                    print("vous perdez connaissance")
                    exit(0)
                else :
                    print("vous perdez connaissance")
                    exit(0)
            else:
                print("vous perdez connaissance")
                exit(0)

        else :
            print("vous perdez connaissance")
            exit(0)



    else :
        print ("vous n'avez pas la capacité mentale nessessaire pour faire ce labyrinthe et vous mourez tandis que vous essayez de faire fonctionner votre cerveau")