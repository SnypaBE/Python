'''
montar dieta
input => homem ou mulher

calcular tmb:
input => homem > 66 + (13,8*peso em kilos) + (5*altura em cm) - (6,8 - idade) 
input => mulher > 655 + (9,6* peso em kg) + (1,8* altura em cm) - (4,7* idade em anos) 

taxa de atividade:
sedentario = 1.2
levemente ativo = 1.375
moderado ativo = 1.55
alto ativo = 1.725
extremamente ativo = 1.9

montar dieta:
1.3* peso = proteina
40% do que sobrar = gordura
60% do que sobrar = carboidrato

resultado:
input => quantas refeições por dia? [4,5,6]

macros / tanto de refeições
'''

nome = str(input('Olá, Digite seu nome: '))
print (f'Olá {nome}, vamos montar sua dieta para perda de peso!\nPara calcular sua taxa de matabolismo basal responda o questionário.')
peso = int(input(f'{nome} Digite seu peso em Kg:\n'))
while (peso < 30) or (peso > 400):
    peso = int(input('Valor inválido.\nDigite novamente:\n'))
altura = int(input(f'{nome} Digite sua altura em cm:\n'))
while (altura < 130) or (altura > 250):
    altura = int(input('Valor inválido.\nDigite novamente:\n'))
idade = int(input(f'{nome} Digite sua idade:\n'))
while (idade < 15) or (idade > 150):
    if idade <15:
        idade = int(input('Idade nao pode ser menor que 15 anos.\nDigite novamente:\n'))
    elif idade >150:
        idade = int(input('Idade nao pode ser maior que 150 anos.\nDigite novamente:\n'))
    else:
        idade = int(input('Valor inválido.\nDigite novamente:\n'))

Mtmb = 66+(13.8*peso)+(5*altura)-(6.8-idade)
Ftmb = 655+(9.6*peso)+(1.8*altura)-(4.7-idade)

sexo = (input('\nMasculino\nFeminino\nDigite seu genero:\n'))
while (sexo != 'masculino') and (sexo != 'feminino'):
    sexo = (input("Genero inválido.\nDigite novamente:\n"))
atividade = int(input('\n[1]Sedentário\n[2]Ativo\n[3]Pouco ativo\n[4]Muito ativo\n[5]Extremamente ativo:\nQual seu nivel de atividade?\n'))
while (atividade <1) and (atividade >5):
    atividade = int(input('Essa opção não existe\nEscolha novamente:\n'))
if (atividade == 1) and (sexo == "masculino"):
    print('sua taxa de metabolismo basal do seu dia a dia é de', Ftmb*1.2,'kcal')
elif (atividade == 2) and (sexo == "masculino"):
    print('sua taxa de metabolismo basal do seu dia a dia é de', Ftmb*1.37,'kcal')
elif (atividade == 3) and (sexo == "masculino"):
    print('sua taxa de metabolismo basal do seu dia a dia é de', Ftmb*1.55,'kcal')
elif (atividade == 4) and (sexo == "masculino"):
    print('sua taxa de metabolismo basal do seu dia a dia é de', Ftmb*1.72,'kcal')
elif (atividade == 5) and (sexo == "masculino"):
    print('sua taxa de metabolismo basal do seu dia a dia é de', Ftmb*1.9,'kcal')
elif (atividade == 1) and (sexo == "feminino"):
    print('sua taxa de metabolismo basal do seu dia a dia é de', Ftmb*1.2,'kcal')
elif (atividade == 2) and (sexo == "feminino"):
    print('sua taxa de metabolismo basal do seu dia a dia é de', Ftmb*1.37,'kcal')
elif (atividade == 3) and (sexo == "feminino"):
    print('sua taxa de metabolismo basal do seu dia a dia é de', Ftmb*1.55,'kcal')
elif (atividade == 4) and (sexo == "feminino"):
    print('sua taxa de metabolismo basal do seu dia a dia é de', Ftmb*1.72,'kcal')
elif (atividade == 5) and (sexo == "feminino"):
    print('sua taxa de metabolismo basal do seu dia a dia é de', Ftmb*1.9,'kcal')
else:
    print('Ocorreu um erro!')






#print(f'{nome}, {peso}kg, {altura}cm de altura, {idade} anos, {sexo} e Seu nivel de atividade é: {atividade}')




