#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import os

arquivo = open('file.db', 'wb')
for i in range(10):
	pickle.dump(i, arquivo)
arquivo.close()

print ("Arquivo criando com sucesso")

db = {}
def exbir_menu():
	os.system('cls')
	print('Existem(m): ' + str(len(db)) + ' candidatos registrados!\n\n')
	print('1 - Incluir candidato')
	print('2 - Listar Candidatos')
	print('3 - Modificar candidato')
	print('4 - Excluir candidato')
	print('5 - Votos por Regiao')
	print('6 - Votos por Candidato')
	print('7 - Sair')
	return int(input(""))


def existe_registro(codigo):
	duplicated = False
	if codigo in db.keys():
		duplicated = True

	return duplicated


def inserirCandidato ():
	candidato = {}
	codigo = input('Digite o codigo do candidato\n')
	if existe_registro(codigo):
		print('Já existe um candidato cadastrado com este codigo')
		frase = input('Pressione para volta ao menu\n')
		__principal__()
	else:
		candidato['cod_candidato'] = codigo
		candidato['nome'] = input('Digite o nome do candidato\n')
		candidato['cargo'] = input('Digito o cargo do candidato\n')
		candidato['regiao'] = input('Digite a região do candidato\n')
		candidato['num_votos'] = int(input('Digite o numero de votos\n'))
		db[codigo] = candidato
		__principal__()



def modificarCandidato():
	candidato = {}
	codigo = input('Digite o codigo do candidato\n')
	if existe_registro(codigo):
		candidato['cod_candidato'] = codigo
		candidato['nome'] = input('Digite o nome do candidato\n')
		candidato['cargo'] = input('Digito o cargo do candidato\n')
		candidato['regiao'] = input('Digite a região do candidato\n')
		candidato['num_votos'] = int(input('Digite o numero de votos\n'))
		db[codigo] = candidato
		__principal__()
	else:
		print('Candidato não encontrado')
		trash = input('pressione para voltar ao menu\n')
		__principal__()

def mostrarVotosCandidatos(codigo):
	print('Nome: ' + db[codigo]['nome'])
	print('Número de votos: ' + str(db[codigo]['num_votos']))

def votosPorRegiao():
	regioes = dict()
	for candidato in db.values():
		regioes[candidato['regiao']] = regioes.get(candidato['regiao'],0) + candidato['num_votos']
	print('Total de votos por regiao:' + str(regioes))
	input('Pressione para voltar ao menu principal!')
	__principal__()

def listarTodosCandidatos():
    if len(db) > 0:
        for codigo in db.keys():
            mostrar(codigo)
            print('-' * 10)
        trash = input('pressione para voltar ao menu\n')
        __principal__()
    else:
        print('Não há registros para serem exibidos')
        trash = input('pressione para voltar ao menu\n')
        __principal__()

def votosPorCandidato():
	if len(db) > 0:
		for codigo in db.keys():
			mostrarVotosCandidatos(codigo)
			print('-'*10)
		frase = input('pressione para voltar ao menu\n')
		__principal__()
	else:
		print('Não há registros para serem exibidos')
		frase = input('pressione para voltar ao menu\n')
		__principal__()



def apagarCandidato():
	codigo = input('Digite o código da peça\n')

	if existe_registro(codigo):
		del (db[codigo])
		print('Registro apagado com sucesso')
		trash = input('pressione para voltar ao menu\n')
		__principal__()
	else:
		print('Registro não encontrado')
		trash = input('pressione para voltar ao menu\n')
		__principal__()
def mostrar(codigo):
	print('Código: ' + db[codigo]['cod_candidato'])
	print('Nome: ' + db[codigo]['nome'])
	print('Cargo: ' + db[codigo]['cargo'])
	print('Região: ' + db[codigo]['regiao'])
	print('Número de votos: ' + str(db[codigo]['num_votos']))

def __principal__():
	option = exbir_menu()
	if(option == 1):
		inserirCandidato()
	elif(option == 2):
		listarTodosCandidatos()
	elif(option == 3):
		modificarCandidato()
	elif(option == 4):
		apagarCandidato()
	elif(option == 5):
		votosPorRegiao()
	elif(option == 6):
		votosPorCandidato()
	elif(option == 7 ):
		print('Saindo ...')
		exit()

__principal__()
