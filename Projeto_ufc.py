def ufc (nome, idade, peso, altura, categoria):
  nome = input("QUAL E SEU NOME?: ")
  print(f"certo, {nome} agora vamos pras proximas perguntas")
  
  idade = int(input("QUANTOS ANOS VOCE TEM?: "))
  print(f"ta bom, {idade} anos")

  peso = float(input(f"QUANTO VOCE PESA?: "))
  print(f"ta, voce tem {peso}kg.")

  altura = float(input(f"QUAL A SUA ALTURA?: "))
  print(f"certo, {altura} de altura")
  print("agora vamos ver em qual categoria voce se encaixa")
if peso < 65:
   print(f"voce se encaixa na {categoria}: peso galo")

elif peso > 65 and peso <70:
   print(f"voce se encaixa na {categoria}: peso medio")

else:
    print(f"voce se encaixa na {categoria}: peso meio pesado")
    print("agora vamos ver se voce esta apto para lutar na UFC, e jaja te daremos uma resposta.")
    print("...................................................................")
    print("fizemos uma analise do seus dados e e isso, voce esta contratado para luta na UFC, iremos arrumar lutas para você, ate la treine bastante e se cuide, boa sorte e parabes.")

ufc("nome", "idade", "peso", "altura", "categoria")