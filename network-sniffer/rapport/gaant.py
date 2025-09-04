import matplotlib.pyplot as plt
import pandas as pd

# Définition des tâches avec dictionnaire
taches = {
    "Prise en main / intégration": ["2025-04-01", "2025-04-07"],
    "Lecture & exploration": ["2025-04-08", "2025-04-19"],
    "Préparation des données": ["2025-04-22", "2025-05-03"],
    "Modélisation / expérimentation": ["2025-05-06", "2025-06-07"],
    "Rédaction du rapport": ["2025-06-10", "2025-06-27"],
    "Relecture / soutenance": ["2025-06-30", "2025-07-04"]
}

# Conversion en DataFrame
df = pd.DataFrame([
    {"Tâche": k, "Début": pd.to_datetime(v[0]), "Fin": pd.to_datetime(v[1])}
    for k, v in taches.items()
])
df["Durée"] = (df["Fin"] - df["Début"]).dt.days

# Création du diagramme de Gantt
fig, ax = plt.subplots(figsize=(10, 5))

# Affichage des barres de Gantt (ordre inversé pour lecture descendante)
for i, row in df[::-1].iterrows():
    ax.barh(row["Tâche"], row["Durée"], left=row["Début"], color="cornflowerblue")

# Format du graphique
ax.set_xlabel("Date")
ax.set_title("Déroulé du stage – Diagramme de Gantt")
plt.tight_layout()

# Affichage
plt.show()
