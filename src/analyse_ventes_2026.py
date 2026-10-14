from pathlib import Path
from fonctions import(
    charger_donnees,
    verifier_donnees,
    nettoyage_necessaire,
    nettoyer_donnees,
    preparer_donnees,
    analyser_produits,
    analyser_villes,
    analyser_categoris,
    analyser_jours,
    generer_resume,
    exporter_resultats,
    creer_graphique,
    generer_rapport_html
    )
dossier_projet = Path(__file__).parent.parent
dossier_data =dossier_projet/ "data"
dossier_resultat= dossier_projet/ "resultats"
chemin= dossier_data/ "ventes_2026.csv"
def main():
    df = charger_donnees(chemin)
    verifier_donnees(df)
    if nettoyage_necessaire(df):
        df= nettoyer_donnees(df)
    else:
        print("Aucune anomalie déctectée nettoyage inutile")
    df = preparer_donnees(df)
    produits = analyser_produits(df)
    print("\n========= Vente par produit =========:")
    print("\n",produits)
    print("\n========= Vente par ville =========:")
    villes=analyser_villes(df)
    print("\n",villes)
    print("\n========= Vente par categorie =========:")
    categories=analyser_categoris(df)
    print("\n",categories)
    print("\n========= Chiffre d'affaire par jour =========:")
    chiffre_affaire_jour=analyser_jours(df)
    print("\n",chiffre_affaire_jour)
    generer_resume(produits,villes,categories)
    exporter_resultats(produits,dossier_resultat/"ventes_par_produit.csv")
    exporter_resultats(produits,dossier_resultat/"part_chiffre_affaire_par_produit.csv")
    exporter_resultats(villes,dossier_resultat/"ventes_par_ville.csc")
    exporter_resultats(categories,dossier_resultat/"ventes_par_categorie.csv")
    exporter_resultats(chiffre_affaire_jour,dossier_resultat/"chiffre-affaire_par_jour.csv")
    creer_graphique(produits,"Produit",dossier_resultat/"chiffre_affaire_par_produit.png")
    creer_graphique(chiffre_affaire_jour,"Date",dossier_resultat/"chiffre_affaire_par_jour.png")
    creer_graphique(produits,"Produit",dossier_resultat/"part_chiffre_affaire_par_produit.png",kind="pie")
    creer_graphique(villes,"Ville",dossier_resultat/"chiffre_affaire_par_ville.png")
    creer_graphique(categories,"Catégorie",dossier_resultat/"chiffre_affaire_par_categorie.png")
    # Générer le rapport HTML
    generer_rapport_html(df,produits,villes,categories,chiffre_affaire_jour,dossier_resultat / "rapport_ventes.html")
if __name__ == "__main__":
    main()