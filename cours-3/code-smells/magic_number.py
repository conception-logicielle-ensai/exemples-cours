import numpy as np

def v1():
    def detecter_valeurs_extremes(valeurs):
        """
        Identifie les valeurs situées à plus de 3 écarts-types de la moyenne.
        """
        moyenne = np.mean(valeurs)
        ecart_type = np.std(valeurs)

        valeurs_extremes = []
        for valeur in valeurs:
            if abs(valeur - moyenne) > 3 * ecart_type:
                valeurs_extremes.append(valeur)

        return valeurs_extremes


    def calculer_moyenne_glissante(valeurs):
        """
        Calcule une moyenne glissante sur une fenêtre de taille 3.
        Les positions où le calcul est impossible retournent None.
        """
        if len(valeurs) < 3:
            return [None] * len(valeurs)

        moyennes_glissantes = [None]  # Bord gauche
        for index in range(1, len(valeurs) - 1):
            moyenne_locale = np.mean(valeurs[index - 1:index + 2])
            moyennes_glissantes.append(moyenne_locale)

        moyennes_glissantes.append(None)  # Bord droit
        return moyennes_glissantes


    # Données d'entrée
    valeurs_mesurees = [100, 100, 101, 99, 100, 101, 99, 100, 100, 100, 300]

    # Détection des valeurs extrêmes
    valeurs_extremes = detecter_valeurs_extremes(valeurs_mesurees)
    print(f"Valeurs extrêmes : {valeurs_extremes}")

    # Calcul de la moyenne glissante
    moyennes = calculer_moyenne_glissante(valeurs_mesurees)
    print(f"Moyenne glissante sur 3 : {moyennes}")


def v2():
    # Constantes de configuration
    TAILLE_FENETRE_MOYENNE = 3
    SEUIL_ECART_TYPE = 3


    def detecter_valeurs_extremes(valeurs):
        """
        Identifie les valeurs situées à plus de SEUIL_ECART_TYPE écarts-types
        de la moyenne.
        """
        moyenne = np.mean(valeurs)
        ecart_type = np.std(valeurs)

        valeurs_extremes = []
        for valeur in valeurs:
            if abs(valeur - moyenne) > SEUIL_ECART_TYPE * ecart_type:
                valeurs_extremes.append(valeur)

        return valeurs_extremes


    def calculer_moyenne_glissante(valeurs):
        """
        Calcule une moyenne glissante sur une fenêtre de taille
        TAILLE_FENETRE_MOYENNE.
        Les bords où le calcul est impossible retournent None.
        """
        if len(valeurs) < TAILLE_FENETRE_MOYENNE:
            return [None] * len(valeurs)

        moyennes_glissantes = [None]  # Bord gauche
        for index in range(1, len(valeurs) - 1):
            moyenne_locale = np.mean(
                valeurs[index - 1:index + TAILLE_FENETRE_MOYENNE - 1]
            )
            moyennes_glissantes.append(moyenne_locale)

        moyennes_glissantes.append(None)  # Bord droit
        return moyennes_glissantes


    # Données d'entrée
    valeurs_mesurees = [100, 100, 101, 99, 100, 101, 99, 100, 100, 100, 300]

    # Détection des valeurs extrêmes
    valeurs_extremes = detecter_valeurs_extremes(valeurs_mesurees)
    print(f"Valeurs extrêmes : {valeurs_extremes}")

    # Calcul de la moyenne glissante
    moyennes = calculer_moyenne_glissante(valeurs_mesurees)
    print(f"Moyenne glissante sur {TAILLE_FENETRE_MOYENNE} : {moyennes}")



print("=== Avant amélioration ===")
v1()
print("=== Après amélioration ===")
v2()