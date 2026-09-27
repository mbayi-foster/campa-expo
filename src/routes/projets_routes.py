"""Blueprint de la page « Projets ».

Une route ne contient aucune logique métier : elle délègue au contrôleur.
"""

from flask import Blueprint

from src.controllers.projets_controller import ProjetsController

projets_bp = Blueprint("projets", __name__)


@projets_bp.route("/projets", methods=["GET"])
def index():
    """Catalogue des projets étudiants validés (filtrable via ?secteur=)."""
    return ProjetsController.index()
