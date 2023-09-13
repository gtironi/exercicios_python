import sys
import os

x = 10
z = 1

try:
    resultado = x/z
    print(resultado)
    
except Exception as e:
    line = format(sys.exc_info()[-1].tb_lineno) #Vê a linha com erro
    line = format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e #Vê varias coisas
    
arquivo = open(os.path.basename(__file__)).read()
print(arquivo)

f'''
This script has an error, I will give you the script and the traceback, please find the error and answer me just the file fixed, with no other word:
{open(os.path.basename(__file__)).read()} 
'''