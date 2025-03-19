# 🎭 Beyond the Smile: Capturing Micro Expressions with Event-based Vision

Ce projet explore l'utilisation de caméras événementielles et de réseaux de neurones à impulsions pour détecter et analyser les micro-expressions faciales.

## 📋 Table des matières

1. [Introduction](#introduction)
2. [Technologie](#technologie)
3. [Méthodologie](#méthodologie)
4. [Dataset](#dataset)
5. [Résultats](#résultats)
6. [Discussion](#discussion)
7. [Conclusion](#conclusion)

## 🎬 Introduction

Les micro-expressions, ces mouvements faciaux brefs et involontaires, révèlent nos véritables émotions. Ce projet vise à les capturer grâce à la vision basée sur les événements et l'intelligence artificielle.

## 💻 Technologie

- **Caméras événementielles** : Capture les changements de scène avec une résolution temporelle microseconde
- **Réseaux de neurones à impulsions (SNN)** : Traitement neuromorphique des données événementielles
- **SpikingJelly** : Bibliothèque Python pour l'implémentation de SNN

## 🧠 Méthodologie

1. Capture des micro-expressions avec une caméra événementielle
2. Prétraitement des données événementielles
3. Entraînement d'un SNN basé sur l'architecture SEWResNet
4. Classification des micro-expressions en 7 catégories

## 📊 Dataset

- 233 vidéos, ~8 secondes chacune
- 7 classes de micro-expressions :
  - Lever de paupière supérieure (14.2%)
  - Sourire (13.3%)
  - Bouche ouverte (17.2%)
  - Plissement du nez (13.3%)
  - Froncement des sourcils (15.0%)
  - Clignement des yeux (13.7%)
  - Contraction de la mâchoire (13.3%)

## 🏆 Résultats

- Précision maximale de 43.18% sur les 7 catégories
- Précision de 95.45% sur un sous-ensemble spécifique
- Amélioration par rapport aux méthodes traditionnelles (CNN : 30.95%)

## 💡 Discussion

### Avantages
- Haute résolution temporelle
- Détection précise des mouvements rapides
- Efficacité énergétique

### Limitations
- Sensibilité au bruit
- Complexité algorithmique

## 🚀 Travaux futurs

- Exploration de techniques d'apprentissage avancées
- Intégration de mécanismes d'attention
- Amélioration de la robustesse dans des environnements complexes

## 🎓 Conclusion

Ce projet ouvre de nouvelles perspectives pour la reconnaissance des émotions, avec des applications potentielles en psychologie, sécurité et interaction homme-machine.

---

👨‍🔬 Réalisé par Victor MAYAUD et Elliot BOUCHY, EURECOM, France.
