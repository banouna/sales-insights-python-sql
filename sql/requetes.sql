select date,(quantite*prix_unitaire) as chiffre_affaire_
from ventes
order by chiffre_affaire_ desc;