import sys
import os
import unittest
from app.validacao import validar_cpf


class TestValidarCPF(unittest.TestCase):
    def test_cpfs_validos(self):
        self.assertTrue(validar_cpf("529.982.247-25"))  
        self.assertTrue(validar_cpf("170.928.730-61")) 
        self.assertTrue(validar_cpf("98765432100"))     

    def test_cpfs_invalidos(self):
        self.assertFalse(validar_cpf("111.111.111-11"))  
        self.assertFalse(validar_cpf("123.456.789-00"))  
        self.assertFalse(validar_cpf("00000000000"))     

    def test_formatos_invalidos(self):
        self.assertFalse(validar_cpf("12345678"))        
        self.assertFalse(validar_cpf("123456789098"))   
        self.assertFalse(validar_cpf("abc.def.ghi-jk")) 

    def test_com_caracteres_aleatorios(self):
        self.assertFalse(validar_cpf("529-982*247-25"))  

if __name__ == "__main__":
    unittest.main()
