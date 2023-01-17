'''
montar dieta
input => homem ou mulher

calcular tmb:
homem > 66 + (13,8*peso em kilos) + (5*altura em cm) - (6,8 - idade) 
mulher > 655 + (9,6* peso em kg) + (1,8* altura em cm) - (4,7* idade em anos) 

taxa de atividade:
sedentario = 1.2
levemente ativo = 1.375
moderado ativo = 1.55
alto ativo = 1.725
extremamente ativo = 1.9
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
Ftmb1 = Ftmb*1.2
Ftmb2 = Ftmb*1.37
Ftmb3 = Ftmb*1.55
Ftmb4 = Ftmb*1.72
Ftmb5 = Ftmb*1.9
Mtmb1 = Mtmb*1.2
Mtmb2 = Mtmb*1.37
Mtmb3 = Mtmb*1.55
Mtmb4 = Mtmb*1.72
Mtmb5 = Mtmb*1.9

sexo = (input('\nMasculino\nFeminino\nDigite seu genero:\n'))
while (sexo != 'masculino') and (sexo != 'feminino'):
    sexo = (input("Genero inválido.\nDigite novamente:\n"))
atividade = int(input('\n[1]Sedentário\n[2]Ativo\n[3]Pouco ativo\n[4]Muito ativo\n[5]Extremamente ativo:\nQual seu nivel de atividade?\n'))
while (atividade <1) and (atividade >5):
    atividade = int(input('Essa opção não existe\nEscolha novamente:\n'))
if (atividade == 1) and (sexo == "masculino"):
    print(f'sua taxa de metabolismo basal do seu dia a dia é de {Mtmb1:.2f}kcal\n')
    dietam = int(input('Quantas refeições por dia será sua dieta?\n'))
    while (dietam <4) or (dietam >6):
        dietam = int(input('Valor tem que ser de 4 a 6 refeições por dia.\nDigite novamente:\n'))
    if dietam == 4:
        result1 = (Mtmb1*0.85) #90% do tmb em calorias
        prot1 = ((peso*1.3)*4)/dietam       #((peso*1.3 = gramas de proteina/dia) |*4 = tranformar em kcal)= valor da proteina em calorias | /dietam = calorias por refeição
        carbo1 = ((Mtmb1*0.85-prot1*4)*0.6)/dietam 
        gord1 = ((Mtmb1*0.85-prot1*4)*0.4)/dietam
        frango = (prot1/4)*3.7
        ovo = (prot1/4)*0.34
        patinho = (prot1/4*3.44)

        print(f'''Sua dieta é {result1/dietam:.2f}kcal por refeição.
{prot1:.2f}kcal de proteina, {carbo1:.2f}kcal de carboidratos e {gord1:.2f}kcal de gorduras.
Escolha uma fonte de Protreina, uma fonte de Carboidratos e uma fonte de Gordura:
Proteina:                       
[1]{frango:.0f}g de frango                      
[2]{ovo:.0f} claras de ovos                          
[3]{patinho:.0f}g de patinho        
        
Carboidrato:       
[1]{carbo1:.0f}
[2]{carbo1:.0f}        
[3]{carbo1:.0f}        
        
Gordura:
[1]{gord1:.2f}
[2]{gord1:.2f}

        ''')
    elif dietam == 5:
        print('sua dieta é Mtmb1/5')
    elif dietam == 6:
        print('sua dieta é Mtmb1/5')

elif (atividade == 2) and (sexo == "masculino"):
    print(f'sua taxa de metabolismo basal do seu dia a dia é de {Mtmb2:.2f}kcal')
elif (atividade == 3) and (sexo == "masculino"):
    print(f'sua taxa de metabolismo basal do seu dia a dia é de {Mtmb3:.2f}kcal')
elif (atividade == 4) and (sexo == "masculino"):
    print(f'sua taxa de metabolismo basal do seu dia a dia é de {Mtmb4:.2f}kcal')
elif (atividade == 5) and (sexo == "masculino"):
    print(f'sua taxa de metabolismo basal do seu dia a dia é de {Mtmb5:.2f}kcal')
elif (atividade == 1) and (sexo == "feminino"):
    print(f'sua taxa de metabolismo basal do seu dia a dia é de {Ftmb1:.2f}kcal')
elif (atividade == 2) and (sexo == "feminino"):
    print(f'sua taxa de metabolismo basal do seu dia a dia é de {Ftmb2:.2f}kcal')
elif (atividade == 3) and (sexo == "feminino"):
    print(f'sua taxa de metabolismo basal do seu dia a dia é de {Ftmb3:.2f}kcal')
elif (atividade == 4) and (sexo == "feminino"):
    print(f'sua taxa de metabolismo basal do seu dia a dia é de {Ftmb4:.2f}kcal')
elif (atividade == 5) and (sexo == "feminino"):
    print(f'sua taxa de metabolismo basal do seu dia a dia é de {Ftmb5:.2f}kcal')
else:
    print('Ops, ocorreu um erro!')
'''
montar dieta:
1.3* peso = proteina
40% do que sobrar = gordura
60% do que sobrar = carboidrato

resultado:
input => quantas refeições por dia? [4,5,6]

macros / tanto de refeições
'''





