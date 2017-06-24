"""
arq = open('aula_arquivos.txt','w')

arq.write('Machine Learning')
arq.write('\napredendo python')

texto = '''
Apredendo python
	machine learning
	python é legal
'''

arq.write(texto)
arq.close()
"""

with open('dataset.txt','r') as arq:
	conteudo = arq.read().splitlines()
	print(conteudo[0])
