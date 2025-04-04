import re

def validar_cpf(cpf: str) -> bool:
    """
    Valida um CPF brasileiro.

    :param cpf: CPF como string (somente números ou no formato xxx.xxx.xxx-xx)
    :return: True se for válido, False caso contrário
    """
    # Remove caracteres não numéricos
    cpf = re.sub(r'\D', '', cpf)

    # Verifica se tem 11 dígitos e não é uma sequência repetida
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # Cálculo do primeiro dígito verificador
    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma1 * 10 % 11) % 10

    # Cálculo do segundo dígito verificador
    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma2 * 10 % 11) % 10

    # Valida os dígitos verificadores
    return int(cpf[9]) == digito1 and int(cpf[10]) == digito2
