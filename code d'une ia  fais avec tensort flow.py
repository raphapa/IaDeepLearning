import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
func = lambda x: x+x
# Création d'un modèle séquentiel
model = Sequential()

# Ajout de la première couche dense
model.add(Dense(32, activation=func, input_shape=(1,)))

# Ajout d'une autre couche dense
model.add(Dense(32, activation=func))

# Ajout de la couche de sortie
model.add(Dense(1, activation='sigmoid'))

# Compilation du modèle
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

