Resumo dos testes: 

teste_red: 


Importação: O módulo unittest é importado para permitir a criação e execução de testes unitários.
Placeholder: A função calcular_media ainda não foi implementada, servindo como um espaço reservado.
Classe de Teste: Herda de unittest.TestCase e contém métodos que testam a funcionalidade da média.
Métodos de Teste: Cada método de teste utiliza assertAlmostEqual para comparar o resultado esperado com o resultado da função.
Execução do Script: Permite que os testes sejam executados automaticamente se o script for rodado diretamente.

teste_green:

Importação: Importa o módulo unittest para permitir a criação de testes.
Função Placeholder: A primeira definição da função calcular_media é um espaço reservado que será substituído pela implementação real.
Implementação da Função: A segunda definição da função realmente calcula a média das notas.
Classe de Teste: A classe TestCalculoMedia contém métodos que testam a função calcular_media.
Métodos de Teste: Cada método usa assertAlmostEqual para comparar o resultado calculado com o esperado.
Execução do Script: Permite que os testes sejam executados automaticamente quando o script é executado diretamente.

teste_refactor:


Importação: Importa a biblioteca unittest para permitir a criação de testes.

Função calcular_media:
Adiciona uma verificação para garantir que as notas estejam entre 0 e 10.
Lança uma exceção ValueError se qualquer nota estiver fora desse intervalo.
Retorna a média das três notas.

Classe de Teste TestCalculoMedia:
Contém métodos que testam a funcionalidade da média e a validação de notas.
Cada método de teste usa assertAlmostEqual para verificar se o resultado da função está correto.
Teste de Notas Inválidas:

Verifica se a função lança uma exceção quando notas inválidas são fornecidas.
