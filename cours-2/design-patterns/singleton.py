import logging
from typing import Optional, Literal

class Singleton(type):
    """ A metaclass that creates a Singleton base class when called. """
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=Singleton):
    _logger = None  # Variable pour stocker le logger singleton

    def setup(self, log_level: Literal['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
              log_file: Optional[str] = None):
        """
        Configure le logger au démarrage avec le niveau de log et le fichier de log. 
        Pour info le niveau de log, c'est le niveau minimal de log que le logger accepte d'output
        """
        if Logger._logger is not None:
            raise RuntimeError("Logger déjà configuré!")

        Logger._logger = logging.getLogger(__name__)
        Logger._logger.setLevel(log_level)

        # Créer un formatteur
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # Si un fichier est spécifié, alors on utilise un FileHandler
        if log_file:
            file_handler = logging.FileHandler(log_file, encoding='utf-8')
            file_handler.setFormatter(formatter)
            Logger._logger.addHandler(file_handler)
    @staticmethod
    def get_logger():
        if Logger._logger is None:
            raise RuntimeError("Logger non configuré, appelez setup() d'abord.")
        return Logger._logger

    def log_info(self, message: str):
        Logger._logger.info(message)

    def log_debug(self, message: str):
        Logger._logger.debug(message)

    def log_warning(self, message: str):
        Logger._logger.warning(message)

    def log_error(self, message: str):
        Logger._logger.error(message)

    def log_critical(self, message: str):
        Logger._logger.critical(message)

# Exemple d'utilisation
if __name__ == "__main__":
    # Configuration du logger au démarrage avec un fichier de log et niveau INFO
    logger_initializer = Logger()
    logger_initializer.setup(log_level='INFO', log_file='output.log')
    # Obtenir l'instance initialisée ailleurs
    logger1: logging.Logger = Logger.get_logger()
    logger1.info("L'application précise l'invocation d'une fonction normale mais utile pour la compréhension de son execution <=> print")
    logger1.debug("L'application fait des opérations bas niveau qu'on ne doit regarder qu'en cas de débuggage")

    # Dans une autre classe on peut importer le logger avec le get_logger statique 
    logger2: logging.Logger = Logger.get_logger()
    logger2.warning("L'application précise un comportement anormal ou un problème non bloquant")
    logger2.error("L'application précise un comportement critique qui précise un dysfonctionnement bloquant")


