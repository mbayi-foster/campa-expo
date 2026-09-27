"""Contrôleur de la page « À propos ».

Rôle : récupérer l'identité de la plateforme et la composition du bureau
principal, puis les envoyer à la vue.
"""

from flask import current_app, render_template

from src.services.a_propos_service import AProposService


class AProposController:
    """Orchestre l'affichage de la page À propos."""

    @staticmethod
    def index():
        """Affiche la présentation de CAMPAEXPO RDC et son bureau principal."""
        context = AProposService.get_context()
        context["page_title"] = "À propos de CAMPAEXPO RDC"
        context["app_name"] = current_app.config.get("APP_NAME", "CAMPAEXPO RDC")
        return render_template("a_propos/index.html", **context)
