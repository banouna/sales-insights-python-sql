# Analyses SQL — Projet d'analyse des ventes

## 1. Chiffre d'affaires par produit

**Objectif :** identifier les produits qui génèrent le plus de chiffre d'affaires.

SELECT
    produit,
    SUM(quantite) AS quantite_totale,
    SUM(quantite * prix_unitaire) AS chiffre_affaire_total
FROM ventes
GROUP BY produit
ORDER BY chiffre_affaire_total DESC;

 Résultat

 produit  quantite_totale  chiffre_affaire_total
Ordinateur                8                   6800
     Ecran                8                   1760
    Casque               14                   1050
   Clavier               15                    675
    Souris               24                    600

**Interprétation :** l'ordinateur génère le chiffre d'affaires le plus élevé, avec 6 800 €. La souris est le produit vendu en plus grande quantité, avec 24 unités.


## 2. Chiffre d'affaires par catégorie

**Objectif :** déterminer les catégories qui contribuent le plus au chiffre d'affaires.
select categorie, sum(quantite)as quantite_totale,sum(quantite*prix_unitaire) as chiffre_affaire_total
from ventes
group by categorie
order by chiffre_affaire_total desc;

### Résultat
categorie  quantite_totale  chiffre_affaire_total
Informatique               16                   8560
 Accessoires               39                   1275
       Audio               14                   1050

La catégorie Informatique domine les ventes en valeur, avec 8 560 € de chiffre d'affaires.

 3. Chiffre d'affaires par ville

**Objectif :** identifier les villes qui génèrent le plus de revenus.
select ville, sum(quantite)as quantite_totale,sum(quantite*prix_unitaire) as chiffre_affaire_total
from ventes
group by ville
order by chiffre_affaire_total desc;

### Résultat
ville  quantite_totale  chiffre_affaire_total
    Paris               22                   4285
    Lille               18                   3435
     Lyon               13                   1790
Marseille               16                   1375
Paris occupe la première place

## 4. Chiffre d'affaires par jour

select date,(quantite*prix_unitaire) as chiffre_affaire_
from ventes
order by chiffre_affaire_ desc;
### Résultat
2026-09-06              2550
2026-09-01              1700
2026-09-08              1700
2026-09-03               850
2026-09-04               660
2026-09-02               440
2026-09-09               440
2026-09-07               375
2026-09-03               300
2026-09-05               270
2026-09-10               225
2026-09-07               220
2026-09-04               200
2026-09-10               180
2026-09-09               175
2026-09-05               150
2026-09-02               135
2026-09-01               125
2026-09-06               100
2026-09-08                90

Nous constatons que le six septembre, l'entreprise a généré beaucoup plus de chiffre d'affaire que tous les autres jours

## Conclusion

Ces requêtes SQL permettent d'analyser les ventes par produit, catégorie, ville et jour. Elles complètent les analyses réalisées avec Python, pandas et Matplotlib dans le cadre du projet.
