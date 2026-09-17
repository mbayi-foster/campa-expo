/* ==========================================================================
   Interactions de la page d'accueil CAMPAEXPO RDC
   ========================================================================== */

/*
 * Navigation interne : chaque lien porte un attribut `data-path`
 * (ex. data-path="programmes"). Tant qu'aucun routeur n'est branché, les liens
 * gardent leur comportement par défaut (#). Dès qu'un `window.navigateToPath`
 * est défini par l'application hôte, il prend le relais.
 */
document.querySelectorAll("[data-path]").forEach(function (element) {
  element.addEventListener("click", function (evenement) {
    var cible = this.getAttribute("data-path");
    if (typeof window.navigateToPath === "function") {
      evenement.preventDefault();
      window.navigateToPath(cible);
    }
  });
});
