'''
listaA = []
listaB = []
listaC = []

Utilizando as listas acima, crie um algoritmo que para cada opção do menu abaixo:


Menu
1- Inserir números inteiros na listaA
2- Imprimir listaA individualmente
3- Retirar elemento listaA
4- Ler um número e mostrar quantas vezes este número se repete na lista
5- Copiar todos elementos pares da listaA para a listaB
6- Copiar todos os índices impares da listaA para a listaC
7- Ler um valor de índice e mostrar qual elemento ocupa esta posição
8- Ler um número e mostrar qual seu índice na listaC
'''

listaA = []
listaB = []
listaC = []

while True:
    escolha = input(
          """Menu
            1- Inserir números inteiros na listaA
            2- Imprimir listaA individualmente
            3- Retirar elemento listaA
            4- Ler um número e mostrar quantas vezes este número se repete na lista
            5- Copiar todos elementos pares da listaA para a listaB
            6- Copiar todos os índices impares da listaA para a listaC
            7- Ler um valor de índice e mostrar qual elemento ocupa esta posição
            8- Ler um número e mostrar qual seu índice na listaC
            Escolha >>: """
    )
    if escolha == '1':
        while True:
            try:
                listaA.append(int(input("Insira o número que você deseja incluir na listaA: ")))
                break
            except:
                print("Isso não é um número")
            print(listaA)

    if escolha == '2':
        listaA = [1,11,33,42,57,50,21,17,5]

        print("listaA: ",listaA)
        for elemento in listaA:
            print(elemento)

        ''' outra maneira
            len() = função que retorna o tamanho da lista / string
        for indice in range(len(listaA)):
            print(indice, listaA[indice])
        '''
    if escolha == '3':
        listaA = [1,11,33,42,57,50,21,17,5]

        try:
            numero = (int(input("Digite o número a ser retirado da lista: ")))
            listaA.remove(numero)
        except:
            print("Você não digitou um número ou o número não existe nesta lista")
        print(listaA)

        ''' outra maneira
        try:
            indice = int(input("Digite o indice do elemento a ser retirado da lista: "))
            del(listaA[indice])
        except:
            print("Isso não é um número de índice") 
        print (listaA)
        '''

    if escolha == '4':
        listaA = [1,11,33,42,57,11,50,21,17,5,11,33]
        try:
            numero = int(input("Digite o número para ver se repete na lista: "))
            if numero not in listaA:
                print(f"O número {numero} não está na lista")
            else:
                repete = listaA.count(numero)
                if repete > 1:
                    print(f"O número {numero} repete {repete-1}")
                else:
                    print(f"O número {numero} está na lista, mas não se repete.")
        except:
            print("Não é um número. ")
        

    if escolha == '5':
        listaA = [1,11,33,42,57,11,50,21,17,5,11,33]
        for numero in listaA:
            if numero % 2 == 0:
                listaB.append(numero)
        print(listaA)
        print(listaB)

    if escolha == '6':
        listaA = [1,11,33,42,57,11,50,21,17,5,11,33]
        for indice in range(len(listaA)):
            if indice % 2 != 0:
                listaC.append(listaA[indice])
        print(listaA)
        print(listaC)

    if escolha == '7':
        listaA = [1,11,33,42,57,11,50,21,17,5,11,33]
        try:
            indice = int(input("Digite o índice do número desejado: "))
            if indice >= 0 and indice < len(listaA):
                print(listaA[indice])
            else:
                print("Não é um índice válido para essa lista.")
        except:
            print("Não é um número. ")


    if escolha == '8':
        listaC = [1,11,33,42,57,11,50,21,17,5,11,33]

        try:
            numero = int(input("Digite um número: "))
            for indice in range(len(listaC)):
                if numero == listaC[indice]:
                    print(f"O número {numero} está na posição {indice} da lista.")
        except:
            print("Você não digitou um número.")






        

