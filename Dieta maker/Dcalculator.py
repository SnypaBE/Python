
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
Mtmb1 = Mtmb*1.2
Mtmb2 = Mtmb*1.37
Mtmb3 = Mtmb*1.55
Mtmb4 = Mtmb*1.72
Mresult1 = (Mtmb1*0.85)    #| M = masculino| result = 85% do tmb | 1 = atividade
Mresult2 = (Mtmb2*0.85)
Mresult3 = (Mtmb3*0.85)
Mresult4 = (Mtmb4*0.85)
Fresult1 = (Ftmb1*0.85)     #| F = feminino | result = 85% do tmb | 1 = atividade
Fresult2 = (Ftmb2*0.85)
Fresult3 = (Ftmb3*0.85)
Fresult4 = (Ftmb4*0.85)
ref = int(input('Quantas refeições por dia será sua dieta?\n'))
prot = ((peso*1.3)*4)/ref       #((peso*1.3 = gramas de proteina/dia) |*4 = tranformar em kcal)= valor da proteina em calorias | /dietam = calorias por refeição
frango = (prot/4)*3.7
ovo = (prot/4)*0.34
patinho = (prot/4)*3.44



sexo = (input('\nMasculino\nFeminino\nDigite seu genero:\n'))
while (sexo != 'masculino') and (sexo != 'feminino'):
    sexo = (input("Genero inválido.\nDigite novamente:\n"))

atividade = int(input('\n[1]Sedentário\n[2]Ativo\n[3]Pouco ativo\n[4]Muito ativo\nQual seu nivel de atividade?\n'))
while (atividade <1) and (atividade >4):
    atividade = int(input('Essa opção não existe\nEscolha novamente:\n'))

if (atividade == 1) and (sexo == "masculino"):
    print(f'sua taxa de metabolismo basal do seu dia a dia é de {Mtmb1:.2f}kcal\n')         
    carbo1 = ((Mresult1-prot*4)*0.6)/ref 
    gord1 = ((Mresult1-prot*4)*0.4)/ref
    arroz = (carbo1/4)*3.57
    batata = (carbo1/4)*5.43
    mandioca = (carbo1/4)*2.63
    azeite = int((gord1/9)*0.08)
    castanha = (gord1/9)*1.51

    while (ref <4) or (ref >6):
        ref = int(input('Valor tem que ser de 4 a 6 refeições por dia.\nDigite novamente:\n'))
        
    if ref == 4:        
        print(f'''Sua dieta é de {Mresult1/ref:.2f}kcal por refeição:
{prot:.2f}kcal de proteina,
{carbo1:.2f}kcal de carboidratos e
{gord1:.2f}kcal de gorduras.

Escolha uma das 3 opções de Protreina, uma das 3 de Carboidratos e uma das 2 de Gordura para cada refeição:

Proteina:
[1]-{frango:.0f}g de frango ou
[2]-{ovo:.0f} claras de ovos ou
[3]-{patinho:.0f}g de patinho.
        
Carboidrato:
[1]-{arroz:.0f}g de arroz branco ou
[2]-{batata:.0f}g de batata doce cozida ou
[3]-{mandioca:.0f}g de mandioca.
        
Gordura:
[1]-{azeite:.0f} colhere(s) de azeite de oliva extravirgem ou
[2]-{castanha:.0f}g de castanha do Pará.
''')
    elif ref == 5:
        print(f'''Sua dieta é {Mresult1/ref:.2f}kcal por refeição.

{prot:.2f}kcal de proteina, 
{carbo1:.2f}kcal de carboidratos e 
{gord1:.2f}kcal de gorduras.

Escolha uma das 3 opções de Protreina, uma das 3 de Carboidratos e uma das 2 de Gordura para cada refeição:

Proteina:
[1]{frango:.0f}g de frango ou
[2]{ovo:.0f} claras de ovos ou
[3]{patinho:.0f}g de patinho.
        
Carboidrato:
[1]{arroz:.0f}g de arroz branco ou
[2]{batata:.0f}g de batata doce cozida ou
[3]{mandioca:.0f}g de mandioca.
        
Gordura:
[1]{azeite:.0f} colhere(s) de azeite de oliva extravirgem ou
[2]{castanha:.0f}g de castanha do Pará.
''')
    elif ref == 6:
        print(f'''Sua dieta é {Mresult1/ref:.2f}kcal por refeição.

{prot:.2f}kcal de proteina, 
{carbo1:.2f}kcal de carboidratos e 
{gord1:.2f}kcal de gorduras.

Escolha uma das 3 opções de Protreina, uma das 3 de Carboidratos e uma das 2 de Gordura para cada refeição:

Proteina:
[1]{frango:.0f}g de frango ou
[2]{ovo:.0f} claras de ovos ou
[3]{patinho:.0f}g de patinho.
        
Carboidrato:
[1]{arroz:.0f}g de arroz branco ou
[2]{batata:.0f}g de batata doce cozida ou
[3]{mandioca:.0f}g de mandioca.
        
Gordura:
[1]{azeite:.0f} colhere(s) de azeite de oliva extravirgem ou
[2]{castanha:.0f}g de castanha do Pará.
''')

elif (atividade == 2) and (sexo == "masculino"):
    print(f'sua taxa de metabolismo basal do seu dia a dia é de {Mtmb2:.2f}kcal')
    carbo2 = ((Mresult2-prot*4)*0.6)/ref 
    gord2 = ((Mresult2-prot*4)*0.4)/ref
    arroz = (carbo2/4)*3.57
    batata = (carbo2/4)*5.43
    mandioca = (carbo2/4)*2.63
    azeite = int((gord2/9)*0.08)
    castanha = (gord2/9)*1.51

    while (ref <4) or (ref >6):
        ref = int(input('Valor tem que ser de 4 a 6 refeições por dia.\nDigite novamente:\n'))
        
    if ref == 4:        
        print(f'''Sua dieta é de {Mresult2/ref:.2f}kcal por refeição:
{prot:.2f}kcal de proteina,
{carbo2:.2f}kcal de carboidratos e
{gord2:.2f}kcal de gorduras.

Escolha uma das 3 opções de Protreina, uma das 3 de Carboidratos e uma das 2 de Gordura para cada refeição:

Proteina:
[1]-{frango:.0f}g de frango ou
[2]-{ovo:.0f} claras de ovos ou
[3]-{patinho:.0f}g de patinho.
        
Carboidrato:
[1]-{arroz:.0f}g de arroz branco ou
[2]-{batata:.0f}g de batata doce cozida ou
[3]-{mandioca:.0f}g de mandioca.
        
Gordura:
[1]-{azeite:.0f} colhere(s) de azeite de oliva extravirgem ou
[2]-{castanha:.0f}g de castanha do Pará.
''')
    elif ref == 5:
        print(f'''Sua dieta é {Mresult2/ref:.2f}kcal por refeição.

{prot:.2f}kcal de proteina, 
{carbo2:.2f}kcal de carboidratos e 
{gord2:.2f}kcal de gorduras.

Escolha uma das 3 opções de Protreina, uma das 3 de Carboidratos e uma das 2 de Gordura para cada refeição:

Proteina:
[1]{frango:.0f}g de frango ou
[2]{ovo:.0f} claras de ovos ou
[3]{patinho:.0f}g de patinho.
        
Carboidrato:
[1]{arroz:.0f}g de arroz branco ou
[2]{batata:.0f}g de batata doce cozida ou
[3]{mandioca:.0f}g de mandioca.
        
Gordura:
[1]{azeite:.0f} colhere(s) de azeite de oliva extravirgem ou
[2]{castanha:.0f}g de castanha do Pará.
''')
    elif ref == 6:
        print(f'''Sua dieta é {Mresult2/ref:.2f}kcal por refeição.

{prot:.2f}kcal de proteina,
{carbo2:.2f}kcal de carboidratos e 
{gord2:.2f}kcal de gorduras.

Escolha uma das 3 opções de Protreina, uma das 3 de Carboidratos e uma das 2 de Gordura para cada refeição:

Proteina:
[1]{frango:.0f}g de frango ou
[2]{ovo:.0f} claras de ovos ou
[3]{patinho:.0f}g de patinho.
        
Carboidrato:
[1]{arroz:.0f}g de arroz branco ou
[2]{batata:.0f}g de batata doce cozida ou
[3]{mandioca:.0f}g de mandioca.
        
Gordura:
[1]{azeite:.0f} colhere(s) de azeite de oliva extravirgem ou
[2]{castanha:.0f}g de castanha do Pará.
''')

elif (atividade == 3) and (sexo == "masculino"):
    print(f'sua taxa de metabolismo basal do seu dia a dia é de {Mtmb3:.2f}kcal')
    carbo3 = ((Mresult3-prot*4)*0.6)/ref 
    gord3 = ((Mresult3-prot*4)*0.4)/ref
    arroz = (carbo3/4)*3.57
    batata = (carbo3/4)*5.43
    mandioca = (carbo3/4)*2.63
    azeite = int((gord3/9)*0.08)
    castanha = (gord3/9)*1.51

    while (ref <4) or (ref >6):
        ref = int(input('Valor tem que ser de 4 a 6 refeições por dia.\nDigite novamente:\n'))
        
    if ref == 4:        
        print(f'''Sua dieta é de {Mresult3/ref:.2f}kcal por refeição:
{prot:.2f}kcal de proteina,
{carbo3:.2f}kcal de carboidratos e
{gord3:.2f}kcal de gorduras.

Escolha uma das 3 opções de Protreina, uma das 3 de Carboidratos e uma das 2 de Gordura para cada refeição:

Proteina:
[1]-{frango:.0f}g de frango ou
[2]-{ovo:.0f} claras de ovos ou
[3]-{patinho:.0f}g de patinho.
        
Carboidrato:
[1]-{arroz:.0f}g de arroz branco ou
[2]-{batata:.0f}g de batata doce cozida ou
[3]-{mandioca:.0f}g de mandioca.
        
Gordura:
[1]-{azeite:.0f} colhere(s) de azeite de oliva extravirgem ou
[2]-{castanha:.0f}g de castanha do Pará.
''')
    elif ref == 5:
        print(f'''Sua dieta é {Mresult3/ref:.2f}kcal por refeição.

{prot:.2f}kcal de proteina, 
{carbo3:.2f}kcal de carboidratos e 
{gord3:.2f}kcal de gorduras.

Escolha uma das 3 opções de Protreina, uma das 3 de Carboidratos e uma das 2 de Gordura para cada refeição:

Proteina:
[1]{frango:.0f}g de frango ou
[2]{ovo:.0f} claras de ovos ou
[3]{patinho:.0f}g de patinho.
        
Carboidrato:
[1]{arroz:.0f}g de arroz branco ou
[2]{batata:.0f}g de batata doce cozida ou
[3]{mandioca:.0f}g de mandioca.
        
Gordura:
[1]{azeite:.0f} colhere(s) de azeite de oliva extravirgem ou
[2]{castanha:.0f}g de castanha do Pará.
''')
    elif ref == 6:
        print(f'''Sua dieta é {Mresult3/ref:.2f}kcal por refeição.

{prot:.2f}kcal de proteina, 
{carbo3:.2f}kcal de carboidratos e 
{gord3:.2f}kcal de gorduras.

Escolha uma das 3 opções de Protreina, uma das 3 de Carboidratos e uma das 2 de Gordura para cada refeição:

Proteina:
[1]{frango:.0f}g de frango ou
[2]{ovo:.0f} claras de ovos ou
[3]{patinho:.0f}g de patinho.
        
Carboidrato:
[1]{arroz:.0f}g de arroz branco ou
[2]{batata:.0f}g de batata doce cozida ou
[3]{mandioca:.0f}g de mandioca.
        
Gordura:
[1]{azeite:.0f} colhere(s) de azeite de oliva extravirgem ou
[2]{castanha:.0f}g de castanha do Pará.
''')

elif (atividade == 4) and (sexo == "masculino"):
    print(f'sua taxa de metabolismo basal do seu dia a dia é de {Mtmb4:.2f}kcal')
    carbo4 = ((Mresult4-prot*4)*0.6)/ref 
    gord4 = ((Mresult4-prot*4)*0.4)/ref
    arroz = (carbo4/4)*3.57
    batata = (carbo4/4)*5.43
    mandioca = (carbo4/4)*2.63
    azeite = int((gord4/9)*0.08)
    castanha = (gord4/9)*1.51

    while (ref <4) or (ref >6):
        ref = int(input('Valor tem que ser de 4 a 6 refeições por dia.\nDigite novamente:\n'))
        
    if ref == 4:        
        print(f'''Sua dieta é de {Mresult4/ref:.2f}kcal por refeição:
{prot:.2f}kcal de proteina,
{carbo4:.2f}kcal de carboidratos e
{gord4:.2f}kcal de gorduras.

Escolha uma das 3 opções de Protreina, uma das 3 de Carboidratos e uma das 2 de Gordura para cada refeição:

Proteina:
[1]-{frango:.0f}g de frango ou
[2]-{ovo:.0f} claras de ovos ou
[3]-{patinho:.0f}g de patinho.
        
Carboidrato:
[1]-{arroz:.0f}g de arroz branco ou
[2]-{batata:.0f}g de batata doce cozida ou
[3]-{mandioca:.0f}g de mandioca.
        
Gordura:
[1]-{azeite:.0f} colhere(s) de azeite de oliva extravirgem ou
[2]-{castanha:.0f}g de castanha do Pará.
''')
    elif ref == 5:
        print(f'''Sua dieta é {Mresult4/ref:.2f}kcal por refeição.

{prot:.2f}kcal de proteina, 
{carbo4:.2f}kcal de carboidratos e 
{gord4:.2f}kcal de gorduras.

Escolha uma das 3 opções de Protreina, 
uma das 3 de Carboidratos e 
uma das 2 de Gordura para cada refeição:

Proteina:
[1]{frango:.0f}g de frango ou
[2]{ovo:.0f} claras de ovos ou
[3]{patinho:.0f}g de patinho.
        
Carboidrato:
[1]{arroz:.0f}g de arroz branco ou
[2]{batata:.0f}g de batata doce cozida ou
[3]{mandioca:.0f}g de mandioca.
        
Gordura:
[1]{azeite:.0f} colhere(s) de azeite de oliva extravirgem ou
[2]{castanha:.0f}g de castanha do Pará.
''')
    elif ref == 6:
        print(f'''Sua dieta é {Mresult4/ref:.2f}kcal por refeição.

{prot:.2f}kcal de proteina, 
{carbo4:.2f}kcal de carboidratos e 
{gord4:.2f}kcal de gorduras.

Escolha uma das 3 opções de Protreina,uma das 3 de Carboidratos euma das 2 de Gordura para cada refeição:

Proteina:
[1]{frango:.0f}g de frango ou
[2]{ovo:.0f} claras de ovos ou
[3]{patinho:.0f}g de patinho.
        
Carboidrato:
[1]{arroz:.0f}g de arroz branco ou
[2]{batata:.0f}g de batata doce cozida ou
[3]{mandioca:.0f}g de mandioca.
        
Gordura:
[1]{azeite:.0f} colhere(s) de azeite de oliva extravirgem ou
[2]{castanha:.0f}g de castanha do Pará.
''')

elif (atividade == 1) and (sexo == "feminino"):
    print(f'sua taxa de metabolismo basal do seu dia a dia é de {Ftmb1:.2f}kcal')
    carbo1 = ((Fresult1-prot*4)*0.6)/ref 
    gord1 = ((Fresult1-prot*4)*0.4)/ref
    arroz = (carbo1/4)*3.57
    batata = (carbo1/4)*5.43
    mandioca = (carbo1/4)*2.63
    azeite = int((gord1/9)*0.08)
    castanha = (gord1/9)*1.51

    while (ref <4) or (ref >6):
        ref = int(input('Valor tem que ser de 4 a 6 refeições por dia.\nDigite novamente:\n'))
        
    if ref == 4:        
        print(f'''Sua dieta é de {Fresult1/ref:.2f}kcal por refeição:
{prot:.2f}kcal de proteina,
{carbo1:.2f}kcal de carboidratos e
{gord1:.2f}kcal de gorduras.

Escolha uma das 3 opções de Protreina, uma das 3 de Carboidratos e uma das 2 de Gordura para cada refeição:

Proteina:
[1]-{frango:.0f}g de frango ou
[2]-{ovo:.0f} claras de ovos ou
[3]-{patinho:.0f}g de patinho.
        
Carboidrato:
[1]-{arroz:.0f}g de arroz branco ou
[2]-{batata:.0f}g de batata doce cozida ou
[3]-{mandioca:.0f}g de mandioca.
        
Gordura:
[1]-{azeite:.0f} colhere(s) de azeite de oliva extravirgem ou
[2]-{castanha:.0f}g de castanha do Pará.
''')

    if ref == 5:        
        print(f'''Sua dieta é de {Fresult1/ref:.2f}kcal por refeição:
{prot:.2f}kcal de proteina,
{carbo1:.2f}kcal de carboidratos e
{gord1:.2f}kcal de gorduras.

Escolha uma das 3 opções de Protreina, uma das 3 de Carboidratos e uma das 2 de Gordura para cada refeição:

Proteina:
[1]-{frango:.0f}g de frango ou
[2]-{ovo:.0f} claras de ovos ou
[3]-{patinho:.0f}g de patinho.
        
Carboidrato:
[1]-{arroz:.0f}g de arroz branco ou
[2]-{batata:.0f}g de batata doce cozida ou
[3]-{mandioca:.0f}g de mandioca.
        
Gordura:
[1]-{azeite:.0f} colhere(s) de azeite de oliva extravirgem ou
[2]-{castanha:.0f}g de castanha do Pará.
''')
    if ref == 6:        
        print(f'''Sua dieta é de {Fresult1/ref:.2f}kcal por refeição:
{prot:.2f}kcal de proteina,
{carbo1:.2f}kcal de carboidratos e
{gord1:.2f}kcal de gorduras.

Escolha uma das 3 opções de Protreina, uma das 3 de Carboidratos e uma das 2 de Gordura para cada refeição:

Proteina:
[1]-{frango:.0f}g de frango ou
[2]-{ovo:.0f} claras de ovos ou
[3]-{patinho:.0f}g de patinho.
        
Carboidrato:
[1]-{arroz:.0f}g de arroz branco ou
[2]-{batata:.0f}g de batata doce cozida ou
[3]-{mandioca:.0f}g de mandioca.
        
Gordura:
[1]-{azeite:.0f} colhere(s) de azeite de oliva extravirgem ou
[2]-{castanha:.0f}g de castanha do Pará.
''')

elif (atividade == 2) and (sexo == "feminino"):
    print(f'sua taxa de metabolismo basal do seu dia a dia é de {Ftmb2:.2f}kcal')
    carbo2 = ((Fresult2-prot*4)*0.6)/ref 
    gord2 = ((Fresult2-prot*4)*0.4)/ref
    arroz = (carbo2/4)*3.57
    batata = (carbo2/4)*5.43
    mandioca = (carbo2/4)*2.63
    azeite = int((gord2/9)*0.08)
    castanha = (gord2/9)*1.51

    while (ref <4) or (ref >6):
        ref = int(input('Valor tem que ser de 4 a 6 refeições por dia.\nDigite novamente:\n'))
        
    if ref == 4:        
        print(f'''Sua dieta é de {Fresult2/ref:.2f}kcal por refeição:
{prot:.2f}kcal de proteina,
{carbo2:.2f}kcal de carboidratos e
{gord2:.2f}kcal de gorduras.

Escolha uma das 3 opções de Protreina, uma das 3 de Carboidratos e uma das 2 de Gordura para cada refeição:

Proteina:
[1]-{frango:.0f}g de frango ou
[2]-{ovo:.0f} claras de ovos ou
[3]-{patinho:.0f}g de patinho.
        
Carboidrato:
[1]-{arroz:.0f}g de arroz branco ou
[2]-{batata:.0f}g de batata doce cozida ou
[3]-{mandioca:.0f}g de mandioca.
        
Gordura:
[1]-{azeite:.0f} colhere(s) de azeite de oliva extravirgem ou
[2]-{castanha:.0f}g de castanha do Pará.
''')

    if ref == 5:        
        print(f'''Sua dieta é de {Fresult2/ref:.2f}kcal por refeição:
{prot:.2f}kcal de proteina,
{carbo2:.2f}kcal de carboidratos e
{gord2:.2f}kcal de gorduras.

Escolha uma das 3 opções de Protreina, uma das 3 de Carboidratos e uma das 2 de Gordura para cada refeição:

Proteina:
[1]-{frango:.0f}g de frango ou
[2]-{ovo:.0f} claras de ovos ou
[3]-{patinho:.0f}g de patinho.
        
Carboidrato:
[1]-{arroz:.0f}g de arroz branco ou
[2]-{batata:.0f}g de batata doce cozida ou
[3]-{mandioca:.0f}g de mandioca.
        
Gordura:
[1]-{azeite:.0f} colhere(s) de azeite de oliva extravirgem ou
[2]-{castanha:.0f}g de castanha do Pará.
''')
    if ref == 6:        
        print(f'''Sua dieta é de {Fresult2/ref:.2f}kcal por refeição:
{prot:.2f}kcal de proteina,
{carbo2:.2f}kcal de carboidratos e
{gord2:.2f}kcal de gorduras.

Escolha uma das 3 opções de Protreina, uma das 3 de Carboidratos e uma das 2 de Gordura para cada refeição:

Proteina:
[1]-{frango:.0f}g de frango ou
[2]-{ovo:.0f} claras de ovos ou
[3]-{patinho:.0f}g de patinho.
        
Carboidrato:
[1]-{arroz:.0f}g de arroz branco ou
[2]-{batata:.0f}g de batata doce cozida ou
[3]-{mandioca:.0f}g de mandioca.
        
Gordura:
[1]-{azeite:.0f} colhere(s) de azeite de oliva extravirgem ou
[2]-{castanha:.0f}g de castanha do Pará.
''')

elif (atividade == 3) and (sexo == "feminino"):
    print(f'sua taxa de metabolismo basal do seu dia a dia é de {Ftmb3:.2f}kcal')
    carbo3 = ((Fresult3-prot*4)*0.6)/ref 
    gord3 = ((Fresult3-prot*4)*0.4)/ref
    arroz = (carbo3/4)*3.57
    batata = (carbo3/4)*5.43
    mandioca = (carbo3/4)*2.63
    azeite = int((gord3/9)*0.08)
    castanha = (gord3/9)*1.51

    while (ref <4) or (ref >6):
        ref = int(input('Valor tem que ser de 4 a 6 refeições por dia.\nDigite novamente:\n'))
        
    if ref == 4:        
        print(f'''Sua dieta é de {Fresult3/ref:.2f}kcal por refeição:
{prot:.2f}kcal de proteina,
{carbo3:.2f}kcal de carboidratos e
{gord3:.2f}kcal de gorduras.

Escolha uma das 3 opções de Protreina, uma das 3 de Carboidratos e uma das 2 de Gordura para cada refeição:

Proteina:
[1]-{frango:.0f}g de frango ou
[2]-{ovo:.0f} claras de ovos ou
[3]-{patinho:.0f}g de patinho.
        
Carboidrato:
[1]-{arroz:.0f}g de arroz branco ou
[2]-{batata:.0f}g de batata doce cozida ou
[3]-{mandioca:.0f}g de mandioca.
        
Gordura:
[1]-{azeite:.0f} colhere(s) de azeite de oliva extravirgem ou
[2]-{castanha:.0f}g de castanha do Pará.
''')

    if ref == 5:        
        print(f'''Sua dieta é de {Fresult3/ref:.2f}kcal por refeição:
{prot:.2f}kcal de proteina,
{carbo3:.2f}kcal de carboidratos e
{gord3:.2f}kcal de gorduras.

Escolha uma das 3 opções de Protreina, uma das 3 de Carboidratos e uma das 2 de Gordura para cada refeição:

Proteina:
[1]-{frango:.0f}g de frango ou
[2]-{ovo:.0f} claras de ovos ou
[3]-{patinho:.0f}g de patinho.
        
Carboidrato:
[1]-{arroz:.0f}g de arroz branco ou
[2]-{batata:.0f}g de batata doce cozida ou
[3]-{mandioca:.0f}g de mandioca.
        
Gordura:
[1]-{azeite:.0f} colhere(s) de azeite de oliva extravirgem ou
[2]-{castanha:.0f}g de castanha do Pará.
''')
    if ref == 6:        
        print(f'''Sua dieta é de {Fresult3/ref:.2f}kcal por refeição:
{prot:.2f}kcal de proteina,
{carbo3:.2f}kcal de carboidratos e
{gord3:.2f}kcal de gorduras.

Escolha uma das 3 opções de Protreina, uma das 3 de Carboidratos e uma das 2 de Gordura para cada refeição:

Proteina:
[1]-{frango:.0f}g de frango ou
[2]-{ovo:.0f} claras de ovos ou
[3]-{patinho:.0f}g de patinho.
        
Carboidrato:
[1]-{arroz:.0f}g de arroz branco ou
[2]-{batata:.0f}g de batata doce cozida ou
[3]-{mandioca:.0f}g de mandioca.
        
Gordura:
[1]-{azeite:.0f} colhere(s) de azeite de oliva extravirgem ou
[2]-{castanha:.0f}g de castanha do Pará.
''')

elif (atividade == 4) and (sexo == "feminino"):
    print(f'sua taxa de metabolismo basal do seu dia a dia é de {Ftmb4:.2f}kcal')
    carbo4 = ((Fresult4-prot*4)*0.6)/ref 
    gord4 = ((Fresult4-prot*4)*0.4)/ref
    arroz = (carbo4/4)*3.57
    batata = (carbo4/4)*5.43
    mandioca = (carbo4/4)*2.63
    azeite = int((gord4/9)*0.08)
    castanha = (gord4/9)*1.51

    while (ref <4) or (ref >6):
        ref = int(input('Valor tem que ser de 4 a 6 refeições por dia.\nDigite novamente:\n'))
        
    if ref == 4:        
        print(f'''Sua dieta é de {Fresult4/ref:.2f}kcal por refeição:
{prot:.2f}kcal de proteina,
{carbo4:.2f}kcal de carboidratos e
{gord4:.2f}kcal de gorduras.

Escolha uma das 3 opções de Protreina, uma das 3 de Carboidratos e uma das 2 de Gordura para cada refeição:

Proteina:
[1]-{frango:.0f}g de frango ou
[2]-{ovo:.0f} claras de ovos ou
[3]-{patinho:.0f}g de patinho.
        
Carboidrato:
[1]-{arroz:.0f}g de arroz branco ou
[2]-{batata:.0f}g de batata doce cozida ou
[3]-{mandioca:.0f}g de mandioca.
        
Gordura:
[1]-{azeite:.0f} colhere(s) de azeite de oliva extravirgem ou
[2]-{castanha:.0f}g de castanha do Pará.
''')

    if ref == 5:        
        print(f'''Sua dieta é de {Fresult4/ref:.2f}kcal por refeição:
{prot:.2f}kcal de proteina,
{carbo4:.2f}kcal de carboidratos e
{gord4:.2f}kcal de gorduras.

Escolha uma das 3 opções de Protreina, uma das 3 de Carboidratos e uma das 2 de Gordura para cada refeição:

Proteina:
[1]-{frango:.0f}g de frango ou
[2]-{ovo:.0f} claras de ovos ou
[3]-{patinho:.0f}g de patinho.
        
Carboidrato:
[1]-{arroz:.0f}g de arroz branco ou
[2]-{batata:.0f}g de batata doce cozida ou
[3]-{mandioca:.0f}g de mandioca.
        
Gordura:
[1]-{azeite:.0f} colhere(s) de azeite de oliva extravirgem ou
[2]-{castanha:.0f}g de castanha do Pará.
''')
    if ref == 6:        
        print(f'''Sua dieta é de {Fresult4/ref:.2f}kcal por refeição:
{prot:.2f}kcal de proteina,
{carbo4:.2f}kcal de carboidratos e
{gord4:.2f}kcal de gorduras.

Escolha uma das 3 opções de Protreina, uma das 3 de Carboidratos e uma das 2 de Gordura para cada refeição:

Proteina:
[1]-{frango:.0f}g de frango ou
[2]-{ovo:.0f} claras de ovos ou
[3]-{patinho:.0f}g de patinho.
        
Carboidrato:
[1]-{arroz:.0f}g de arroz branco ou
[2]-{batata:.0f}g de batata doce cozida ou
[3]-{mandioca:.0f}g de mandioca.
        
Gordura:
[1]-{azeite:.0f} colhere(s) de azeite de oliva extravirgem ou
[2]-{castanha:.0f}g de castanha do Pará.
''')


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





