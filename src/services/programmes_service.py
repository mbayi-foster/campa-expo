"""Service de la page « Programmes ».

Rôle : préparer toutes les données affichées par la vue (programmes,
parcours d'accompagnement, agenda des événements, questions fréquentes).
Les données sont statiques ici ; il suffira de brancher une base de données
ou un appel API à cet endroit sans toucher aux routes ni aux vues.
"""

from src.models import Evenement, Programme


class ProgrammesService:
    """Fournit les données de la page Programmes."""

    @staticmethod
    def _get_chiffres() -> list[dict]:
        """Chiffres clés affichés en tête de page."""
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
                "detail": "Idées structurées et prototypées",
                "icone": "rocket",
                "tonalite": "or",
            },
            {
                "valeur": "62",
                "libelle": "Projets financés",
                "detail": "Bourses d'amorçage non dilutives",
                "icone": "payments",
                "tonalite": "profond",
            },
            {
                "valeur": "26",
                "libelle": "Provinces couvertes",
                "detail": "Via les comités CDU universitaires",
                "icone": "map",
                "tonalite": "info",
            },
        ]

    @staticmethod
    def _get_programmes() -> list[Programme]:
        """Les programmes phares, du campus jusqu'à l'exposition nationale."""
        return [
            Programme(
                slug="incubation-universitaire",
                nom="Incubation Universitaire",
                accroche="6 mois pour passer du mémoire au prototype industrialisable",
                description=(
                    "Le parcours de référence : laboratoire de prototypage, accès aux "
                    "infrastructures de 28 universités partenaires et bourse d'amorçage "
                    "pour valider le produit en conditions réelles."
                ),
                icone="biotech",
                duree="6 mois",
                format="Présentiel sur campus + suivi digital",
                public="Étudiants en L3, Master et diplômés depuis moins de 2 ans",
                prochaine_session="Cohorte 7 — Avril 2026",
                places="60 places (12 provinces pilotes)",
                avantages=(
                    "Bourse d'amorçage non dilutive jusqu'à 5 000 USD",
                    "Accès aux fablabs et laboratoires des universités partenaires",
                    "Espace de coworking au siège national de Kinshasa",
                    "Accompagnement juridique (SARL, OHADA, propriété intellectuelle)",
                ),
                etapes=(
                    "Diagnostic du projet et audit de l'état de l'art",
                    "Prototypage encadré par les ingénieurs des fablabs",
                    "Tests terrain et collecte de preuves clients",
                    "Structuration juridique et pitch devant les investisseurs",
                ),
                tonalite="bleu",
            ),
            Programme(
                slug="coaching-mentoring",
                nom="Coaching & Mentoring",
                accroche="1 session toutes les 2 semaines avec un dirigeant en activité",
                description=(
                    "Un matching personnalisé avec un mentor issu des multinationales, de "
                    "la diaspora ou des entreprises phares de la RDC, engagé dans une "
                    "charte de transmission active."
                ),
                icone="handshake",
                duree="12 mois renouvelables",
                format="Présentiel + visioconférence",
                public="Tous les porteurs de projets validés",
                prochaine_session="Matching continu toute l'année",
                places="+85 mentors certifiés disponibles",
                avantages=(
                    "Feuille de route trimestrielle co-signée avec le mentor",
                    "Accès au réseau d'anciens lauréats CAMPAEXPO",
                    "Revue de gestion mensuelle avec un expert-comptable",
                ),
                tonalite="profond",
            ),
            Programme(
                slug="formations-bootcamps",
                nom="Formations & Bootcamps",
                accroche="60 heures intensives pour maîtriser les compétences qui manquent",
                description=(
                    "Masterclasses certifiantes axées sur le codage applicatif, la gestion "
                    "financière d'exploitation, le droit des affaires OHADA, le marketing "
                    "digital et le pitch commercial."
                ),
                icone="terminal",
                duree="8 semaines · 60 heures",
                format="Bootcamps week-end + masterclasses en ligne",
                public="Toute la communauté universitaire de RDC",
                prochaine_session="Session intensive — Mai 2026",
                places="300 places par session",
                avantages=(
                    "Certificat co-signé par nos partenaires institutionnels",
                    "Supports pédagogiques et démos techniques réutilisables",
                    "Masterclasses animées par des directeurs généraux",
                    "Accès à vie aux rediffusions en ligne",
                ),
                tonalite="or",
            ),
            Programme(
                slug="grande-exposition",
                nom="Grande Exposition Annuelle",
                accroche="Le plus grand showroom étudiant d'Afrique centrale",
                description=(
                    "Trois jours pour exposer devant les investisseurs providentiels, les "
                    "ministères et les dirigeants industriels, signer des contrats et "
                    "concourir pour les Grands Prix d'Innovation."
                ),
                icone="stars",
                duree="3 jours",
                format="Présentiel (Kinshasa) + retransmission digitale",
                public="Startups étudiantes sélectionnées après audition",
                prochaine_session="18 au 20 Juin 2026 — Palais du Peuple",
                places="150 stands · 5 000 visiteurs attendus",
                avantages=(
                    "Grand Prix d'Innovation : 50 000 USD de dotations",
                    "Rencontres B2B programmées avec les fonds panafricains",
                    "Couverture médiatique nationale et panafricaine",
                ),
                tonalite="profond",
            ),
            Programme(
                slug="mobilisation-universitaire",
                nom="Mobilisation Universitaire (CDU)",
                accroche="Des comités étudiants permanents dans chaque université",
                description=(
                    "Les Comités de Développement Universitaires animent des cellules "
                    "permanentes sur les campus : sensibilisation, idéation, relais des "
                    "appels à candidatures et logistique des tours provinciaux."
                ),
                icone="groups",
                duree="Permanent (année académique)",
                format="Cellules étudiantes sur campus",
                public="Délégués étudiants, clubs scientifiques et associations",
                prochaine_session="Rentrée académique 2026-2027",
                places="2 délégués par université membre",
                avantages=(
                    "12 antennes provinciales actives",
                    "Formation en animation communautaire et gestion de projet",
                    "Badge officiel de représentation CAMPAEXPO",
                ),
                tonalite="info",
            ),
        ]

    @staticmethod
    def _get_parcours() -> list[dict]:
        """Le parcours du porteur de projet, étape par étape."""
        return [
            {
                "numero": "01",
                "titre": "Réveiller",
                "duree": "1 mois",
                "description": (
                    "Sensibilisation dans les auditoires, ateliers d'idéation et détection "
                    "des talents sur les 28 campus partenaires."
                ),
                "livrable": "Idée formalisée",
                "icone": "wb_twilight",
                "tonalite": "bleu",
            },
            {
                "numero": "02",
                "titre": "Structurer",
                "duree": "2 mois",
                "description": (
                    "Validation scientifique de la solution, étude de marché locale et "
                    "construction du modèle économique."
                ),
                "livrable": "Proposition de valeur",
                "icone": "architecture",
                "tonalite": "or",
            },
            {
                "numero": "03",
                "titre": "Former",
                "duree": "8 semaines",
                "description": (
                    "Bootcamp de 60 heures : plan financier, droit OHADA, marketing digital "
                    "et technique de pitch."
                ),
                "livrable": "Business plan",
                "icone": "model_training",
                "tonalite": "info",
            },
            {
                "numero": "04",
                "titre": "Accompagner",
                "duree": "12 mois",
                "description": (
                    "Mentorat bi-mensuel avec un dirigeant en activité et revue de gestion "
                    "mensuelle du prototype."
                ),
                "livrable": "Prototype testé",
                "icone": "support_agent",
                "tonalite": "bleu",
            },
            {
                "numero": "05",
                "titre": "Valoriser",
                "duree": "3 jours",
                "description": (
                    "Exposition nationale, signature de partenariats commerciaux et levée "
                    "de fonds d'amorçage devant les investisseurs."
                ),
                "livrable": "Société créée",
                "icone": "workspace_premium",
                "tonalite": "or",
            },
        ]

    @staticmethod
    def _get_evenements() -> list[Evenement]:
        """Agenda des événements à venir."""
        return [
            Evenement(
                jour="05",
                mois="Mai",
                annee="2026",
                titre="Hackathon RDC Innovation : Villes Durables",
                ville="Lubumbashi · Goma · Kinshasa",
                lieu="Campus UNILU, UNIGOM et UNIKIN",
                format="Hybride multi-campus",
                heure="48 heures non-stop",
                description=(
                    "Prototypage inter-universitaire sur l'assainissement urbain, la "
                    "mobilité douce et l'accès à l'énergie dans les communes de Kinshasa."
                ),
                places="300 participants · 60 équipes",
                action="Inscrire son équipe",
                tonalite="or",
            ),
            Evenement(
                jour="18",
                mois="Juin",
                annee="2026",
                titre="Grande Foire CAMPAEXPO Kinshasa",
                ville="Kinshasa",
                lieu="Palais du Peuple & campus UNIKIN",
                format="Présentiel",
                heure="09h00 — 18h00",
                description=(
                    "Exposition plénière de 150 startups étudiantes devant les fonds de "
                    "capital-risque panafricains, les ministères et les industriels."
                ),
                places="150 stands · 5 000 visiteurs",
                action="Réserver mon badge",
                tonalite="bleu",
            ),
            Evenement(
                jour="20",
                mois="Juin",
                annee="2026",
                titre="Nuit des Lauréats & Grands Prix d'Innovation",
                ville="Kinshasa",
                lieu="Palais du Peuple — Salle plénière",
                format="Présentiel + retransmission",
                heure="18h30 — 23h00",
                description=(
                    "Remise des Grands Prix d'Innovation (50 000 USD de dotations), "
                    "signature des conventions d'incubation et gala des partenaires."
                ),
                places="Sur invitation · retransmission ouverte",
                action="Suivre la cérémonie",
                tonalite="profond",
            ),
            Evenement(
                jour="11",
                mois="Juillet",
                annee="2026",
                titre="Masterclass : Financement d'Amorçage en RDC",
                ville="En ligne",
                lieu="Visioconférence (lien envoyé par email)",
                format="En ligne",
                heure="15h00 — 17h00",
                description=(
                    "Structures de financement, fonds de garantie, micro-subventions et "
                    "négociation avec les business angels congolais."
                ),
                places="500 places",
                action="Réserver ma place",
                tonalite="info",
            ),
            Evenement(
                jour="22",
                mois="Août",
                annee="2026",
                titre="Bootcamp Prototypage Express",
                ville="Kinshasa · Goma · Lubumbashi",
                lieu="Fablabs universitaires partenaires",
                format="Hybride",
                heure="3 jours · 09h00 — 17h00",
                description=(
                    "Conception, impression 3D et tests d'usage encadrés par les "
                    "ingénieurs des fablabs pour transformer une maquette en prototype."
                ),
                places="120 places",
                action="Candidater au bootcamp",
                tonalite="or",
            ),
            Evenement(
                jour="09",
                mois="Septembre",
                annee="2026",
                titre="Forum Diaspora & Investisseurs",
                ville="Kinshasa + Paris",
                lieu="Siège CAMPAEXPO & Maison de la RDC (Paris)",
                format="Hybride international",
                heure="14h00 — 20h00 (Kinshasa)",
                description=(
                    "Mise en relation des porteurs de projets avec la diaspora "
                    "entrepreneuriale et les fonds d'investissement européens."
                ),
                places="80 projets sélectionnés",
                action="Déposer ma candidature",
                tonalite="bleu",
            ),
            Evenement(
                jour="15",
                mois="Octobre",
                annee="2026",
                titre="Tournée Provinciale des CDU",
                ville="12 chefs-lieux de province",
                lieu="Universités partenaires",
                format="Présentiel",
                heure="Journées portes ouvertes",
                description=(
                    "Rencontres de proximité pour présenter les programmes, auditer les "
                    "projets locaux et installer les nouveaux comités étudiants."
                ),
                places="Entrée libre",
                action="Voir les étapes",
                tonalite="info",
            ),
        ]

    @staticmethod
    def _get_faq() -> list[dict]:
        """Questions fréquentes sur les programmes."""
        return [
            {
                "question": "L'inscription aux programmes est-elle payante ?",
                "reponse": (
                    "Non. L'ensemble des programmes est 100 % gratuit pour les étudiants "
                    "régulièrement inscrits dans un établissement d'enseignement supérieur "
                    "de la RDC et pour les diplômés de moins de deux ans."
                ),
            },
            {
                "question": "Puis-je candidater sans prototype ?",
                "reponse": (
                    "Oui. Une idée documentée suffit pour les étapes « Réveiller » et "
                    "« Structurer ». Le prototypage est justement pris en charge par les "
                    "fablabs des universités partenaires."
                ),
            },
            {
                "question": "Mon projet est-il protégé pendant l'évaluation ?",
                "reponse": (
                    "Chaque membre du jury et du comité scientifique signe une charte de "
                    "confidentialité. Les projets retenus bénéficient en plus d'un "
                    "accompagnement au dépôt de brevet ou de modèle d'utilité."
                ),
            },
            {
                "question": "Je suis dans une province sans antenne CDU, est-ce un frein ?",
                "reponse": (
                    "Non. Les bootcamps et masterclasses sont disponibles en ligne et la "
                    "plupart des rendez-vous sont hybrides. La tournée provinciale "
                    "d'octobre 2026 couvre les 12 chefs-lieux pour élargir le réseau."
                ),
            },
            {
                "question": "Que se passe-t-il une fois le projet validé ?",
                "reponse": (
                    "Vous intégrez la cohorte d'incubation : mentorat bi-mensuel, bourse "
                    "d'amorçage, revue de gestion mensuelle et sélection pour la Grande "
                    "Exposition annuelle."
                ),
            },
        ]

    @classmethod
    def get_context(cls) -> dict:
        """Construit le contexte complet à transmettre à la vue."""
        programmes = cls._get_programmes()
        return {
            "programmes": programmes,
            "parcours": cls._get_parcours(),
            "evenements": cls._get_evenements(),
            "faq": cls._get_faq(),
            "chiffres": cls._get_chiffres(),
            "tags_hero": [
                "26 provinces couvertes",
                "100 % gratuit",
                "28 universités partenaires",
            ],
        }
