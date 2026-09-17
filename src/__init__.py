"""Fabrique d'application Flask (Application Factory).

Ce module assemble l'application :
    - configuration  ->  src/shared/config.py
    - routes         ->  src/routes/
    - vues           ->  src/views/templates/
    - assets         ->  static/ (à la racine du projet)
"""

from pathlib import Path

from flask import Flask, render_template

from src.shared.config import DevelopmentConfig

#: Chemin absolu vers le dossier "static" situé à la racine du projet.
#: (les chemins relatifs seraient résolus depuis "src/", ce qui pointerait
#: vers un dossier inexistant)
STATIC_DIR = Path(__file__).resolve().parent.parent / "static"


def create_app(config_object: type = DevelopmentConfig) -> Flask:
    """Crée et configure l'instance Flask."""
    app = Flask(
        __name__,
        template_folder="views/templates",
        static_folder=str(STATIC_DIR),
        static_url_path="/static",
    )
    app.config.from_object(config_object)

    _register_blueprints(app)
    _register_error_handlers(app)

    return app


def _register_blueprints(app: Flask) -> None:
    """Enregistre tous les blueprints de l'application."""
    from src.routes.home_routes import home_bp

    app.register_blueprint(home_bp)


def _register_error_handlers(app: Flask) -> None:
    """Déclare les pages d'erreur personnalisées."""

    @app.errorhandler(404)
    def page_introuvable(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def erreur_serveur(error):
        return render_template("errors/500.html"), 500
