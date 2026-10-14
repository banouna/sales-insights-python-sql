import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
def charger_donnees(chemin_fichier):
    df= pd.read_csv(chemin_fichier)
    return df
def verifier_donnees(df):
    print("Nombre de lignens::",len(df))
    print("\n Valeurs manquantes en colonne:",df.isnull().sum())
    print("\n Nombre de lignes en double:",df.duplicated().sum())
def nettoyage_necessaire(df):
    doublons=df.duplicated().sum()
    nbcasesvide=df.isnull().sum().sum()
    if doublons>0 | nbcasesvide>0:
        return True
    else:
        return False
def nettoyer_donnees(df):
    df = df.copy()
    df= df.drop_duplicates()
    colonnes_essentielles=["date","produit","quantite","prix_unitaire","ville"]
    df= df.dropna(subset=colonnes_essentielles)
    df = df[(df["quantite"]>=0)&(df["prix_unitaire"]>=0)]
    return df
def preparer_donnees(df):
    df=df.copy()
    df["chiffre_affaire"]=df["quantite"]*df["prix_unitaire"]
    return df
def analyser_produits(df):
    resume= df.groupby("produit").agg(quantite_totale=("quantite","sum"),
                                      chiffre_affaire_total=("chiffre_affaire","sum"))
    resume= resume.sort_values(by="chiffre_affaire_total",ascending= False)
    return resume
def analyser_jours(df):
    df = df.copy()

    df["date"] = pd.to_datetime(df["date"])

    resume = df.groupby("date").agg(
        quantite_totale=("quantite", "sum"),
        chiffre_affaire_total=("chiffre_affaire", "sum")
    )
    return resume.sort_index()
def analyser_villes(df):
    resume=df.groupby("ville").agg(quantite_totale=("quantite","sum"),
                                   chiffre_affaire_total=("chiffre_affaire","sum"))
    return resume.sort_values(by="chiffre_affaire_total",ascending=False)
def analyser_categoris(df):
    resume=df.groupby("categorie").agg(quantite_totale=("quantite","sum"),
                                       chiffre_affaire_total=("chiffre_affaire","sum"))
    return resume.sort_values(by="chiffre_affaire_total",ascending=False)
def exporter_resultats(df,chemin_image):
    df.to_csv(chemin_image,encoding="utf-8-sig")
def creer_graphique_secteur(produits, chemin_image):
    plt.figure(figsize=(8, 8))
    plt.pie(
        produits["chiffre_affaire_total"],
        labels=produits["produit"],
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Répartition du chiffre d'affaires par produit")
    plt.tight_layout()
    plt.savefig(chemin_image, dpi=150)
    plt.close()
def creer_graphique(classement, nom_analyse, chemin_image, kind="bar"):

    if kind == "pie":
        classement["chiffre_affaire_total"].plot(
            kind="pie",
            labels=classement.index,
            autopct="%1.1f%%",
            startangle=90
        )
        plt.title(f"Répartition du chiffre d'affaires par {nom_analyse}")
        plt.ylabel("")
    else:
        classement["chiffre_affaire_total"].plot(kind=kind)

        plt.title(f"Chiffre d'affaires par {nom_analyse}")
        plt.xlabel(nom_analyse.capitalize())
        plt.ylabel("Chiffre d'affaires (€)")
        plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig(chemin_image, dpi=150)
    plt.close()
def generer_resume(produits,villes,categories):
    meilleur_produit=produits["chiffre_affaire_total"].idxmax()
    mt_meilleur_p=produits["chiffre_affaire_total"].max()
    meilleur_ville=villes["chiffre_affaire_total"].idxmax()
    mt_meilleur_v=villes["chiffre_affaire_total"].max()
    meilleur_categorie=categories["chiffre_affaire_total"].idxmax()
    mt_meilleur_c=categories["chiffre_affaire_total"].max()
    chiffre_af_total_global=produits["chiffre_affaire_total"].sum()
    produits["pourcentage_CA_par_produit"]=(produits["chiffre_affaire_total"]/produits["chiffre_affaire_total"].sum())*100
    print("\n=============== RAPPORT DES VENTES ===============")
    print(f"Chifre d'affaire total est: {chiffre_af_total_global:,.2f} eurro")
    print(f"Meilleur Produit: {meilleur_produit} {mt_meilleur_p:,.2f} eurro")
    print(f"Meilleur Ville: {meilleur_ville} {mt_meilleur_v:,.2f} eurro")
    print(f"Meilleur Categorie: {meilleur_categorie} {mt_meilleur_c:,.2f} eurro")
    print("\n",f"Part de chiffre d'affaire en % par {produits["pourcentage_CA_par_produit"]}")
    print("==================================================")
def generer_rapport_html(df, produits, villes, categories, jours,chemin_rapport):
    # 1. Calculer les indicateurs principaux
    chiffre_affaires_total = df["chiffre_affaire"].sum()
    quantite_totale = df["quantite"].sum()
    nombre_produits = df["produit"].nunique()

    meilleur_produit = produits["chiffre_affaire_total"].idxmax()
    ca_meilleur_produit = produits["chiffre_affaire_total"].max()

    meilleure_ville = villes["chiffre_affaire_total"].idxmax()
    ca_meilleure_ville = villes["chiffre_affaire_total"].max()

    meilleure_categorie = categories["chiffre_affaire_total"].idxmax()
    ca_meilleure_categorie = categories["chiffre_affaire_total"].max()

    # 2. Transformer les tableaux Pandas en tableaux HTML
    tableau_produits = produits.to_html(
        classes="tableau",
        border=0,
        float_format=lambda valeur: f"{valeur:,.2f}"
    )

    tableau_villes = villes.to_html(
        classes="tableau",
        border=0,
        float_format=lambda valeur: f"{valeur:,.2f}"
    )

    tableau_categories = categories.to_html(
        classes="tableau",
        border=0,
        float_format=lambda valeur: f"{valeur:,.2f}"
    )
    tableau_jours = jours.to_html(
    classes="tableau",
    border=0,
    float_format=lambda valeur: f"{valeur:,.2f}"
    )
    # 3. Préparer les graphiques déjà créés
    dossier_rapport = Path(chemin_rapport).parent
    noms_graphiques = [
             "chiffre_affaire_par_produit.png",
            "chiffre_affaire_par_ville.png",
            "chiffre_affaire_par_categorie.png",
            "chiffre_affaire_par_jour.png",
            "part_chiffre_affaire_par_produit.png"  ]
    blocs_graphiques = []

    for nom_image in noms_graphiques:
        chemin_image = dossier_rapport / nom_image

        if chemin_image.exists():
            blocs_graphiques.append(
                f'<img src="{nom_image}" alt="{nom_image}">'
            )
    graphiques_html = "\\n".join(blocs_graphiques)

    # 4. Construire la page HTML
    html = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Rapport des ventes</title>

        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 1100px;
                margin: 40px auto;
                padding: 0 20px;
                color: #263238;
                background: #f5f7fa;
            }}

            h1, h2 {{
                color: #17365d;
            }}

            .indicateurs {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 16px;
            }}

            .carte {{
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 2px 8px #00000012;
            }}

            .valeur {{
                font-size: 24px;
                font-weight: bold;
                color: #176b50;
            }}

            .section {{
                background: white;
                padding: 24px;
                margin-top: 24px;
                border-radius: 10px;
                overflow-x: auto;
            }}

            .tableau {{
                border-collapse: collapse;
                width: 100%;
            }}

            .tableau th, .tableau td {{
                padding: 10px;
                border-bottom: 1px solid #dddddd;
                text-align: right;
            }}

            .tableau th:first-child, .tableau td:first-child {{
                text-align: left;
            }}

            .tableau th {{
                background: #eaf0f6;
            }}

            img {{
                display: block;
                max-width: 100%;
                height: auto;
                margin: 20px auto;
            }}

            footer {{
                margin: 30px 0;
                color: #65727c;
                font-size: 13px;
            }}
        </style>
    </head>

    <body>
        <h1>Rapport d'analyse des ventes</h1>

        <p>
        Ce rapport présente une analyse des ventes à partir des données enregistrées.
        Il permet d'évaluer les performances commerciales, d'identifier les produits
        les plus performants et d'observer la répartition du chiffre d'affaires
        par produit, par ville, par catégorie et par jour.
        </p>
        <p>Synthèse des performances commerciales.</p>

        <div class="indicateurs">
            <div class="carte">
                <p>Chiffre d'affaires total</p>
                <div class="valeur">{chiffre_affaires_total:,.2f} €</div>
            </div>

            <div class="carte">
                <p>Quantités vendues</p>
                <div class="valeur">{quantite_totale}</div>
            </div>

            <div class="carte">
                <p>Nombre de produits distincts</p>
                <div class="valeur">{nombre_produits}</div>
            </div>
        </div>

        <div class="section">
            <h2>Principaux résultats</h2>
            <p><strong>Meilleur produit :</strong>
               {meilleur_produit} — {ca_meilleur_produit:,.2f} €</p>
            <p><strong>Meilleure ville :</strong>
               {meilleure_ville} — {ca_meilleure_ville:,.2f} €</p>
            <p><strong>Meilleure catégorie :</strong>
               {meilleure_categorie} — {ca_meilleure_categorie:,.2f} €</p>
        </div>

        <div class="section">
            <h2>Analyse par produit</h2>
            <p>Ce tableau présente les quantités vendues,le chiffre d'affaires et son pourcentage générés.L'ordre est en fonction du chiffre d'affaire du plus important au moins. Il permet de comparer les performances commerciales et d'identifier les produits qui contribuent le plus au chiffre d'affaires total.</p>
            {tableau_produits}
            <p>Ordinateur vient largement en tête avec un chiffre d'affaires de 6800 Euros puis Ecran avec 1760 après arrive Casque avec 1050 en suite Clavier avec 675 et en fin Souris avec 600 Euros</p>
        </div>

        <div class="section">
            <h2>Analyse par ville</h2>
            <p>Ce tableau compare les ventes réalisées dans les différentes villes. Il permet de repérer les marchés géographiques les plus performants et ceux dans lesquels des actions commerciales pourraient être envisagées.</p>
            {tableau_villes}
            <p>Paris occupe la première place avec un chiffre d'affaires de 4285 Euros.</p>
        </div>

        <div class="section">
            <h2>Analyse par catégorie</h2>
            <p>Ce tableau regroupe les ventes par catégorie de produits. Il aide à comprendre quelles familles de produits génèrent le plus de chiffre d'affaires et à comparer leur poids dans l'activité commerciale..</p>
            {tableau_categories}
            <p>La catégorie informatique prend la première place avec un chiffre d'affaires de 8560 Euros.</p>
        </div>
        <div class="section">
            <h2>Chiffre d'affaires par jour</h2>
            <p>Ce tableau présente les quantités vendues et le chiffre d'affaires pour chaque date. Il permet de suivre l'évolution quotidienne de l'activité et de repérer les journées les plus et les moins performantes.</p>
                {tableau_jours}
            <p> Nous constatons que le six septembre, l'entreprise a généré beaucoup plus de chiffre d'affaires que les autres jours avec un montant de 2650 Euros</p> 
        </div>
        <div class="section">
            <h2>Graphiques</h2>
            <p>Ces graphiques illustrent visuellement les tableaux ci-dessus</p>
            {graphiques_html}
        </div>
        <div class="section">
                <h2>Conclusion</h2>
                <p>L'analyse des ventes réalisées sur la période étudiée permet d'obtenir une vision globale des performances commerciales. Avec un chiffre d'affaires total de 10 885 € pour 69 unités vendues, les résultats mettent en évidence des différences importantes entre les produits et les catégories.</p>
                <p>Les ordinateurs constituent le principal moteur du chiffre d'affaires, avec 6 800 €, soit environ 62,5 % du total. La catégorie Informatique occupe également une place prépondérante, avec 8 560 € de chiffre d'affaires. Ces résultats montrent que les ventes reposent principalement sur les produits informatiques.</p>
                <p>L'analyse par ville permet de comparer les performances commerciales selon la localisation, tandis que l'étude quotidienne met en évidence les variations du chiffre d'affaires au cours de la période. Ces informations peuvent aider à mieux comprendre la répartition des ventes et à identifier les axes d'amélioration.</p>
                <p>En conclusion, cette analyse constitue une base utile pour orienter les décisions commerciales. Il serait pertinent de renforcer les actions autour des produits les plus performants, d'étudier les opportunités de développement pour les autres catégories et d'approfondir l'analyse des ventes par ville et par période. Une étude sur une période plus longue permettrait de confirmer ces tendances et d'identifier d'éventuelles évolutions saisonnières.</p>
        </div>

        <footer>
            Rapport généré automatiquement avec Python, Pandas et Matplotlib.
        </footer>
    </body>
    </html>
    """

    # 5. Enregistrer le rapport
    chemin_rapport = Path(chemin_rapport)
    chemin_rapport.parent.mkdir(parents=True, exist_ok=True)
    chemin_rapport.write_text(html, encoding="utf-8")

    print(f"Rapport généré : {chemin_rapport}")