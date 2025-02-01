from jinja2 import Environment
def environment(**options):
    """
    Configuration Jinja2 pour prise en compte du jinja2 pour les fichiers html xml
    """
    env = Environment(
        **options
    )
    return env