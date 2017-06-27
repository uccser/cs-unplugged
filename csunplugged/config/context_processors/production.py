"""Context processor for checking if in production environment."""

import environ


def production(request):
    """Return a dictionary containing boolean if production environment.

    Returns:
        Dictionary containing production boolean to add to context.
    """
    env = environ.Env()
    return {"PRODUCTION": env.bool("DJANGO_SETTINGS_MODULE") == "config.settings.production"}
