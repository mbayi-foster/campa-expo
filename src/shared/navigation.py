"""Définition de la navigation principale de l'application.

Les entrées de menu sont centralisées ici : pour ajouter une page dans
l'en-tête (version bureau **et** version mobile), il suffit d'ajouter une
entrée dans ``NAVIGATION_PRINCIPALE``.

Le lien correspondant à la page affichée est marqué automatiquement comme
actif (attribut ``aria-current="page"``, pastille de couleur, etc.) grâce au
processeur de contexte enregistré dans ``src/__init__.py``.
"""

from dataclasses import dataclass, replace

from flask import Request


@dataclass(frozen=True)
class LienNavigation:
    """Une entrée du menu principal de l'en-tête."""

    libelle: str
    endpoint: str
    identifiant: str
    icone: str = "chevron_right"
    #: Renseigné par le processeur de contexte selon la page demandée.
    actif: bool = False


#: Ordre d'affichage des liens dans l'en-tête et le menu mobile.
NAVIGATION_PRINCIPALE: tuple[LienNavigation, ...] = (
    LienNavigation(
        libelle="Accueil",
        endpoint="home.index",
        identifiant="accueil",
        icone="home",
    ),
    LienNavigation(
        libelle="Programmes",
        endpoint="programmes.index",
        identifiant="programmes",
        icone="grid_view",
    ),
    LienNavigation(
        libelle="Projets",
        endpoint="projets.index",
        identifiant="projets-etudiants",
        icone="folder_special",
    ),
    LienNavigation(
        libelle="Contact",
        endpoint="contact.index",
        identifiant="contact",
        icone="mail",
    ),
    LienNavigation(
        libelle="À propos",
        endpoint="a_propos.index",
        identifiant="a-propos",
        icone="account_balance",
    ),
)


def _est_page_courante(lien: LienNavigation, requete: Request) -> bool:
    """Indique si le lien correspond à la page en cours de rendu.

    L'endpoint exact est comparé en priorité, puis le blueprint : ainsi une
    future sous-page (ex. ``programmes.detail``) gardera l'entrée principale
    « Programmes » active.
    """
    if lien.endpoint == requete.endpoint:
        return True

    blueprint_courant = requete.blueprint or ""
    return bool(blueprint_courant) and lien.endpoint.split(".")[0] == blueprint_courant


def liens_avec_etat(requete: Request) -> list[LienNavigation]:
    """Retourne les liens de navigation enrichis de leur état « actif »."""
    return [
        replace(lien, actif=_est_page_courante(lien, requete))
        for lien in NAVIGATION_PRINCIPALE
    ]
