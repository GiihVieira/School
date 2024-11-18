import re
from validate_docbr import CPF

def cpf_invalido(num_cpf):
    cpf = CPF()
    cpf_valido = cpf.validate(num_cpf)
    return not cpf_valido

def nome_invalido(nome):
    return not nome.isalpha()

def celular_invalido(celular):
    # Model -> 99 99999-9999
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}' # [0-9] defines the range of numbers, and {2} defines how many times those numbers repeat.
    result = re.findall(modelo, celular) # The 're' module in Python allows operations with regular expressions.
    return not result
