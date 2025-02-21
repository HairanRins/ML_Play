import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor 

# Charger les données prétraitées
X_test_scaled = np.load('../data/X_test_scaled.npy')
y_test = np.load('../data/y_test.npy') 

# Charger le modèle Forêts Aléatoires
rf_reg = RandomForestRegressor(n_estimators=100, random_state=42)
rf_reg.fit(X_test_scaled, y_test)
y_pred_rf = rf_reg.predict(X_test_scaled)

# Visualisation des prédictions vs valeurs réelles
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred_rf, alpha=0.7, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')
plt.xlabel('Prix Réels')
plt.ylabel('Prix Prédits')
plt.title('Comparaison des Prix Réels vs Prédits')
plt.savefig('../results/price_prediction_scatter.png', dpi=300)
plt.show()
