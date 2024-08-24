Az Ai tesztelésére nyissa meg, a "baleseti_ai.py" filet. Ott adja meg a kért adatokat, és várja a megítélt veszély értékét. Elötte bizonyosodjon meg, hogy telepítve vannak a szükséges könyvtárak, illetve a python.








A fájlok magyarázata:

baleseti_veszely_data.csv - Táblázat formályában tárolja a betanításhoz szükséges adatokat

baleseti ai adatgyujto app.exe - Egy felület, amely az adatok gyűjtésére szolgál. A .csv fájlt tölti fel.

baleseti_ai_tanito.py - Egy program, mely a rendelkezésre álló adatok alapján létrehozza a model struktúráját, és betanítja a modelt. Ezt egy .keras file-ban menti le.

baleseti_elorejelzo.keras - A betanított modellt tartalmazza.

baleseti_ai.py - Betölti a modelt, és azt használva tesztelhetjük a kész ai-t. Bekér adatokat, és a bekért adatok alapján jósol egy baleseti veszély mértéket.

baleseti_veszely_elorejelzo.pdf - Tartalmazza a paraméterek magyarázatát, hogy miért azokat választottam, és hogy milyen továbbfejlesztési lehetőségek vannak.
