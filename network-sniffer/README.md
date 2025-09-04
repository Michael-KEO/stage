# network-sniffer

Projet d'entraînement et d'inférence de modèles ML pour détection d'anomalies / attaques réseau (utilise RAPIDS + cuDF + XGBoost GPU).

## Structure principale
- app/ : notebooks (prétraitement, entraînement, inference)
  - training_v1_raw.ipynb
  - training_v2_class_weight.ipynb
  - training_v3_class_weight_with_bot_weight_cap.ipynb
  - data_preprocessing.ipynb, data_processing.ipynb, inference.ipynb
- data/ : données sources et fichiers traités
  - processed_file_cleaned.csv (fichier principal utilisé)
  - train_test/ (X_train.csv, y_train.csv, etc.)
- models/ : modèles et artefacts (xgb_model_v*.json, label encoder .npy/.json)
- requirements.txt : dépendances Python
- rapids-jupyter.sh : script d'aide pour lancer Jupyter avec l'environnement RAPIDS

## Objectif
Entraîner un modèle XGBoost sur GPU, évaluer performances (classification report, matrice de confusion) et sauvegarder modèle + encodage des labels.

## Prérequis
- Machine Linux ou WSL2 avec GPU NVIDIA et drivers compatibles.
- CUDA installée et compatible avec la version de RAPIDS utilisée.
- Python 3.8+ (voir requirements.txt).
- Espace disque suffisant pour les données et caches GPU.

## Installation rapide
1. Cloner / ouvrir le dépôt (déjà placé dans `stage/network-sniffer`).
2. Installer dépendances (option locale ou via container) :
   - Option simple (venv/pip, si GPU et libs compatibles) :
     ```
     python -m venv .venv
     source .venv/bin/activate
     pip install -r requirements.txt
     ```
   - Recommandé : utiliser `rapids-jupyter.sh` (prépare / lance un environnement Jupyter avec RAPIDS). Voir section suivante.

## rapids-jupyter.sh
Le script `rapids-jupyter.sh` est fourni pour faciliter le démarrage d'un environnement Jupyter avec RAPIDS/cuDF. Il peut :
- préparer un environnement/container,
- vérifier variables GPU/CUDA,
- lancer `jupyter lab` dans le répertoire du projet.

Exemples d'utilisation :
```
chmod +x rapids-jupyter.sh
./rapids-jupyter.sh
```
Consulter le contenu du script pour adapter les options (port, token, montage de volumes, etc.).

## Exécution des notebooks
- Ouvrir Jupyter Lab (via le script ci‑dessus ou `jupyter lab`) et lancer :
  - `data_processing.ipynb` / `data_preprocessing.ipynb` pour préparer `processed_file_cleaned.csv`.
  - `training_v3_class_weight_with_bot_weight_cap.ipynb` (ou `training_v3_test.ipynb`) pour entraînement GPU avec gestion des poids de classes.
  - `inference.ipynb` pour chargement du modèle et prédictions.

## Résultats
- Modèle XGBoost : `models/xgb_model_v3.json` (exemples v1/v2/v3 présents).
- Encodage des labels : `models/label_encoder_classes_v3.npy` / `.json`.
- Graphiques et rapports affichés dans les notebooks.

## Conseils pratiques
- Vérifier la disponibilité GPU avant d'exécuter (nvidia-smi).
- Attention à la mémoire GPU lors d'opérations lourdes (one-hot sur hautes cardinalités).
- Faire des tests par petits sous-ensembles avant d'entraîner sur tout le dataset.
- Sauvegarder régulièrement les artefacts (`models/`) et checkpoints.

## Débogage rapide
- Erreurs cuDF/cuML : vérifier version RAPIDS vs CUDA.
- Problèmes d'OOM GPU : réduire batch / features / utiliser échantillonnage.
- Incompatibilités XGBoost GPU : vérifier `tree_method`, `device` et version XGBoost.

