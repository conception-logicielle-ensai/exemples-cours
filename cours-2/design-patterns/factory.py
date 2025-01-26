from abc import abstractmethod
from typing import Literal


class Cloud:
    """Classe de base pour tous les types de nuages."""
    def __init__(self, size: str, altitude: str):
        self.size = size  # Taille du nuage (petit, moyen, grand)
        self.altitude = altitude  # Altitude du nuage (basse, moyenne, haute)
        self.color = self._default_color()  # Couleur par défaut selon le type de nuage
    @abstractmethod
    def _default_color(self) -> Literal["gris", "noir", "blanc"]:
        raise NotImplementedError("Chaque type de nuage doit définir sa couleur par défaut.")

    def _default_event(self) -> str:
        return  "reste calme et n'a aucun effet météorologique."
    def generate_weather(self) -> str:
        return f"Le nuage {self.size}, de couleur {self._default_color()}, situé à {self.altitude} altitude, {self._default_event()}."

    def __str__(self):
        return f"Cloud(size={self.size}, altitude={self.altitude}, color={self.color})"

class RainCloud(Cloud):
    """Nuage produisant de la pluie."""
    def _default_color(self) -> Literal["gris"]:
        return "gris"
    def _default_event(self) -> str:
        return "produit de la pluie"

class ThunderCloud(Cloud):
    """Nuage produisant des orages."""
    def _default_color(self) -> Literal["noir"]:
        return "noir"
    def _default_event(self) -> str:
        return " produit des éclairs et du tonnerre !"

class NeutralCloud(Cloud):
    """Nuage sans effet météorologique."""
    def _default_color(self) -> Literal["blanc"]:
        return "blanc"

class CloudFactory:
    """Factory pour créer des nuages en fonction du type et des paramètres."""
    @staticmethod
    def create_cloud(cloud_type: Literal["rain", "thunder", "neutral"], size: str, altitude: str) -> Cloud:
        if cloud_type == "rain":
            return RainCloud(size, altitude)
        elif cloud_type == "thunder":
            return ThunderCloud(size, altitude)
        elif cloud_type == "neutral":
            return NeutralCloud(size, altitude)
        else:
            raise ValueError(f"Type de nuage inconnu : {cloud_type}")

# Exemple d'utilisation
if __name__ == "__main__":
    # Créer un nuage de pluie
    rain_cloud = CloudFactory.create_cloud("rain", size="grand", altitude="moyenne")
    print(rain_cloud)
    print(rain_cloud.generate_weather())  
    # Le nuage grand, de couleur gris, situé à moyenne altitude, produit de la pluie.

    # Créer un nuage d'orage
    thunder_cloud = CloudFactory.create_cloud("thunder", size="immense", altitude="haute")
    print(thunder_cloud)
    print(thunder_cloud.generate_weather()) 
    # Le nuage immense, de couleur noir, situé à haute altitude,  produit des éclairs et du tonnerre !.

    # Créer un nuage neutre
    neutral_cloud = CloudFactory.create_cloud("neutral", size="petit", altitude="basse")
    print(neutral_cloud)
    print(neutral_cloud.generate_weather())  
 