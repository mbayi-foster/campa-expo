"""Blueprint de la page « Programmes ».

Une route ne contient aucune logique métier : elle délègue au contrôleur.
"""

from flask import Blueprint

from src.controllers.programmes_controller import ProgrammesController

programmes_bp = Blueprint("programmes", __name__)


@programmes_bp.route("/programmes", methods=["GET"])
def index():
    """Page des programmes et de l'agenda des événements."""
    return ProgrammesController.index()
