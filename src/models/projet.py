"""Modèle représentant un projet étudiant validé par CAMPAEXPO."""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Projet:
    """Un projet étudiant validé par le comité scientifique."""

    nom: str
    secteur: str
    province: str
    universite: str
    porteur: str
    description: str
    phase: str
    statut: str
    date_validation: str
    financement: str
    icone: str
    impact: tuple[str, ...] = field(default_factory=tuple)
    tonalite: str = "bleu"
