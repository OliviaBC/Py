'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista de
notas. Escreva uma função chamada 'excluir_nota' que recebe como argumentos de
entrada o dicionário e o nome de um aluno. A função deve excluir a primeira
nota desse aluno e retornar o dicionário com as alterações realizadas.
Se o aluno não existir no dicionário, deve retornar o dicionário sem alterações.
'''
def excluir_nota(alunos, nome):
  if nome in alunos:
    alunos.pop(nome, 2)
    return alunos
  else:
    return alunos

alunos = {'Augusto': [4.5, 7.0, 6.0, 3.0], 
          'Denise': [9.0, 8.5], 
          'Ana Paula': [3.5, 1.0, 6.5],
          'Marcelo': [9.0, 10.0, 7.0, 7.0]}
resultado = excluir_nota(alunos, 'Ana Paula')        	
print(resultado)           