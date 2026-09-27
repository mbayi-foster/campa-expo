"""Contrôleur de la page « Projets ».

Rôle : récupérer le catalogue des projets validés (éventuellement filtré
par le paramètre d'URL `secteur`) et l'envoyer à la vue.
"""

from flask import current_app, render_template, request

from src.services.projets_service import ProjetsService


class ProjetsController:
    """Orchestre l'affichage de la page Projets."""

    @staticmethod
    def index():
        """Affiche les projets étudiants validés."""
        secteur = request.args.get("secteur")
        context = ProjetsService.get_context(secteur=secteur)
        context["page_title"] = "Projets étudiants validés"
        context["app_name"] = current_app.config.get("APP_NAME", "CAMPAEXPO RDC")
        return render_template("projets/index.html", **context)
