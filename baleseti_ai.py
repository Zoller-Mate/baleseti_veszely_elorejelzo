import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler

import os
import platform

def clear_console():
    # A platform függvény segítségével ellenőrizzük az operációs rendszert
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


# Modell betöltése
model = tf.keras.models.load_model('baleseti_elorejelzo.keras')

# StandardScaler inicializálása (ugyanúgy kell konfigurálni, mint tanításkor)
scaler = StandardScaler()

# Funkció az adat bekérésére
def get_user_input():
    
    print("\nAdd meg az alábbi adatokat:")

    ido_be = input("Idő (óra:perc): ").split(":")
    ido = float(ido_be[0]*60 + ido_be[1])


    auto_muszaki_allapota = float(input("Autó műszaki állapota (1-10): "))
    KSS = float(input("Sofőr fáradtsági szin - KSS (1-9): "))
    vezetesi_tapasztalat = float(input("Vezetési tapasztalat (év): "))
    RQI = float(input("Út minősége - RQI (0-10): "))
    forgalom_surusege = float(input("Forgalom sűrűsége (veh/km): "))
    latasi_viszonyok = float(input("Látási viszonyok (%): "))
    homerseklet = float(input("Hőmérséklet (C°): "))
    csapadek = float(input("Csapadék (mm): "))
    
    # Fagy automatikus beállítása
    fagy = 1 if homerseklet <= 0 else 0
    
    return [ido, auto_muszaki_allapota, KSS, vezetesi_tapasztalat, RQI,
            forgalom_surusege, latasi_viszonyok, homerseklet, csapadek, fagy]


clear_console()
print("------------ Baleseti veszély előrejelző  ------------")
# Adatok bekérése
user_input = get_user_input()

# Adatok normalizálása
# Az előző adatok normalizálása tanításkor ugyanúgy szükséges
# Betöltünk egy példa adatot az adatok skálázásához
example_data = pd.read_csv('baleseti_veszely_data.csv')
x_example = example_data.drop(columns=["baleseti_veszely_merteke"])
scaler.fit(x_example)

# A felhasználó által megadott adat normalizálása
user_input_scaled = scaler.transform([user_input])

# Előrejelzés
prediction = model.predict(user_input_scaled)
predicted_class = np.argmax(prediction)  # Legvalószínűbb osztály

print(f"\n\nA becsült baleseti veszély mértéke: {predicted_class + 1}")
