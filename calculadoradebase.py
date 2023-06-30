import os

opcao = 'Ok'

def binarioadecimal(valor):
    caracteres = len(valor)
    indice = caracteres - 1
    soma = 0
    for i in range(caracteres):
        soma = soma + (int(valor[i]) * (2**indice))
        indice = indice - 1
    return soma





def octaladecimal(valor):
    caracteres = len(valor)
    indice = caracteres - 1
    soma = 0
    for i in range(caracteres):
        soma = soma + (int(valor[i]) * (8**indice))
        indice = indice - 1
    return soma



def hexadecimaladecimal(valor):
    caracteres = len(valor)
    indice = caracteres - 1
    soma = 0
    novovalor = 0
    for i in range(caracteres):
        if valor[i] == 'a':
            novovalor = 10
        elif valor[i] == 'b':
            novovalor = 11
        elif valor[i] == 'c':
            novovalor = 12
        elif valor[i] == 'd':
            novovalor = 13
        elif valor[i] == 'e':
            novovalor = 14
        elif valor[i] == 'f':
            novovalor = 15


        if novovalor == 0:
            soma = soma + (int(valor[i]) * (16**indice))
        elif novovalor > 0:
            soma = soma + (int(novovalor) * (16**indice))
        indice = indice - 1
        novovalor = 0
    return soma



def decimalabinario(valor):
    valores = []
    valor = int(valor)
    while valor > 0:
        resultado = valor // 2
        novovalor = valor % 2
        valor = resultado
        valores.append(novovalor)

    valores.reverse()
    lista = ''.join(map(str, valores))

    return lista



def decimalaoctal(valor):
    valores = []
    valor = int(valor)
    while valor > 0:
        resultado = valor // 8
        novovalor = valor % 8
        valor = resultado
        valores.append(novovalor)

    valores.reverse()
    lista = ''.join(map(str, valores))

    return lista



def decimalahexa(valor):
    valores = []
    valor = int(valor)
    while valor > 0:
        resultado = valor // 16
        novovalor = valor % 16
        valor = resultado
        if novovalor == 16:
            novovalor = '0'
        elif novovalor == 15:
            novovalor = 'f'
        elif novovalor == 14:
            novovalor = 'e'
        elif novovalor == 13:
            novovalor = 'd'
        elif novovalor == 12:
            novovalor = 'c'
        elif novovalor == 11:
            novovalor = 'b'
        elif novovalor == 10:
            novovalor = 'a'
        valores.append(novovalor)

    valores.reverse()
    lista = ''.join(map(str, valores))

    return lista

basedonumero = ''
Passar = True



while opcao != '1':
    Passar = True
    if(basedonumero == ''):
        numero = input('Digite o valor que deseja converter: \n')
        os.system('cls' if os.name == 'nt' else 'clear')
        totalcaracter = len(numero)
    for i in range(totalcaracter):
        verificar = numero[i]
        if verificar == 'a' or verificar == 'b' or verificar == 'c' or verificar == 'd' or verificar == 'e' or verificar == 'f':
            basedonumero = '4'
        elif verificar == 'g' or verificar == 'h' or verificar == 'i' or verificar == 'j' or verificar == 'k' or verificar == 'l':
            Passar = False
            print('Digite um numero valido!!!')
        elif verificar == 'm' or verificar == 'n' or verificar == 'o' or verificar == 'p' or verificar == 'q' or verificar == 'r':
            Passar = False
            print('Digite um numero valido!!!')
        elif verificar == 's' or verificar == 't' or verificar == 'u' or verificar == 'w' or verificar == 'x' or verificar == 'y' or verificar == 'z':
            Passar = False
            print('Digite um numero valido!!!')
    if(basedonumero == ''):
        if(Passar == True):
            print('Escolha em qual base está seu numero')
            basedonumero = input('1 - Binario / 2 - Octal / 3 - Decimal / 4 - Hexadecimal : \n')
            os.system('cls' if os.name == 'nt' else 'clear')
    if(basedonumero == '1'):
        print('Digite para qual base deseja converter')
        baseparaconverter = input('1 - Octal / 2 - Decimal / 3 - Hexadecimal : \n')
        os.system('cls' if os.name == 'nt' else 'clear')
        if(baseparaconverter == '1'):
            decimal = str(binarioadecimal(numero))
            resultado = str(decimalaoctal(decimal))
            print(f'O valor da sua converção de binario para Octal é : {resultado}')
            print('Digite uma opção para continuar ou sair de execução')
            opcao = input("1 - Sair / 2 - Converter para outra base : \n")
            os.system('cls' if os.name == 'nt' else 'clear')
            basedonumero = '2'
            numero = resultado
        elif(baseparaconverter == '2'):
            resultado = str(binarioadecimal(numero))
            print(f'O valor da sua converção de binario para Decimal é : {resultado}')
            print('Digite uma opção para continuar ou sair de execução')
            opcao = input("1 - Sair / 2 - Converter para outra base : \n")
            os.system('cls' if os.name == 'nt' else 'clear')
            basedonumero = '3'
            numero = resultado
        elif(baseparaconverter == '3'):
            decimal = str(binarioadecimal(numero))
            resultado = str(decimalahexa(decimal))
            print(f'O valor da sua converção de binario para Hexadecimal é : {resultado}')
            print('Digite uma opção para continuar ou sair de execução')
            opcao = input("1 - Sair / 2 - Converter para outra base : \n")
            os.system('cls' if os.name == 'nt' else 'clear')
            basedonumero = '4'
            numero = resultado
    elif(basedonumero == '2'):
        print('Digite para qual base deseja converter')
        baseparaconverter = input('1 - Binario / 2 - Decimal / 3 - Hexadecimal : \n')
        os.system('cls' if os.name == 'nt' else 'clear')
        if(baseparaconverter == '1'):
            decimal = str(octaladecimal(numero))
            resultado = str(decimalabinario(decimal))
            print(f'O valor da sua converção de Octal para Binario é : {resultado}')
            print('Digite uma opção para continuar ou sair de execução')
            opcao = input("1 - Sair / 2 - Converter para outra base : \n")
            os.system('cls' if os.name == 'nt' else 'clear')
            basedonumero = '1'
            numero = resultado
        elif(baseparaconverter == '2'):
            resultado = str(octaladecimal(numero))
            print(f'O valor da sua converção de Octal para Decimal é : {resultado}')
            print('Digite uma opção para continuar ou sair de execução')
            opcao = input("1 - Sair / 2 - Converter para outra base : \n")
            os.system('cls' if os.name == 'nt' else 'clear')
            basedonumero = '3'
            numero = resultado
        elif(baseparaconverter == '3'):
            decimal = str(octaladecimal(numero))
            resultado = str(decimalahexa(decimal))
            print(f'O valor da sua converção de Octal para Hexadecimal é : {resultado}')
            print('Digite uma opção para continuar ou sair de execução')
            opcao = input("1 - Sair / 2 - Converter para outra base : \n")
            os.system('cls' if os.name == 'nt' else 'clear')
            basedonumero = '4'
            numero = resultado
    elif(basedonumero == '3'):
        print('Digite para qual base deseja converter')
        baseparaconverter = input('1 - Binario / 2 - Octal / 3 - Hexadecimal : \n')
        os.system('cls' if os.name == 'nt' else 'clear')
        if(baseparaconverter == '1'):
            resultado = str(decimalabinario(decimal))
            print(f'O valor da sua converção de Decimal para Binario é : {resultado}')
            print('Digite uma opção para continuar ou sair de execução')
            opcao = input("1 - Sair / 2 - Converter para outra base : \n")
            os.system('cls' if os.name == 'nt' else 'clear')
            basedonumero = '1'
            numero = resultado
        elif(baseparaconverter == '2'):
            resultado = str(decimalaoctal(numero))
            print(f'O valor da sua converção de Decimal para Octal é : {resultado}')
            print('Digite uma opção para continuar ou sair de execução')
            opcao = input("1 - Sair / 2 - Converter para outra base : \n")
            os.system('cls' if os.name == 'nt' else 'clear')
            basedonumero = '2'
            numero = resultado
        elif(baseparaconverter == '3'):
            resultado = str(decimalahexa(decimal))
            print(f'O valor da sua converção de Decimal para Hexadecimal é : {resultado}')
            print('Digite uma opção para continuar ou sair de execução')
            opcao = input("1 - Sair / 2 - Converter para outra base : \n")
            os.system('cls' if os.name == 'nt' else 'clear')
            basedonumero = '4'
            numero = resultado
    elif(basedonumero == '4'):
        print('Digite para qual base deseja converter')
        baseparaconverter = input('1 - Binario / 2 - Octal / 3 - Decimal : \n')
        os.system('cls' if os.name == 'nt' else 'clear')
        if(baseparaconverter == '1'):
            decimal = str(hexadecimaladecimal(numero))
            resultado = str(decimalabinario(decimal))
            print(f'O valor da sua converção de Hexadecimal para Binario é : {resultado}')
            print('Digite uma opção para continuar ou sair de execução')
            opcao = input("1 - Sair / 2 - Converter para outra base : \n")
            os.system('cls' if os.name == 'nt' else 'clear')
            basedonumero = '1'
            numero = resultado
        elif(baseparaconverter == '2'):
            decimal = str(hexadecimaladecimal(numero))
            resultado = str(decimalaoctal(decimal))
            print(f'O valor da sua converção de Hexadecimal para Octal é : {resultado}')
            print('Digite uma opção para continuar ou sair de execução')
            opcao = input("1 - Sair / 2 - Converter para outra base : \n")
            os.system('cls' if os.name == 'nt' else 'clear')
            basedonumero = '2'
            numero = resultado
        elif(baseparaconverter == '3'):
            resultado = str(hexadecimaladecimal(numero))
            print(f'O valor da sua converção de Hexadecimal para Decimal é : {resultado}')
            print('Digite uma opção para continuar ou sair de execução')
            opcao = input("1 - Sair / 2 - Converter para outra base : \n")
            os.system('cls' if os.name == 'nt' else 'clear')
            basedonumero = '3'
            numero = resultado
