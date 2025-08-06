import unicodedata

nome = input("Digite seu nome: ")


nome_normalizado = unicodedata.normalize('NFD', nome)
nome_sem_acentos = ''.join(c for c in nome_normalizado if unicodedata.category(c) != 'Mn')
nome_minusculo = nome_sem_acentos.lower()

nome = nome_minusculo
nome = nome_normalizado
nome = nome_sem_acentos.lower()

vogal = 0
consonante = 0

print(nome)
for letra in nome:

        if (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"or letra == " "):
            vogal += 1
            if (letra == " "):
                vogal -= 1
        else:
            consonante += 1

print("O seu nome tem tantas vogais %d, e tantas consonante %d"%(vogal,consonante))

familia = ["Joao P","Maria","Joao M","Marcos"]
for presente in familia:
    print
for num in range(1,5):
    print
print(num,presente)
_________________________________________________________________________________________________________________________________________________________________________________________
print("Calculador de IMC")

nome = input("Qual o seu nome? ").capitalize()
idade = int(input("Qual a sua idade? "))
altura = int(input("Em centimetros qual a sua idade? (170) "))
genero = (input("Qual o seu genero de nascimento? (M ou F) ")).upper()
peso = float(input("Qual o seu peso? (Ex: 50) "))


print(f"Olá {nome}, seu peso é {peso} e altura {altura} ")
 
altura = altura/100

if (genero == "M") :
    imc = round( peso/(altura*altura), 2)
    if imc < 18.5:
        print("Sua classificação é: Baixo Peso ")
    elif 18.5 <= imc <= 24.9:
       print("Sua classificação é: normal ")
    elif 25.0 <= imc <= 29.9:
       print("Sua classificação é: excesso de peso ")
    elif 30.0 <= imc <= 34.9 :
       print("Sua classificação é: Obesidade 1 ")
    elif 35 <= imc <= 39.9:
       print("Sua classificação é: Obesidade 2 ")
    elif imc >= 40.0 :
        print("Sua classificacao é Obesidade 3 ")
    print(f"Seu IMC é {imc} ")
    
else: 
    imc = round( peso/(altura*altura), 2)
    if imc < 18.5:
        print("Sua classificação é: Baixo Peso ")
    elif 18.5 <= imc <= 24.9:
       print("Sua classificação é: normal ")
    elif 25.0 <= imc <= 29.9:
       print("Sua classificação é: excesso de peso ")
    elif 30.0 <= imc <= 34.9 :
       print("Sua classificação é: Obesidade 1 ")
    elif 35 <= imc <= 39.9:
       print("Sua classificação é: Obesidade 2 ")
    elif imc >= 40.0 :
        print("Sua classificacao é Obesidade 3 ")
    print(f"Seu IMC é {imc} ")






