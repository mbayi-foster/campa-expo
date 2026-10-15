"""Blueprint des pages « administration ».

Une route ne contient aucune logique métier : elle délègue au contrôleur.
"""

from flask import Blueprint

from src.controllers.admin.user_controller import UserController

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/admin", methods=["GET"])
def index():
    return UserController.index()

@admin_bp.route("/admin/users", methods=["GET"])
def users():
    return UserController.index()