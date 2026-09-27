"""Contrôleur de la page « Programmes ».

Rôle : récupérer les données via le service, puis les envoyer à la vue.
"""

from flask import current_app, render_template

from src.services.programmes_service import ProgrammesService


class ProgrammesController:
    """Orchestre l'affichage de la page Programmes."""

    @staticmethod
    def index():
        """Affiche les programmes et l'agenda des événements à venir."""
        context = ProgrammesService.get_context()
        context["page_title"] = "Programmes & Événements"
        context["app_name"] = current_app.config.get("APP_NAME", "CAMPAEXPO RDC")
        return render_template("programmes/index.html", **context)
