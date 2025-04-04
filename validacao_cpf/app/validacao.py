import re

def validar_cpf(cpf: str) -> bool:
    """
    Valida um CPF brasileiro.

    :param cpf: CPF como string (somente números ou no formato xxx.xxx.xxx-xx)
    :return: True se for válido, False caso contrário
    """
    # Verifica xxx.xxx.xxx-xx
    if not re.fullmatch(r'\d{11}|\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
        return False

    # Remove os caracteres
    cpf = re.sub(r'\D', '', cpf)

   
    if cpf == cpf[0] * 11:
        return False

    
    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma1 * 10) % 11
    digito1 = 0 if digito1 >= 10 else digito1

    
    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma2 * 10) % 11
    digito2 = 0 if digito2 >= 10 else digito2

    return int(cpf[9]) == digito1 and int(cpf[10]) == digito2
