import numpy as np

def v1():
    def extreme(data):
        # Calcul de la moyenne et de l'écart-type
        mean = np.mean(data)
        std_dev = np.std(data)
        resultat = []  # Liste pour stocker les valeurs extrêmes
        for x in data:
            if abs(x - mean) > 3 * std_dev: 
                resultat.append(x)  # Utilisation de append pour ajouter des éléments
        return resultat  # Retourne la liste des valeurs extrêmes

    # Calcul de la moyenne glissante sur une fenêtre de taille 3
    def moyenne_glissante(data):
        """
        Calcule une moyenne glissante sur une fenêtre de taille 3.
        Les bords où il n'y a pas assez de valeurs retournent None.
        """
        if len(data) < 3:
            return [None] * len(data)

        resultats = [None]  # Padding initial pour le bord gauche
        for i in range(1, len(data) - 1):
            moyenne = np.mean(data[i - 1:i + 2])  # Calcul de la moyenne glissante
            resultats.append(moyenne)
        resultats.append(None)  # Padding final pour le bord droit
        return resultats

    # Données
    data = [100, 102, 98, 97, 250, 101, 99, 102]
    # Identification des valeurs extrêmes (plus de 3 écarts-types de la moyenne)
    extremes = extreme(data)
    print(f"Valeurs extrêmes : {extremes}")
    # Calcul et affichage de la moyenne glissante
    glissement = moyenne_glissante(data)
    print(f"Moyenne glissante sur 3 : {glissement}")

def v2():
    import numpy as np

    # Définition des constantes
    TAILLE_FENETRE_GLISSANTE = 3
    MULTIPLICATEUR_SEUIL = 3

    def extreme(data):
        # Calcul de la moyenne et de l'écart-type
        mean = np.mean(data)
        std_dev = np.std(data)
        resultat = []  # Liste pour stocker les valeurs extrêmes
        for x in data:
            if abs(x - mean) > MULTIPLICATEUR_SEUIL * std_dev:  # Utilisation de la constante
                resultat.append(x)
        return resultat  # Retourne la liste des valeurs extrêmes

    # Calcul de la moyenne glissante sur une fenêtre de taille définie
    def moyenne_glissante(data):
        """
        Calcule une moyenne glissante sur une fenêtre de taille définie.
        Les bords où il n'y a pas assez de valeurs retournent None.
        """
        if len(data) < TAILLE_FENETRE_GLISSANTE:
            return [None] * len(data)

        resultats = [None]  # Padding initial pour le bord gauche
        for i in range(1, len(data) - 1):
            moyenne = np.mean(data[i - 1:i + TAILLE_FENETRE_GLISSANTE - 1])  # Utilisation de la constante
            resultats.append(moyenne)
        resultats.append(None)  # Padding final pour le bord droit
        return resultats

    # Données
    data = [100, 102, 98, 97, 250, 101, 99, 102]
    # Identification des valeurs extrêmes (plus de 3 écarts-types de la moyenne)
    extremes = extreme(data)
    print(f"Valeurs extrêmes : {extremes}")
    # Calcul et affichage de la moyenne glissante
    glissement = moyenne_glissante(data)
    print(f"Moyenne glissante sur 3 : {glissement}")
print("=== Avant amélioration ===")
v1()
print("=== Après amélioration ===")
v2()