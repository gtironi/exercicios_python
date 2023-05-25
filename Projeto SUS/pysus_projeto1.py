from pysus.online_data import SINAN
from pysus.preprocessing.decoders import decodifica_idade_SINAN
import pandas as pd

# path = SINAN.download('Leptospirose', 2018)

# dataframe = pd.read_parquet(path)
# dataframe['DT_NOTIFIC'] = pd.to_datetime(dataframe['DT_NOTIFIC'])
# dataframe.to_csv('Leptospirose.csv', index=False)
dataframe_lepto_2020 = pd.read_csv('Leptospirose.csv')
dataframe_lepto_2020['DT_NOTIFIC'] = pd.to_datetime(dataframe_lepto_2020['DT_NOTIFIC'])
dataframe_lepto_2020.set_index('DT_NOTIFIC', inplace = True)
print(dataframe_lepto_2020)

# Ano

# print(len(dataframe_lepto_2020.index))

# Municipio

agrupado_por_municipio = dataframe_lepto_2020.groupby('ID_MUNICIP').count().sort_values('TP_NOT', ascending=False)
# print(agrupado_por_municipio['TP_NOT'])

# Estado

agrupado_por_estado = dataframe_lepto_2020.groupby('SG_UF').count().sort_values('TP_NOT', ascending=False)
# print(agrupado_por_estado['TP_NOT'])

# Mês

agrupado_por_mês = dataframe_lepto_2020.resample('M').count()
print(agrupado_por_mês['TP_NOT'])

# Mês