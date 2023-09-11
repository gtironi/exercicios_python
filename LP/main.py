import exercicio_pandas as epd
import pandas as pd

serie = pd.Series([1,2,3,4,5,6,7,8,9,10,6,7,8,9,10,10])
serie_5 =  pd.Series([1,10,6])

# print(epd.med_mean(serie))

print(epd.count_values(serie))

# print(epd.pos_element_mul_5(serie_5))

# print(epd.pos_serie_serie(serie_5, serie))

# print(epd.freq_max(serie))
