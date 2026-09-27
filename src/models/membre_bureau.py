"""Modèle représentant un membre du bureau principal de CAMPAEXPO."""

from dataclasses import dataclass


@dataclass(frozen=True)
class MembreBureau:
    """Un membre du bureau exécutif, d'une direction ou du secrétariat."""

    nom: str
    fonction: str
    entite: str
    parcours: str
    bio: str
    email: str
    tonalite: str = "bleu"

    @property
    def initiales(self) -> str:
        """Initiales affichées dans la pastille d'avatar."""
        morceaux = [partie for partie in self.nom.replace("Me ", "").split() if partie]
        return "".join(partie[0] for partie in morceaux[:2]).upper()

    @property
    def est_bureau_executif(self) -> bool:
        """Vrai si le membre siège au bureau exécutif national."""
        return "Exécutif" in self.entite

    @property
    def est_direction(self) -> bool:
        """Vrai si le membre dirige une direction thématique."""
        return self.entite.startswith("Direction") or self.entite.startswith("Coordination")
