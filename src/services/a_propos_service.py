"""Service de la page « À propos ».

Rôle : présenter l'identité de CAMPAEXPO RDC (mission, vision, valeurs,
histoire, gouvernance) ainsi que le bureau principal et ses directions.
"""

from src.models import MembreBureau


class AProposService:
    """Fournit les données de la page À propos."""

    @staticmethod
    def _get_identite() -> dict:
        """Mission, vision et positionnement de la plateforme."""
        return {
            "mission": (
                "Réveiller, structurer et financer le potentiel entrepreneurial des "
                "étudiants de la République Démocratique du Congo, en transformant les "
                "travaux académiques en entreprises viables et créatrices d'emplois."
            ),
            "vision": (
                "Faire de la RDC le premier vivier africain d'entreprises innovantes "
                "portées par des diplômés, avec 500 sociétés estudiantines créées et "
                "5 000 emplois durables à l'horizon 2035."
            ),
            "baseline": "La vitrine de l'entrepreneuriat étudiant",
            "statut": (
                "Programme national d'appui à l'entrepreneuriat estudiantin, conduit en "
                "partenariat avec les établissements d'enseignement supérieur et les "
                "acteurs privés de la RDC."
            ),
        }

    @staticmethod
    def _get_valeurs() -> list[dict]:
        """Les valeurs qui encadrent chaque décision du programme."""
        return [
            {
                "nom": "Excellence académique",
                "description": (
                    "Aucun projet n'entre en incubation sans validation scientifique : "
                    "l'université reste le socle de la crédibilité technique."
                ),
                "icone": "school",
                "tonalite": "bleu",
            },
            {
                "nom": "Transmission",
                "description": (
                    "Chaque lauréat devient à son tour mentor : le savoir acquis est "
                    "redistribué à la génération suivante, campus par campus."
                ),
                "icone": "volunteer_activism",
                "tonalite": "profond",
            },
            {
                "nom": "Panafricanisme",
                "description": (
                    "Nous construisons des ponts entre la RDC, la diaspora et les "
                    "écosystèmes d'Afrique centrale, de l'Ouest et d'Europe."
                ),
                "icone": "public",
                "tonalite": "or",
            },
            {
                "nom": "Éthique & transparence",
                "description": (
                    "Charte signée par tous les mentors, audit externe des bourses et "
                    "publication des rapports annuels d'impact."
                ),
                "icone": "verified_user",
                "tonalite": "info",
            },
            {
                "nom": "Inclusion nationale",
                "description": (
                    "26 provinces représentées, parité femmes-hommes dans les cohortes et "
                    "accessibilité numérique pour les campus à faible connectivité."
                ),
                "icone": "diversity_3",
                "tonalite": "bleu",
            },
            {
                "nom": "Impact mesuré",
                "description": (
                    "Chaque projet financé est suivi sur trois indicateurs : emplois "
                    "créés, revenus générés et bénéficiaires servis."
                ),
                "icone": "monitoring",
                "tonalite": "profond",
            },
        ]

    @staticmethod
    def _get_histoire() -> list[dict]:
        """Les grandes étapes de la plateforme."""
        return [
            {
                "annee": "2019",
                "titre": "Naissance du concept",
                "description": (
                    "Un collectif d'étudiants et d'enseignants de l'UNIKIN imagine une "
                    "plateforme qui relie les projets de fin d'études au marché réel."
                ),
            },
            {
                "annee": "2021",
                "titre": "Première Foire Campus",
                "description": (
                    "12 universités, 40 projets exposés et les premiers mentors bénévoles "
                    "réunis à Kinshasa."
                ),
            },
            {
                "annee": "2022",
                "titre": "Création des comités CDU",
                "description": (
                    "Installation des Comités de Développement Universitaires pour ancrer "
                    "le programme dans la vie quotidienne des campus."
                ),
            },
            {
                "annee": "2023",
                "titre": "Premier Hackathon national",
                "description": (
                    "48 heures de prototypage simultané à Lubumbashi, Goma et Kinshasa, "
                    "avec 180 étudiants inscrits."
                ),
            },
            {
                "annee": "2024",
                "titre": "Lancement du fonds d'amorçage",
                "description": (
                    "Les premières bourses non dilutives sont décaissées : 18 projets "
                    "financés et 9 sociétés créées."
                ),
            },
            {
                "annee": "2025",
                "titre": "Reconnaissance institutionnelle",
                "description": (
                    "Signature des conventions avec le Ministère de l'ESU et 28 "
                    "universités partenaires ; intégration aux parcours académiques."
                ),
            },
            {
                "annee": "2026",
                "titre": "Passage à l'échelle nationale",
                "description": (
                    "Cohorte 7, couverture des 26 provinces, Grand Prix d'Innovation porté "
                    "à 50 000 USD et retransmission panafricaine de la Foire."
                ),
            },
        ]

    @staticmethod
    def _get_chiffres() -> list[dict]:
        """Indicateurs clés de la plateforme."""
        return [
            {
                "valeur": "1 500",
                "libelle": "Étudiants formés",
                "detail": "Bootcamps et masterclasses certifiantes",
                "icone": "school",
                "tonalite": "bleu",
            },
            {
                "valeur": "340",
                "libelle": "Projets accompagnés",
                "detail": "De l'idée au prototype testé",
                "icone": "rocket",
                "tonalite": "or",
            },
            {
                "valeur": "62",
                "libelle": "Projets financés",
                "detail": "Bourses d'amorçage décaissées",
                "icone": "payments",
                "tonalite": "profond",
            },
            {
                "valeur": "85",
                "libelle": "Mentors engagés",
                "detail": "Dirigeants et experts certifiés",
                "icone": "diversity_3",
                "tonalite": "info",
            },
            {
                "valeur": "28",
                "libelle": "Universités partenaires",
                "detail": "Conventions académiques signées",
                "icone": "apartment",
                "tonalite": "bleu",
            },
        ]

    @staticmethod
    def _get_bureau() -> list[MembreBureau]:
        """Les membres du bureau principal (siège national de Kinshasa)."""
        return [
            MembreBureau(
                nom="Prof. Émile Nkombo",
                fonction="Président du Bureau Exécutif National",
                entite="Bureau Exécutif National",
                parcours="Professeur d'économie industrielle · UNIKIN",
                bio=(
                    "Initiateur du projet CAMPAEXPO en 2019, il pilote la stratégie "
                    "nationale et représente la plateforme auprès des institutions."
                ),
                email="president@campaexpo-rdc.cd",
                tonalite="bleu",
            ),
            MembreBureau(
                nom="Me Chantal Ilunga",
                fonction="Vice-Présidente",
                entite="Bureau Exécutif National",
                parcours="Avocate d'affaires · propriété intellectuelle & OHADA",
                bio=(
                    "Elle sécurise juridiquement les projets, encadre les dépôts de "
                    "brevets et veille à la conformité des conventions de financement."
                ),
                email="vice-presidente@campaexpo-rdc.cd",
                tonalite="or",
            ),
            MembreBureau(
                nom="Ing. Patrick Mulumba",
                fonction="Secrétaire Général",
                entite="Bureau Exécutif National",
                parcours="Ingénieur en génie électrique · UPL",
                bio=(
                    "Coordinateur des antennes CDU, il assure la logistique des tournées "
                    "provinciales et le suivi administratif des cohortes."
                ),
                email="secretaire@campaexpo-rdc.cd",
                tonalite="profond",
            ),
            MembreBureau(
                nom="Mme Bénédicte Kasongo",
                fonction="Trésorière & Contrôle de gestion",
                entite="Bureau Exécutif National",
                parcours="Expert-comptable · audit et reporting",
                bio=(
                    "Elle encadre le décaissement des bourses d'amorçage et publie les "
                    "rapports financiers annuels soumis au comité d'audit."
                ),
                email="tresorerie@campaexpo-rdc.cd",
                tonalite="info",
            ),
            MembreBureau(
                nom="Dr Joseph Mweze",
                fonction="Directeur Scientifique & Président du Jury",
                entite="Direction Scientifique & Jury",
                parcours="Docteur en biotechnologies · UNIGOM",
                bio=(
                    "Il préside le comité d'évaluation qui valide la robustesse "
                    "scientifique et la faisabilité technique de chaque projet."
                ),
                email="scientifique@campaexpo-rdc.cd",
                tonalite="bleu",
            ),
            MembreBureau(
                nom="M. Yannick Tshibangu",
                fonction="Directeur des Programmes & Incubation",
                entite="Direction des Programmes",
                parcours="Lauréat CAMPAEXPO 2021 · entrepreneur",
                bio=(
                    "Ancien lauréat devenu encadrant, il pilote les cohortes "
                    "d'incubation, les bootcamps et le matching avec les mentors."
                ),
                email="programmes@campaexpo-rdc.cd",
                tonalite="or",
            ),
            MembreBureau(
                nom="Mme Sarah Ndaya",
                fonction="Directrice des Partenariats & Financement",
                entite="Direction des Partenariats",
                parcours="Banque d'investissement · fonds panafricains",
                bio=(
                    "Elle mobilise les sponsors, les fonds de garantie et les "
                    "investisseurs providentiels présents lors de la Grande Exposition."
                ),
                email="partenariats@campaexpo-rdc.cd",
                tonalite="profond",
            ),
            MembreBureau(
                nom="M. Gédéon Bokungu",
                fonction="Directeur Communication & Médias",
                entite="Direction Communication",
                parcours="Journaliste économique · presse nationale",
                bio=(
                    "Il coordonne la couverture médiatique, les réseaux sociaux "
                    "officiels et la retransmission de la Nuit des Lauréats."
                ),
                email="presse@campaexpo-rdc.cd",
                tonalite="info",
            ),
        ]

    @staticmethod
    def _get_secretariat() -> dict:
        """Le secrétariat permanent installé au siège national."""
        return {
            "services": [
                "Accueil et orientation des candidats",
                "Réception des dossiers physiques et légalisations",
                "Logistique de la Grande Exposition annuelle",
                "Accréditations presse et protocole institutionnel",
                "Archives des conventions et des brevets déposés",
            ],
            "adresse": "Boulevard du 30 Juin, Immeuble Sozacom, 4ᵉ niveau — Gombe, Kinshasa",
            "horaires": "Lundi → Vendredi : 08h30 — 17h00 · Samedi sur rendez-vous",
            "email": "secretariat@campaexpo-rdc.cd",
            "telephone": "+243 820 000 120",
        }

    @staticmethod
    def _get_gouvernance() -> list[dict]:
        """Les garanties de gouvernance et de transparence."""
        return [
            {
                "titre": "Charte d'éthique signée",
                "description": (
                    "Chaque mentor, membre de jury et encadrant signe une charte de "
                    "confidentialité et de non-captation des projets étudiants."
                ),
                "icone": "handshake",
                "tonalite": "bleu",
            },
            {
                "titre": "Audit externe annuel",
                "description": (
                    "Les comptes et l'usage des bourses d'amorçage sont audités par un "
                    "cabinet indépendant, puis publiés dans le rapport annuel."
                ),
                "icone": "fact_check",
                "tonalite": "profond",
            },
            {
                "titre": "Jury souverain",
                "description": (
                    "Les membres du jury déclarent leurs liens d'intérêts et ne peuvent "
                    "évaluer un projet dont ils sont parties prenantes."
                ),
                "icone": "gavel",
                "tonalite": "or",
            },
            {
                "titre": "Données protégées",
                "description": (
                    "Les informations transmises par les étudiants restent strictement "
                    "internes et ne sont jamais cédées à des tiers."
                ),
                "icone": "shield_lock",
                "tonalite": "info",
            },
        ]

    @staticmethod
    def _get_partenaires() -> list[str]:
        """Partenaires institutionnels et corporate affichés sur la page."""
        return [
            "Ministère ESU RDC",
            "UNIKIN Kinshasa",
            "UNILU Lubumbashi",
            "UNIGOM Goma",
            "UCB Bukavu",
            "Vodacom DRC Foundation",
            "Fonds Panafricain Seed",
            "Chambre de Commerce RDC",
        ]

    @classmethod
    def get_context(cls) -> dict:
        """Construit le contexte complet à transmettre à la vue."""
        bureau = cls._get_bureau()
        return {
            "identite": cls._get_identite(),
            "valeurs": cls._get_valeurs(),
            "histoire": cls._get_histoire(),
            "chiffres": cls._get_chiffres(),
            "bureau_executif": [membre for membre in bureau if membre.est_bureau_executif],
            "directions": [membre for membre in bureau if membre.est_direction],
            "secretariat": cls._get_secretariat(),
            "gouvernance": cls._get_gouvernance(),
            "partenaires": cls._get_partenaires(),
            "tags_hero": [
                "Depuis 2019",
                "28 universités",
                "26 provinces",
            ],
        }
