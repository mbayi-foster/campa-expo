"""Blueprint de la page d'accueil.

Une route ne contient aucune logique métier : elle délègue au contrôleur.
"""

from flask import Blueprint

from src.controllers.home_controller import HomeController

home_bp = Blueprint("home", __name__)


@home_bp.route("/", methods=["GET"])
def index():
    """Page d'accueil du site."""
    return HomeController.index()
