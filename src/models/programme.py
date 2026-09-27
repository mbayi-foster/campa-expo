"""Modèle représentant un programme d'accompagnement CAMPAEXPO."""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Programme:
    """Un programme proposé aux étudiants et jeunes diplômés de la RDC."""

    slug: str
    nom: str
    accroche: str
    description: str
    icone: str
    duree: str
    format: str
    public: str
    prochaine_session: str
    places: str
    avantages: tuple[str, ...] = field(default_factory=tuple)
    etapes: tuple[str, ...] = field(default_factory=tuple)
    tonalite: str = "bleu"

    @property
    def ancre(self) -> str:
        """Ancre HTML du bloc programme (ex. "#incubation-universitaire")."""
        return f"#{self.slug}"
