# 🔐 Déchiffrement d’un code secret par recuit simulé

Ce projet implémente un **algorithme de recuit simulé** pour déchiffrer un message chiffré monoalphabétiquement, en utilisant une **matrice de probabilités de transitions entre lettres** (bigrammes).

---

## 🧠 Contexte

Vous trouvez un message chiffré :  FRNBRJMFBRNQXHFYNWSRNKRDNZLXDRDNMOOHCRFYNZXJJRNYSNKRDNBRDHORDNJMHDNBRDHORNWSNRKKRDNMOOHCRFYNZXJJRNRKKRDNMOOHCRFYNRYNYSNQOXDQROROMDNYXSVXSODNRQHZYRYR


On suppose qu’il s’agit d’un **chiffrement par substitution monoalphabétique**, où chaque lettre (et l’espace) a été remplacée par une autre, de manière fixe.  
Il existe alors **27! ≈ 10²⁸ permutations possibles**. Une attaque par force brute est donc irréaliste.

On pourrait aussi utiliser la fréquence des lettres (par exemple, l’espace ≈ 17.4 %, E ≈ 12.1 % en français), mais ce message est trop court pour rendre ces statistiques fiables.

Une approche plus robuste consiste à **exploiter les fréquences des paires de lettres (bigrammes)**, en construisant un score basé sur une **matrice de transition**.

---

## 📦 Fichiers

| Fichier                      | Description                                                         |
|-----------------------------|---------------------------------------------------------------------|
| `transitions_alphabets.txt` | Matrice 27×27 des probabilités de transitions (A–Z + espace).        |
| `MSG.txt`                   | Fichier contenant le message chiffré.                               |
| `Recuit_simule.ipynb`       | Script principal contenant l’implémentation du recuit simulé.       |

---

## 🔍 Description de l’algorithme

L'algorithme utilise la méthode du **recuit simulé (Simulated Annealing)** pour optimiser une permutation de l’alphabet.

### 🧮 Fonction objectif : log-vraisemblance

On cherche à maximiser la **log-vraisemblance** du message déchiffré avec une permutation :

```math
V = \frac{1}{N} \sum_{i=1}^{N-1} \log(P(c_i \to c_{i+1}))
```

```bash
Potentiel du message décodé : -2.0975792909151565

Message décodé :
NE DEMANDE POINT QUE LES CHOSES ARRIVENT COMME TU LES DESIRES MAIS DESIRE QU ELLES ARRIVENT COMME ELLES ARRIVENT ET TU PROSPERERAS TOUJOURS 
EPICTETE
```
## Librairies à installé
```bash
pip install numpy matplotlib random
```

##  References
- L'article Diaconis, P.(2009). The markove chaine monte carlo revolution. Bulletin of the American Mathematical Society, 42(2) 179-205.
- [Recuit simulé](https://fr.wikipedia.org/wiki/Recuit_simul%C3%A9)

- [Chaine TouTube de David Louapre](https://www.youtube.com/watch?v=z4tkHuWZbRA&t=415s&ab_channel=ScienceEtonnante)

