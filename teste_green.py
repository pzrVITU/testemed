# Victor Henrique Fernandes Silva
# 2120668

# Fase Green: Nesta fase, implementamos a função para passar nos testes.

import unittest  # Importa a biblioteca de testes unitários do Python.

def calcular_media(nota1, nota2, nota3):
    pass  # Placeholder para a implementação; a função será implementada a seguir.

def calcular_media(nota1, nota2, nota3):
    # Implementação da função que calcula a média de três notas.
    return (nota1 + nota2 + nota3) / 3  # Retorna a média aritmética das três notas.

class TestCalculoMedia(unittest.TestCase):  # Define uma classe de teste que herda de unittest.TestCase.
    
    def test_media_calculo(self):  # Método de teste para verificar o cálculo da média.
        # Verifica se a média de 7, 8 e 9 é aproximadamente 8.0.
        self.assertAlmostEqual(calcular_media(7, 8, 9), 8.0)  

    def test_notas_zero(self):  # Método de teste para o caso onde todas as notas são zero.
        # Verifica se a média de 0, 0 e 0 é 0.0.
        self.assertAlmostEqual(calcular_media(0, 0, 0), 0.0)  

    def test_notas_maximas(self):  # Método de teste para o caso onde todas as notas são 10.
        # Verifica se a média de 10, 10 e 10 é 10.0.
        self.assertAlmostEqual(calcular_media(10, 10, 10), 10.0)  

    def test_notas_decimais(self):  # Método de teste para verificar a média com notas decimais.
        # Verifica se a média de 7.5, 8.0 e 9.0 é aproximadamente 8.1667.
        self.assertAlmostEqual(calcular_media(7.5, 8.0, 9.0), 8.166666666666666)  

if __name__ == '__main__':  # Verifica se o script está sendo executado diretamente.
    unittest.main()  # Executa todos os testes definidos na classe TestCalculoMedia.
