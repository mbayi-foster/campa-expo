"""Blueprint de la page « À propos ».

Une route ne contient aucune logique métier : elle délègue au contrôleur.
"""

from flask import Blueprint

from src.controllers.a_propos_controller import AProposController

a_propos_bp = Blueprint("a_propos", __name__)


@a_propos_bp.route("/a-propos", methods=["GET"])
def index():
    """Présentation de CAMPAEXPO RDC et de son bureau principal."""
    return AProposController.index()
