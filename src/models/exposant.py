"""Modèle représentant un exposant du salon."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Exposant:
    """Un exposant présent sur le salon."""

    nom: str
    secteur: str
    stand: str
