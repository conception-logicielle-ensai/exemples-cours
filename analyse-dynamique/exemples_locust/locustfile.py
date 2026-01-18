from locust import HttpUser, task, between, events
import random
import logging

# Configuration du logging pour des rapports plus détaillés
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class APIUser(HttpUser):
    """Simule un utilisateur réaliste de l'API avec scénarios variés"""

    # Temps d'attente entre les tâches (simulation réaliste)
    wait_time = between(0.5, 2)

    def on_start(self):
        """Initialisation de chaque utilisateur"""
        logger.info("🚀 Nouvel utilisateur connecté")
        # Vérifie la santé de l'API
        response = self.client.get("/health")
        if response.status_code == 200:
            logger.info("✅ API disponible")

    @task(5)
    def browse_items(self):
        """Navigation dans les items (scénario le plus fréquent)"""
        self.client.get("/items", name="/items - Browse all")


# Événements pour des rapports personnalisés
@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    logger.info("=" * 60)
    logger.info("🎯 DÉMARRAGE DES TESTS DE CHARGE")
    logger.info("=" * 60)
    logger.info(f"Host: {environment.host}")
    logger.info(
        f"Utilisateurs: {environment.runner.target_user_count if hasattr(environment.runner, 'target_user_count') else 'N/A'}"
    )
    logger.info("=" * 60)


@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    logger.info("=" * 60)
    logger.info("🏁 FIN DES TESTS DE CHARGE")
    logger.info("=" * 60)
    stats = environment.stats
    logger.info(f"Total de requêtes: {stats.total.num_requests}")
    logger.info(f"Échecs: {stats.total.num_failures}")
    logger.info(f"RPS moyen: {stats.total.total_rps:.2f}")
    logger.info(f"Temps de réponse médian: {stats.total.median_response_time}ms")
    logger.info(
        f"Temps de réponse 95%: {stats.total.get_response_time_percentile(0.95)}ms"
    )
    logger.info("=" * 60)
