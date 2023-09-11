import pandas as pd

def med_mean(serie):
    mean = serie.mean()
    dp = serie.std()
    return (mean, dp)

def count_values(serie):
    frequencia = serie.value_counts()
    return frequencia

def pos_element_mul_5(serie):
    posicao = serie[serie%5 == 0]
    return posicao

def pos_serie_serie(serie_elementos, serie_achar):
    posicao = pd.Series({})
    for elemento in serie_elementos:
        pos_elemento = serie_achar.loc[serie_achar == elemento]
        posicao = pd.concat([posicao, pos_elemento])
    return posicao

def freq_max(serie):
    max_freq = serie.mode()[0]
    print(max_freq)
    serie_final = serie.where(serie == max_freq, "Desconsiderar")
    return serie_final