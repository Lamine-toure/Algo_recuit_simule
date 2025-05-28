# 🔐 Déchiffrement de message par Recuit Simulé

Ce projet implémente un **algorithme de recuit simulé** pour déchiffrer un message chiffré monoalphabétiquement, en utilisant une **matrice de probabilités de transitions entre lettres**.

---

## 📌 Objectif

L'objectif est de retrouver le message d'origine en trouvant une **permutation de l'alphabet** qui maximise la **vraisemblance statistique** du message déchiffré selon une matrice de transition issue de textes en français.

---

## 📦 Fichiers

- `transitions_alphabets.txt` : Matrice 27x27 des probabilités de transition entre lettres (A-Z + espace).
- `MSG.txt` : Fichier contenant le message chiffré.
- `Recuit_simule.ipynb` : Script principal implémentant l'algorithme.

---

## 🔍 Description de l'algorithme

L'algorithme utilise la **technique de recuit simulé** (Simulated Annealing) pour optimiser une permutation de l'alphabet qui déchiffre au mieux le message.

### Étapes clés :

1. **Initialisation** :
   - Une permutation aléatoire de l'alphabet est générée.
   - Un message chiffré est donné sous forme de liste de lettres majuscules.

2. **Énergie (fonction objectif)** :
   - On déchiffre le message selon la permutation actuelle.
   - On calcule la **log-vraisemblance** du texte déchiffré avec la matrice de transition :

    ```text  
     $ V = (1 / N) * Σ_{i=1}^{N-1} log(P(c_i → c_{i+1}))$  avec une petite constante ajoutée pour éviter log(0).

3. **Recuit simulé** :
   - À chaque itération, deux lettres de la permutation sont échangées pour former un nouvel état.
   - Ce nouvel état est accepté :
     - Toujours, s'il améliore l'énergie.
     - Sinon, avec une probabilité décroissante selon une température :
    
        ```text
       T = \frac{h}{\log(i + 2)}

     - Cela permet d’échapper aux minima locaux.

4. **Critère d'arrêt** :
   - L'algorithme s'arrête après `max_iter` itérations ou dès que l’énergie dépasse un seuil (`-2.12` dans notre cas).

---

## 📊 Visualisations

- **Évolution de l'énergie** :
  Visualisation de la convergence de l’algorithme.

- **Température** :
  Courbe décroissante montrant le refroidissement simulé.

---

## 📈 Résultat

```text
Potentiel du message décodé via la dernière permutation est : -2.0975792909151565
 Le Message décodé est --> NE DEMANDE POINT QUE LES CHOSES ARRIVENT COMME TU LES DESIRES MAIS DESIRE QU ELLES ARRIVENT COMME ELLES ARRIVENT ET TU PROSPERERAS TOUJOURS EPICTETE
