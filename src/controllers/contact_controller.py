"""Contrôleur de la page « Contact ».

Rôle : afficher les coordonnées officielles et traiter les formulaires
(message de contact et inscription à la newsletter).
"""

from flask import current_app, flash, redirect, render_template, request, url_for

from src.services.contact_service import ContactService

#: Ancre vers laquelle on redirige après un envoi réussi.
ANCRE_NEWSLETTER = "#newsletter"
ANCRE_FORMULAIRE = "#formulaire"


class ContactController:
    """Orchestre l'affichage et le traitement de la page Contact."""

    @staticmethod
    def _page(contexte: dict):
        """Rend le gabarit de la page Contact."""
        contexte["page_title"] = "Nous contacter"
        contexte["app_name"] = current_app.config.get("APP_NAME", "CAMPAEXPO RDC")
        return render_template("contact/index.html", **contexte)

    @staticmethod
    def index():
        """Affiche la page Contact (GET) ou traite le formulaire (POST)."""
        if request.method == "POST":
            return ContactController._traiter_message()

        return ContactController._page(ContactService.get_context())

    @staticmethod
    def _traiter_message():
        """Valide puis enregistre un message envoyé depuis le formulaire."""
        formulaire = request.form.to_dict()
        erreurs = ContactService.valider_message(formulaire)

        if erreurs:
            flash(
                "Le formulaire contient des erreurs : merci de corriger les champs signalés.",
                "error",
            )
            contexte = ContactService.get_context(formulaire=formulaire, erreurs=erreurs)
            return ContactController._page(contexte), 400

        ContactService.enregistrer_message(formulaire)
        flash(
            "Message envoyé ! Le secrétariat vous répond sous 48 heures ouvrées.",
            "success",
        )
        return redirect(url_for("contact.index") + ANCRE_FORMULAIRE)

    @staticmethod
    def newsletter():
        """Inscrit une adresse email à la lettre d'information."""
        formulaire = request.form.to_dict()
        erreur = ContactService.valider_newsletter(formulaire)

        if erreur:
            flash(erreur, "error")
        else:
            ContactService.enregistrer_abonne(formulaire.get("email_newsletter", ""))
            flash(
                "Merci ! Votre adresse est inscrite à la newsletter CAMPAEXPO.",
                "success",
            )

        return redirect(url_for("contact.index") + ANCRE_NEWSLETTER)
