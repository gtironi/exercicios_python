AUTORES = ['Gustavo Tironi', 'Gustavo Tironi']

def questao_1(path):
    df = le_csv(path)
    return len(df.index)

def questao_2(path):
    df = le_csv(path)
    pass

def questao_3(path):
    df = le_csv(path)
    pass


def questao_4(path):
    df = le_csv(path)
    pass

def questao_5(path):
    df = le_csv(path)
    pass

def questao_6(path):
    df = le_csv(path)
    pass

def questao_7(path):
    df = le_csv(path)
    pass

def questao_8(path):
    df = le_csv(path)
    pass

def questao_9(path):
    df = le_csv(path)
    pass

def questao_10(path):
    df = le_csv(path)
    pass

def le_csv(path):
    df = pd.read_csv(path)
    return df