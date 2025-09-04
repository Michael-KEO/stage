Certains dossiers volumineux n'ont pas été inclus dans ce dépôt. Ils contiennent des jeux de données et des modèles trop lourds pour être versionnés ici. Pour que les projets fonctionnent correctement, téléchargez et placez les fichiers manquants dans les emplacements indiqués ci‑dessous.

Dossiers exclus (seules des entrées `.gitkeep` sont conservées) :
- network-sniffer/data/
- phishing-email-detector/app/results/
- phishing-email-detector/app/phishing-detector-model/

Récupération des données pour network-sniffer
- Lien de téléchargement : https://drive.google.com/file/d/1JL5Zl96omgYqfAkX4Efo87QccxFygsfd/view?usp=sharing
- Instructions (Windows + WSL) :
  1. Télécharger l'archive
  2. Copier dans le répertoire du projet et extraire :
     - `unzip project_data.zip -d data`
  3. Vérifier que les fichiers sont présents (ne pas supprimer .gitkeep) et déplacé les dans leurs emplacements respectifs :
     - `network-sniffer/data/`
     - `phishing-email-detector/app/results/`
     - `phishing-email-detector/app/phishing-detector-model/`

**Remarques**
- Les dossiers mentionnés ci‑dessus sont volontairement exclus du dépôt pour réduire sa taille. Si vous avez reçu un autre point de distribution (serveur, partage réseau ou lien privé), utilisez-le à la place du lien d'exemple.
- Après avoir placé les fichiers, vous pouvez lancer les notebooks ou les scripts présents dans chaque dossier.
