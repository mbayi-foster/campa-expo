"""Modèle représentant un événement de l'agenda CAMPAEXPO."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Evenement:
    """Un rendez-vous inscrit au calendrier national."""

    jour: str
    mois: str
    annee: str
    titre: str
    ville: str
    lieu: str
    format: str
    heure: str
    description: str
    places: str
    action: str
    tonalite: str = "bleu"

    @property
    def date_courte(self) -> str:
        """Date compacte affichée dans le bloc calendrier."""
        return f"{self.jour} {self.mois} {self.annee}"
