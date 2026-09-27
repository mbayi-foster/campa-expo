"""Service de la page « Projets ».

Rôle : fournir le catalogue des projets étudiants validés et gérer le
filtrage par secteur demandé dans l'URL (ex. /projets?secteur=AgriTech).
"""

from src.models import Projet


class ProjetsService:
    """Fournit les données de la page Projets."""

    #: Libellé du filtre « tous les secteurs ».
    TOUS_LES_SECTEURS = "Tous"

    @staticmethod
    def _get_projets() -> list[Projet]:
        """Le catalogue des projets étudiants validés par le comité scientifique."""
        return [
            Projet(
                nom="AgroTech Kivu",
                secteur="AgriTech & Climat",
                province="Nord-Kivu",
                universite="Université de Goma (UNIGOM)",
                porteur="Fiston Bahati",
                description=(
                    "Boîtier IoT solaire à capteurs d'humidité et d'azote, relié à une "
                    "application mobile SMS pour guider l'irrigation des coopératives de "
                    "café et maraîchères autour du lac Kivu."
                ),
                phase="Déploiement terrain",
                statut="Validé — Cohorte 5",
                date_validation="12 mars 2026",
                financement="Bourse d'amorçage 4 500 USD",
                icone="agriculture",
                impact=("80 maraîchers connectés", "+40 % de rendement", "9 emplois créés"),
                tonalite="bleu",
            ),
            Projet(
                nom="KinPay Student",
                secteur="FinTech & Éducation",
                province="Kinshasa",
                universite="Université de Kinshasa (UNIKIN)",
                porteur="Grace Ilunga",
                description=(
                    "Micro-épargne collective et distribution sécurisée des bourses et "
                    "micro-crédits d'urgence pour frais académiques via le Mobile Money "
                    "congolais."
                ),
                phase="Pilote — 2 400 utilisateurs",
                statut="Validé — Cohorte 6",
                date_validation="28 avril 2026",
                financement="Micro-subvention 3 000 USD",
                icone="account_balance_wallet",
                impact=("2 400 étudiants inscrits", "1 200 bourses distribuées", "0 frais de dossier"),
                tonalite="or",
            ),
            Projet(
                nom="CongoClean Energy",
                secteur="Énergie Propre",
                province="Haut-Katanga",
                universite="Université Protestante de Lubumbashi (UPL)",
                porteur="Moïse Kalala",
                description=(
                    "Production de briquettes de combustion écologiques à partir de "
                    "résidus de maïs et de manioc : une alternative neutre en carbone au "
                    "charbon de bois (makala)."
                ),
                phase="Commercialisation locale",
                statut="Validé — Cohorte 4",
                date_validation="19 novembre 2025",
                financement="Bourse d'amorçage 5 000 USD",
                icone="local_fire_department",
                impact=("12 tonnes de briquettes par mois", "−3 200 sacs de makala", "18 emplois"),
                tonalite="profond",
            ),
            Projet(
                nom="MedStock Mobile",
                secteur="Santé & Biomédical",
                province="Sud-Kivu",
                universite="Université Catholique de Bukavu (UCB)",
                porteur="Grace Kahindo",
                description=(
                    "Gestion numérique des stocks de pharmacie hospitalière, avec alertes "
                    "de rupture et traçabilité des lots, déployée dans les structures de "
                    "santé universitaires du Sud-Kivu."
                ),
                phase="Déploiement — 6 cliniques",
                statut="Validé — Cohorte 4",
                date_validation="05 octobre 2025",
                financement="Prix National Santé 2024",
                icone="medication",
                impact=("6 centres de santé", "−72 % de ruptures de stock", "Traçabilité complète"),
                tonalite="bleu",
            ),
            Projet(
                nom="SolarGrid Katanga",
                secteur="Énergie Propre",
                province="Haut-Katanga",
                universite="Université de Lubumbashi (UNILU)",
                porteur="David Mwamba",
                description=(
                    "Mini-réseaux solaires prépayés installés sur les campus, avec "
                    "compteurs intelligents et maintenance assurée par des étudiants "
                    "ingénieurs formés en interne."
                ),
                phase="Mini-réseaux campus",
                statut="Validé — Cohorte 5",
                date_validation="07 février 2026",
                financement="Bourse d'amorçage 4 000 USD",
                icone="solar_power",
                impact=("3 campus équipés", "1 100 étudiants alimentés", "Facture divisée par 2"),
                tonalite="or",
            ),
            Projet(
                nom="AgriLog DRC",
                secteur="Logistique & Commerce",
                province="Kinshasa",
                universite="Université de Kinshasa (UNIKIN)",
                porteur="Naomie Tshilombo",
                description=(
                    "Plateforme de collecte et de distribution des produits maraîchers qui "
                    "relie directement les coopératives agricoles aux supermarchés et "
                    "restaurants de Kinshasa."
                ),
                phase="Scale-up régional",
                statut="Validé — Cohorte 3",
                date_validation="22 mars 2025",
                financement="Levée d'amorçage 25 000 USD",
                icone="local_shipping",
                impact=("14 emplois créés", "80 maraîchers reliés", "3 provinces desservies"),
                tonalite="profond",
            ),
            Projet(
                nom="Kilimo Hub",
                secteur="AgriTech & Climat",
                province="Kongo-Central",
                universite="Université Kongo (UKA)",
                porteur="Espérance Nzau",
                description=(
                    "Centrale de production de semences certifiées et de compost "
                    "organique pilotée par des coopératives paysannes encadrées par des "
                    "étudiants en agronomie."
                ),
                phase="Prototype validé",
                statut="Validé — Cohorte 6",
                date_validation="14 mai 2026",
                financement="Micro-subvention 2 500 USD",
                icone="compost",
                impact=("12 coopératives", "Semences certifiées", "Coût des intrants ÷ 3"),
                tonalite="bleu",
            ),
            Projet(
                nom="Salaama Ride",
                secteur="Mobilité Urbaine",
                province="Kinshasa",
                universite="Université de Kinshasa (UNIKIN)",
                porteur="Jonathan Mbala",
                description=(
                    "Service de transport partagé géolocalisé avec conductrices formées et "
                    "vérifiées, pensé pour sécuriser les trajets quotidiens des étudiantes "
                    "entre les communes et les campus."
                ),
                phase="Pilote — 300 courses",
                statut="Validé — Cohorte 6",
                date_validation="30 mai 2026",
                financement="Bourse d'amorçage 3 500 USD",
                icone="electric_rickshaw",
                impact=("300 courses sécurisées", "−40 % de coût", "12 conductrices formées"),
                tonalite="info",
            ),
            Projet(
                nom="ProfsConnect",
                secteur="EdTech",
                province="Tshopo",
                universite="Université de Kisangani (UNIKIS)",
                porteur="Bénédicte Angali",
                description=(
                    "Bibliothèque de cours hors ligne diffusée par SMS et clé USB pour les "
                    "élèves des zones sans connexion internet de la Tshopo."
                ),
                phase="Pilote — 8 écoles",
                statut="Validé — Cohorte 5",
                date_validation="03 mars 2026",
                financement="Micro-subvention 2 000 USD",
                icone="cast_for_education",
                impact=("8 écoles pilotes", "1 400 élèves suivis", "Fonctionne hors ligne"),
                tonalite="bleu",
            ),
            Projet(
                nom="CodeNa Biso",
                secteur="Intelligence Artificielle",
                province="Kasaï-Central",
                universite="Université de Kananga (UNIKAN)",
                porteur="Plamedi Muteba",
                description=(
                    "Modèle de traitement automatique du lingala et du swahili pour "
                    "traduire les documents administratifs et médicaux destinés aux "
                    "populations non francophones."
                ),
                phase="Recherche appliquée",
                statut="Validé — Cohorte 6",
                date_validation="21 avril 2026",
                financement="Bourse de recherche 3 000 USD",
                icone="neurology",
                impact=("Lingala ↔ français", "Modèle open source", "3 universités partenaires"),
                tonalite="or",
            ),
            Projet(
                nom="Mai-Ndombe Water",
                secteur="Eau & Assainissement",
                province="Maï-Ndombe",
                universite="Institut Supérieur de Développement Rural (ISDR)",
                porteur="Rachelle Bokolo",
                description=(
                    "Station de filtration solaire mobile fournissant de l'eau potable aux "
                    "villages enclavés, avec un suivi communautaire de la qualité de l'eau."
                ),
                phase="Test terrain",
                statut="Validé — Cohorte 6",
                date_validation="09 juin 2026",
                financement="Micro-subvention 2 800 USD",
                icone="water_drop",
                impact=("5 villages desservis", "1 200 personnes", "Filtration 100 % solaire"),
                tonalite="info",
            ),
        ]

    @staticmethod
    def _get_criteres() -> list[dict]:
        """Les étapes de validation d'un projet."""
        return [
            {
                "numero": "01",
                "titre": "Dépôt en ligne",
                "description": (
                    "Formulaire de candidature, note d'intention de 2 pages et vidéo de "
                    "présentation de 3 minutes."
                ),
                "icone": "upload_file",
                "tonalite": "bleu",
            },
            {
                "numero": "02",
                "titre": "Revue scientifique",
                "description": (
                    "Audit technique du comité scientifique : état de l'art, faisabilité "
                    "locale et disponibilité des compétences."
                ),
                "icone": "science",
                "tonalite": "profond",
            },
            {
                "numero": "03",
                "titre": "Audition du jury",
                "description": (
                    "Pitch de 5 minutes devant un jury mixte (académiques, industriels, "
                    "investisseurs) suivi d'une séance de questions."
                ),
                "icone": "gavel",
                "tonalite": "or",
            },
            {
                "numero": "04",
                "titre": "Validation & admission",
                "description": (
                    "Notification officielle, signature de la charte de confidentialité et "
                    "intégration de la cohorte d'incubation."
                ),
                "icone": "verified",
                "tonalite": "info",
            },
        ]

    @staticmethod
    def _get_criteres_fond() -> list[str]:
        """Les critères de fond évalués par le jury."""
        return [
            "Un problème réel documenté sur le terrain congolais",
            "Une solution différenciée par rapport à l'existant local",
            "Une équipe engagée, avec au moins un étudiant régulièrement inscrit",
            "Une faisabilité technique et financière démontrée",
            "Un potentiel d'impact social et d'emploi mesurable",
        ]

    @classmethod
    def _get_secteurs(cls, projets: list[Projet]) -> list[str]:
        """Liste des secteurs disponibles, préfixée par « Tous »."""
        return [cls.TOUS_LES_SECTEURS, *sorted({projet.secteur for projet in projets})]

    @classmethod
    def get_context(cls, secteur: str | None = None) -> dict:
        """Construit le contexte de la vue, filtré par secteur si demandé."""
        tous_les_projets = cls._get_projets()
        secteurs = cls._get_secteurs(tous_les_projets)

        secteur_actif = secteur if secteur in secteurs else cls.TOUS_LES_SECTEURS
        if secteur_actif == cls.TOUS_LES_SECTEURS:
            projets_affiches = tous_les_projets
        else:
            projets_affiches = [p for p in tous_les_projets if p.secteur == secteur_actif]

        return {
            "projets": projets_affiches,
            "secteurs": secteurs,
            "secteur_actif": secteur_actif,
            "nombre_total": len(tous_les_projets),
            "nombre_affiche": len(projets_affiches),
            "criteres": cls._get_criteres(),
            "criteres_fond": cls._get_criteres_fond(),
            "chiffres": [
                {
                    "valeur": "340",
                    "libelle": "Projets déposés",
                    "detail": "Depuis la première édition nationale",
                    "icone": "description",
                    "tonalite": "bleu",
                },
                {
                    "valeur": "128",
                    "libelle": "Projets validés",
                    "detail": "Admis en programme d'incubation",
                    "icone": "verified",
                    "tonalite": "profond",
                },
                {
                    "valeur": "62",
                    "libelle": "Projets financés",
                    "detail": "Bourses d'amorçage décaissées",
                    "icone": "payments",
                    "tonalite": "or",
                },
                {
                    "valeur": "26",
                    "libelle": "Provinces représentées",
                    "detail": "Tous les coins de la RDC",
                    "icone": "map",
                    "tonalite": "info",
                },
            ],
            "tags_hero": [
                "128 projets validés",
                "11 secteurs d'activité",
                "26 provinces",
            ],
        }
