"""Service de la page « Contact ».

Rôle : exposer les canaux de contact officiels, les réseaux sociaux, les
antennes régionales, et traiter les messages du formulaire ainsi que les
inscriptions à la newsletter.
"""

from flask import current_app


class ContactService:
    """Fournit les données et la logique de la page Contact."""

    #: Sujets proposés dans la liste déroulante du formulaire.
    SUJETS = (
        "Candidature à un programme",
        "Partenariat institutionnel ou corporate",
        "Devenir mentor ou membre du jury",
        "Presse, médias et interviews",
        "Rejoindre un comité CDU",
        "Autre demande",
    )

    @staticmethod
    def _get_identite() -> dict:
        """Coordonnées officielles de la direction nationale."""
        return {
            "adresse": "Boulevard du 30 Juin, Immeuble Sozacom, 4ᵉ niveau",
            "ville": "Gombe — Kinshasa, République Démocratique du Congo",
            "repere": "À 300 m de la Place du 30 Juin, entrée côté avenue Tombalbaye",
            "horaires": "Lundi → Vendredi : 08h30 — 17h00",
            "horaires_samedi": "Samedi : sur rendez-vous",
            "whatsapp": "+243 820 000 120",
            "whatsapp_lien": "https://wa.me/243820000120",
            "telephones": (
                {"libelle": "Direction nationale", "numero": "+243 820 000 120"},
                {"libelle": "Secrétariat des programmes", "numero": "+243 990 000 121"},
            ),
            "emails": (
                {
                    "adresse": "secretariat@campaexpo-rdc.cd",
                    "objet": "Secrétariat général & informations",
                },
                {
                    "adresse": "projets@campaexpo-rdc.cd",
                    "objet": "Candidatures, dossiers et suivi des cohortes",
                },
                {
                    "adresse": "partenariats@campaexpo-rdc.cd",
                    "objet": "Partenariats, mécénat et mentorat",
                },
                {
                    "adresse": "presse@campaexpo-rdc.cd",
                    "objet": "Presse, médias et demandes d'interview",
                },
            ),
        }

    @staticmethod
    def _get_reseaux_sociaux() -> list[dict]:
        """Comptes officiels CAMPAEXPO RDC."""
        return [
            {
                "nom": "Facebook",
                "identifiant": "/CAMPAEXPORDC",
                "detail": "Annonces officielles et lives de la Foire",
                "lien": "https://www.facebook.com/CAMPAEXPORDC",
                "icone": "public",
                "tonalite": "bleu",
            },
            {
                "nom": "Instagram",
                "identifiant": "@campaexpo.rdc",
                "detail": "Coulisses des cohortes et portraits de lauréats",
                "lien": "https://www.instagram.com/campaexpo.rdc",
                "icone": "photo_camera",
                "tonalite": "or",
            },
            {
                "nom": "LinkedIn",
                "identifiant": "/company/campaexpo-rdc",
                "detail": "Réseau des mentors, partenaires et alumni",
                "lien": "https://www.linkedin.com/company/campaexpo-rdc",
                "icone": "work",
                "tonalite": "profond",
            },
            {
                "nom": "X (Twitter)",
                "identifiant": "@campaexpo_rdc",
                "detail": "Fil d'actualité des appels à candidatures",
                "lien": "https://x.com/campaexpo_rdc",
                "icone": "tag",
                "tonalite": "info",
            },
            {
                "nom": "YouTube",
                "identifiant": "/@campaexpo-rdc",
                "detail": "Pitches des lauréats et masterclasses en replay",
                "lien": "https://www.youtube.com/@campaexpo-rdc",
                "icone": "smart_display",
                "tonalite": "bleu",
            },
            {
                "nom": "TikTok",
                "identifiant": "@campaexpo.rdc",
                "detail": "Formats courts pour les étudiants des campus",
                "lien": "https://www.tiktok.com/@campaexpo.rdc",
                "icone": "music_note",
                "tonalite": "or",
            },
        ]

    @staticmethod
    def _get_antennes() -> list[dict]:
        """Antennes provinciales et leurs contacts directs."""
        return [
            {
                "province": "Haut-Katanga",
                "ville": "Lubumbashi",
                "responsable": "Coordination Sud-Est",
                "telephone": "+243 990 000 122",
                "email": "lubumbashi@campaexpo-rdc.cd",
            },
            {
                "province": "Nord-Kivu",
                "ville": "Goma",
                "responsable": "Coordination Grands Lacs",
                "telephone": "+243 990 000 123",
                "email": "goma@campaexpo-rdc.cd",
            },
            {
                "province": "Sud-Kivu",
                "ville": "Bukavu",
                "responsable": "Antenne universitaire UCB",
                "telephone": "+243 990 000 124",
                "email": "bukavu@campaexpo-rdc.cd",
            },
            {
                "province": "Kongo-Central",
                "ville": "Matadi",
                "responsable": "Coordination Ouest",
                "telephone": "+243 990 000 125",
                "email": "matadi@campaexpo-rdc.cd",
            },
        ]

    @staticmethod
    def _get_faq() -> list[dict]:
        """Questions fréquentes relatives aux échanges avec l'équipe."""
        return [
            {
                "question": "Sous quel délai obtient-on une réponse ?",
                "reponse": (
                    "Le secrétariat répond en 48 heures ouvrées par email. Pour une "
                    "demande urgente, le WhatsApp officiel est suivi du lundi au samedi "
                    "de 08h00 à 18h00 (heure de Kinshasa)."
                ),
            },
            {
                "question": "Puis-je déposer ma candidature par email ?",
                "reponse": (
                    "Oui, en écrivant à projets@campaexpo-rdc.cd avec la note d'intention "
                    "et la présentation de l'équipe. Le dépôt en ligne reste la voie "
                    "recommandée car il déclenche l'accusé de réception automatique."
                ),
            },
            {
                "question": "Comment inviter CAMPAEXPO dans mon université ?",
                "reponse": (
                    "Écrivez via le formulaire en choisissant « Rejoindre un comité CDU » : "
                    "la coordination nationale étudie la demande avec le rectorat, puis "
                    "programme une tournée de sensibilisation."
                ),
            },
        ]

    @classmethod
    def get_context(cls, formulaire: dict | None = None, erreurs: dict | None = None) -> dict:
        """Construit le contexte complet de la page Contact."""
        return {
            "identite": cls._get_identite(),
            "reseaux_sociaux": cls._get_reseaux_sociaux(),
            "antennes": cls._get_antennes(),
            "faq": cls._get_faq(),
            "sujets": cls.SUJETS,
            "formulaire": formulaire or {},
            "erreurs": erreurs or {},
            "tags_hero": [
                "Réponse sous 48 h",
                "6 réseaux officiels",
                "4 antennes provinciales",
            ],
        }

    # ---------------------------------------------------------------- traitement

    @staticmethod
    def _email_valide(adresse: str) -> bool:
        """Vérification volontairement simple d'une adresse email."""
        adresse = adresse.strip()
        if " " in adresse or adresse.count("@") != 1:
            return False
        local, _, domaine = adresse.partition("@")
        return bool(local) and "." in domaine and not domaine.startswith(".") and not domaine.endswith(".")

    @classmethod
    def valider_message(cls, donnees: dict) -> dict:
        """Contrôle le formulaire de contact et retourne les erreurs trouvées."""
        erreurs: dict[str, str] = {}

        if not donnees.get("nom", "").strip():
            erreurs["nom"] = "Merci d'indiquer votre nom complet."
        if not cls._email_valide(donnees.get("email", "")):
            erreurs["email"] = "Merci d'indiquer une adresse email valide."
        if not donnees.get("sujet", "").strip():
            erreurs["sujet"] = "Merci de choisir un sujet."
        if len(donnees.get("message", "").strip()) < 20:
            erreurs["message"] = "Le message doit contenir au moins 20 caractères."

        return erreurs

    @staticmethod
    def enregistrer_message(donnees: dict) -> None:
        """Journalise la demande reçue.

        Aucun email n'est envoyé à ce stade : il suffira de brancher ici un
        client SMTP (Flask-Mail, API transactionnelle) sans toucher aux vues.
        """
        current_app.logger.info(
            "Nouveau message de contact — %s <%s> · sujet : %s",
            donnees.get("nom"),
            donnees.get("email"),
            donnees.get("sujet"),
        )

    @classmethod
    def valider_newsletter(cls, donnees: dict) -> str | None:
        """Valide l'inscription newsletter et retourne un message d'erreur éventuel."""
        if not cls._email_valide(donnees.get("email_newsletter", "")):
            return "Merci d'indiquer une adresse email valide pour l'abonnement."
        return None

    @staticmethod
    def enregistrer_abonne(email: str) -> None:
        """Journalise l'abonnement à la newsletter."""
        current_app.logger.info("Nouvel abonné newsletter — %s", email)
