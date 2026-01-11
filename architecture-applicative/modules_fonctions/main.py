def battre_oeufs():
    """Simule le fait de battre les œufs."""
    print("Battre les œufs jusqu'à ce qu'ils soient bien mousseux.")

def faire_fondre_beurre():
    """Simule le fait de faire fondre le beurre."""
    print("Faire fondre le beurre dans une casserole.")

def faire_fondre_chocolat():
    """Simule le fait de faire fondre le chocolat."""
    print("Faire fondre le chocolat au bain-marie.")

def preparer_mousse_au_chocolat():
    """Prépare la mousse au chocolat en appelant les autres fonctions dans l'ordre."""
    print("Préparation de la mousse au chocolat :")
    battre_oeufs()
    faire_fondre_beurre()
    faire_fondre_chocolat()
    print("Mélanger tous les ingrédients pour former une mousse délicieuse!")

# Appel de la fonction principale pour préparer la mousse au chocolat
preparer_mousse_au_chocolat()