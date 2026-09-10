def matematica_projeto(numero1, numero2, operaçoes, resultado):
    #meu projeto de aplicativo matematico
    print(" bem vindo ao Lv Math, o aplicativo de calculos matematicos.")
    print("as operações disponiveis no Lv math são")
    print(" soma: +")
    print("subtração: -")
    print("multiplicação: *")
    print("divião: /")
    print("divião inteira: //")
    print("resto da divisão: %")
    print("potencia: **")
    print("................................................................................................")


    operaçoes = str(input("digite o tipo da operaçao: "))
    numero1 = int(input("digite o primeiro valor: "))
    numero2 = int(input("digite o segundo valor: "))
    
    if operaçoes == "+":
        resultado = numero1 + numero2
        print(f"o resultado da soma é: {resultado}")

    elif operaçoes == "-":
        resultado = numero1 - numero2
        print(f"o resultado da subtraçao é: {resultado}")

    if operaçoes == "*":
        resultado = numero1 * numero2
        print(f"o resultado da multiplicaçao é : {resultado}")


    elif operaçoes == "/":
        resultado = numero1 / numero2
        print(f"o resultado da divisao é: {resultado}")

    if operaçoes == "//":
        resultado = numero1 // numero2
        print (f"o resultado da divisão inteira é: {resultado}")


    elif operaçoes == "%":
        resultado = numero1 % numero2
        print (f"o resultado do resta da divião e: {resultado}")

    if operaçoes == "**":
         resultado =  numero1 ** numero2
         print(f"o resultado da potencia é: {resultado}")

matematica_projeto("numero1", "numero2", "operaçoes", "resultado")