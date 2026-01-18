from src.service.compteur_service import CompteurService


class CompteurView:
    """
    CompteurView gère uniquement l'affichage, il délègue tout le run au service
    """
    def __init__(self, base_dir="./", comptage_fichier_service:CompteurService = CompteurService()):
        self.__base_dir = base_dir
        self.__comptage_fichier_service = comptage_fichier_service

    def compter_metadonnees_caracteres_fichier(self, chemin_fichier_str: str):
        comptages = self.__comptage_fichier_service.recuperer_informations_caracteres_fichier(
            base_dir=self.__base_dir, chemin_fichier_str=chemin_fichier_str
        )
        print(comptages)
