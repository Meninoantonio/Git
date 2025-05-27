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








