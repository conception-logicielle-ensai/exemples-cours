import requests
from typing import Any


class HttpSession:
    """
    Wrapper de session HTTP gérant automatiquement l'authentification
    et le rafraîchissement des jetons.
    """

    def __init__(self, base_url: str, access_token: str, refresh_token: str):
        self.base_url = base_url
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.session = requests.Session()

    def _auth_headers(self) -> dict:
        """
        Génère les headers d'authentification pour les requêtes sortantes.
        """
        return {
            "Authorization": f"Bearer {self.access_token}"
        }

    def refresh_access_token(self) -> None:
        """
        Rafraîchit l'access token à l'aide du refresh token.
        """
        response = self.session.post(
            f"{self.base_url}/auth/refresh",
            json={"refresh_token": self.refresh_token}
        )
        response.raise_for_status()

        data = response.json()
        self.access_token = data["access_token"]

    def get(self, path: str, **kwargs) -> Any:
        """
        Exécute une requête GET authentifiée avec gestion automatique
        de l'expiration du jeton.
        """
        response = self.session.get(
            f"{self.base_url}{path}",
            headers=self._auth_headers(),
            **kwargs
        )

        if response.status_code == 401:
            self.refresh_access_token()
            response = self.session.get(
                f"{self.base_url}{path}",
                headers=self._auth_headers(),
                **kwargs
            )

        response.raise_for_status()
        return response.json()