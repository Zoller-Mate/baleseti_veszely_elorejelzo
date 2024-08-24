import pandas as pd

# Adat betöltése
dataset = pd.read_csv('baleseti_veszely_data.csv')

# Célváltozó és prediktorok szétválasztása
x = dataset.drop(columns=["baleseti_veszely_merteke"])
y = dataset["baleseti_veszely_merteke"] - 1  # Címkék 0-alapúvá tétele

# Adatok szétválasztása tanító és teszt halmazokra
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)


from sklearn.preprocessing import StandardScaler


#adatok normalizálása - nem tudom mennyit segít
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)



# Modell definiálása és tanítása
import tensorflow as tf

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(256, input_shape=(x_train.shape[1],), activation='sigmoid'))
model.add(tf.keras.layers.Dense(256, activation='sigmoid'))
model.add(tf.keras.layers.Dense(5, activation='softmax'))  # softmax az utolsó réteghez

# Modell fordítása
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Modell illesztése
model.fit(x_train, y_train, epochs=100)


model.save('baleseti_elorejelzo.keras')
