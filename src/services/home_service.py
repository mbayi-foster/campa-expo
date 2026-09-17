"""Service de la page d'accueil.

Rôle : préparer toutes les données affichées par la vue.
Ici les données sont statiques ; il suffira de brancher une base de données
ou un appel API à cet endroit sans toucher aux routes ni aux vues.
"""

from src.models import Exposant


class HomeService:
    """Fournit les données de la page d'accueil."""

    @staticmethod
    def _get_exposants() -> list[Exposant]:
        """Retourne les exposants mis en avant."""
        return [
            Exposant(nom="Atelier Ravel", secteur="Artisanat", stand="A12"),
            Exposant(nom="Studio Lambahoany", secteur="Design", stand="B04"),
            Exposant(nom="Saveurs de l'Est", secteur="Agroalimentaire", stand="C21"),
        ]

    @staticmethod
    def _get_statistiques() -> list[dict]:
        """Retourne les chiffres clés affichés sur la page."""
        return [
            {"valeur": "120", "libelle": "Exposants"},
            {"valeur": "3", "libelle": "Jours de salon"},
            {"valeur": "15 000", "libelle": "Visiteurs attendus"},
        ]

    @classmethod
    def get_home_context(cls) -> dict:
        """Construit le contexte complet à transmettre à la vue."""
        return {
            "hero": {
                "titre": "Bienvenue sur Campa Expo",
                "sous_titre": (
                    "Le rendez-vous des créateurs, artisans et entreprises "
                    "qui font bouger la région."
                ),
                "date": "Du 12 au 14 juin 2026",
                "lieu": "Parc des Expositions",
            },
            "statistiques": cls._get_statistiques(),
            "exposants": cls._get_exposants(),
        }
