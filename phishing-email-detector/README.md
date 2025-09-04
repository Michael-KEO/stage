# Détecteur d'Emails de Phishing

Ce projet contient le pipeline d'entraînement et d'inférence d'un modèle de détection d'emails de phishing (NLP). Les artefacts de modèle utilisent le format safetensors et les notebooks Jupyter pour l'expérimentation.

## Structure du dépôt
- app/
  - phishing_detector_training.ipynb — notebook d'entraînement
  - phishing_detector_inference.ipynb — notebook d'inférence / évaluation
  - phishing-detector-model/ — modèle entraîné et fichiers associés (model.safetensors, tokenizer, config)
- data/
  - Phishing_Email.csv — dataset principal (exemples légitimes + phishing)
- results/ — checkpoints d'entraînement
- phishing-detector-model/ — emplacement cible pour modèles exportés
- requirements.txt — dépendances Python

## Objectif
Entraîner un modèle capable de classer un email comme légitime ou phishing, évaluer ses performances et fournir un notebook d'inférence pour déployer ou tester le modèle sur de nouveaux emails.

## Prérequis
- Python 3.8+
- pip installé
- GPU recommandé pour l'entraînement (optionnel selon modèle)
- Espace disque pour checkpoints et modèles

## Installation
Cloner le dépôt puis installer les dépendances :
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Utilisation rapide

1. Préparer les données  
   - Vérifier `data/Phishing_Email.csv`. Adapter le prétraitement si nécessaire (nettoyage, split train/test) depuis le notebook d'entraînement.

2. Entraînement (notebook)  
   - Ouvrir `app/phishing_detector_training.ipynb` dans Jupyter Lab/Notebook et exécuter les cellules dans l'ordre.  
   - Les checkpoints sont enregistrés dans `results/` et le modèle final dans `app/phishing-detector-model/`.

3. Inférence / évaluation (notebook)  
   - Ouvrir `app/phishing_detector_inference.ipynb`.  
   - Charger le modèle depuis `app/phishing-detector-model/` et exécuter les exemples d'inférence.  
   - Les notebooks contiennent des cellules pour les métriques (accuracy, precision, recall, F1) et des exemples d'export.

## Format du modèle
Le modèle entraîné est stocké dans `app/phishing-detector-model/` :
- model.safetensors — poids du modèle
- config.json, tokenizer_config.json, vocab.txt — méta et tokenizer
- special_tokens_map.json — tokens spéciaux

Ces fichiers permettent de recharger le modèle avec les bibliothèques compatibles (transformers / safetensors).

## Bonnes pratiques
- Utiliser un environnement isolé (venv/conda).  
- Sauvegarder régulièrement les checkpoints durant l'entraînement.  
- Évaluer sur un jeu de test séparé pour estimer la généralisation.  
- Pour export léger, n'exporter que les fichiers nécessaires au runtime (model + tokenizer + config).

## Débogage rapide
- Erreurs de dépendances : vérifier les versions dans `requirements.txt`.  
- OOM GPU : réduire batch_size ou entraîner sur CPU si nécessaire.  
- Tokenizer : s'assurer que le vocab/tokenizer utilisé pour l'inférence est le même qu'à l'entraînement.
