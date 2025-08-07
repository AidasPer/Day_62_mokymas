# Sukurti naują projektą mokymas
#
# Projekto kataloge sukurti katalogą models
#
# Kataloge models sukurti failą kursas.py
#
# Faile kursas.py sukurti objekto klasę Kursas, kuri turėtų savybes pavadinimas, destytojas, trukme, taip pat metodą destyti(), kuris spausdintų „Vyksta mokymas!“
#
# Kataloge models sukurti antrą failą python_kursas.py
#
# Faile python_kursas.py sukurti objekto klasę PythonKursas, kuri paveldėtų viską iš klasės Kursas, bei perrašytų metodą destyti() taip, kad jis spausdintų „Vyksta programavimas!“
#
# Pagrindiniame projekto kataloge sukurti failą main.py
#
# Faile main.py importuoti Kursas modulį (failą)
#
# Faile main.py importuoti PythonKursas modulį (failą)
#
# Faile main.py inicijuoti Kursas objektą su norimomis savybėmis
#
# Faile main.py inicijuoti PythonKursas objektą su norimomis savybėmis
#
# Paleisti abiejų objektų metodą destyti()


from models.kursas import Kursas
from models.python_kursas import PythonKursas

kursas1 = Kursas("Matematika", "Saule", 150)
kursas2 = PythonKursas("Programavimas", "Johanas", 60)

print(kursas1)
print(kursas2)