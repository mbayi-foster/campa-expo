"""Configuration de l'application (par environnement)."""

import os


class Config:
    """Configuration de base, commune à tous les environnements."""

    APP_NAME = "CAMPAEXPO RDC"
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-a-changer")
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    """Configuration pour le développement local."""

    DEBUG = True


class ProductionConfig(Config):
    """Configuration pour la production."""

    DEBUG = False


class TestingConfig(Config):
    """Configuration utilisée par les tests."""

    TESTING = True


#: Dictionnaire de sélection : nom de l'environnement -> classe de configuration
CONFIGS = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}
