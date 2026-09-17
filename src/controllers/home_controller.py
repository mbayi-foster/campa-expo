"""Contrôleur de la page d'accueil.

Rôle : récupérer les données via le service, puis les envoyer à la vue.
"""

from flask import current_app, render_template, request

from src.services.home_service import HomeService


class HomeController:
    """Orchestre l'affichage de la page d'accueil."""

    @staticmethod
    def index():
        """Affiche la page d'accueil."""
        context = HomeService.get_home_context()
        context["page_title"] = current_app.config.get("APP_NAME", "Accueil")
        context["nom_visiteur"] = request.args.get("nom", "visiteur")
        return render_template("home/index.html", **context)
