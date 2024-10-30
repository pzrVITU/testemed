# Victor Henrique Fernandes Silva
# 2120668

# Fase Refactor: Nesta fase, melhoramos o código e adicionamos validações.

import unittest  # Importa a biblioteca de testes unitários do Python.

def calcular_media(nota1, nota2, nota3):
    # Verifica se as notas estão dentro do intervalo permitido
    for nota in [nota1, nota2, nota3]:  # Itera sobre cada nota fornecida.
        if nota < 0 or nota > 10:  # Verifica se a nota está fora do intervalo de 0 a 10.
            raise ValueError("As notas devem estar entre 0 e 10.")  # Lança uma exceção se a nota for inválida.
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

    def test_notas_invalidas(self):  # Método de teste para verificar a validação de notas inválidas.
        with self.assertRaises(ValueError):  # Verifica se a exceção ValueError é lançada.
            calcular_media(11, 5, 6)  # Testa com uma nota maior que 10.
        with self.assertRaises(ValueError):  # Verifica novamente se a exceção é lançada.
            calcular_media(-1, 5, 6)  # Testa com uma nota menor que 0.

if __name__ == '__main__':  # Verifica se o script está sendo executado diretamente.
    unittest.main()  # Executa todos os testes definidos na classe TestCalculoMedia.
