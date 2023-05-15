from pysus.online_data import SINAN
import pandas as pd

lista_doencas = SINAN.list_diseases()

anos_dispo_leptospirose = SINAN.get_available_years('Leptospirose')

df = SINAN.download('Leptospirose', 2021)

df.to_csv('leptospirose.csv', index=False)