from flask import render_template


class UserController:
    """Contrôleur pour la gestion des utilisateurs dans l'administration."""

    @staticmethod
    def index():
        """Affiche la liste des utilisateurs."""
        # Logique pour récupérer les utilisateurs depuis la base de données
        users = []  # Remplacer par la récupération réelle des utilisateurs
        return render_template("admin/users.html", users=users)