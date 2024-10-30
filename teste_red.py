# Victor Henrique Fernandes Silva
# 2120668

# Fase Red: Aqui começamos escrevendo os testes antes de implementar a função.

import unittest  # Importa a biblioteca de testes unitários do Python.

def calcular_media(nota1, nota2, nota3):
    pass  # Placeholder para a implementação da função. Aqui não há código ainda.

class TestCalculoMedia(unittest.TestCase):  # Define uma classe de teste que herda de unittest.TestCase.
    
    def test_media_calculo(self):  # Método de teste para verificar o cálculo da média.
        self.assertAlmostEqual(calcular_media(7, 8, 9), 8.0)  # Verifica se a média de 7, 8 e 9 é aproximadamente 8.0.

    def test_notas_zero(self):  # Método de teste para o caso onde todas as notas são zero.
        self.assertAlmostEqual(calcular_media(0, 0, 0), 0.0)  # Verifica se a média de 0, 0 e 0 é 0.0.

    def test_notas_maximas(self):  # Método de teste para o caso onde todas as notas são 10.
        self.assertAlmostEqual(calcular_media(10, 10, 10), 10.0)  # Verifica se a média de 10, 10 e 10 é 10.0.

    def test_notas_decimais(self):  # Método de teste para verificar a média com notas decimais.
        self.assertAlmostEqual(calcular_media(7.5, 8.0, 9.0), 8.166666666666666)  # Verifica se a média é correta.

if __name__ == '__main__':  # Verifica se o script está sendo executado diretamente.
    unittest.main()  # Executa todos os testes definidos na classe TestCalculoMedia.
