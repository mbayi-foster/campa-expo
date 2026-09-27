"""Blueprint de la page « Contact ».

Une route ne contient aucune logique métier : elle délègue au contrôleur.
"""

from flask import Blueprint

from src.controllers.contact_controller import ContactController

contact_bp = Blueprint("contact", __name__)


@contact_bp.route("/contact", methods=["GET", "POST"])
def index():
    """Page de contact : coordonnées, réseaux sociaux et formulaire."""
    return ContactController.index()


@contact_bp.route("/contact/newsletter", methods=["POST"])
def newsletter():
    """Inscription à la lettre d'information (formulaire du pied de page inclus)."""
    return ContactController.newsletter()
