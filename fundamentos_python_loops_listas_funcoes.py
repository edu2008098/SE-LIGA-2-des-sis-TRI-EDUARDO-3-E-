1. Qual é a principal diferença de uso entre o laço for e o laço while

O laço for é utilizado quando sabemos quantas vezes queremos repetir uma ação ou quando precisamos percorrer os elementos de uma sequência, como uma lista. Já o laço while é utilizado quando queremos repetir uma ação enquanto determinada condição for verdadeira.
2. Escreva um laço for em conjunto com a função range() para imprimir os números de 1 a 5 na tela.

Podemos utilizar o for junto com a função range(), que gera uma sequência de números. Como o limite final não é incluído, utilizamos 6 para imprimir até 5.
for numero in range(1, 6):
    print(numero)

3. O que acontece na execução de um programa se a condição de um laço while nunca se tornar falsa (por exemplo, while True:)

O programa entrará em um loop infinito, ou seja, continuará executando repetidamente sem parar. Isso pode consumir recursos do computador e impedir que o programa continue normalmente, caso não exista uma instrução para interromper o laço.
4. Para que serve a instrução break quando utilizada dentro de uma estrutura de repetição

A instrução break serve para interromper imediatamente a execução de um laço de repetição, mesmo que sua condição ainda seja verdadeira.

Exemplo:
for numero in range(1, 6):
    if numero == 3:
        break
    print(numero)

5. Para que serve a instrução continue Explique com suas palavras.

A instrução continue serve para pular a execução restante da repetição atual e passar diretamente para a próxima. Diferentemente do break, ela não encerra o laço.

Exemplo:
for numero in range(1, 6):
    if numero == 3:
        continue
    print(numero)

6. Escreva o código para criar uma lista vazia chamada sistemas.

Para criar uma lista vazia, utilizamos colchetes [].
sistemas = []

7. Qual método do Python é utilizado para adicionar um novo elemento ao final de uma lista existente

O método utilizado é o append(), que adiciona um novo elemento ao final da lista.

Exemplo:
8. Dado o código: linguagens = ["Python", "Java", "C#", "PHP"]. Como você acessa e imprime especificamente o valor "C#"linguagens = ["Python", "Java", "C#", "PHP"]

print(linguagens[2])


Utilizamos o índice 2, pois as posições de uma lista em Python começam pelo número zero.
9. Qual função nativa do Python utilizamos para descobrir a quantidade de elementos que existem dentro de uma lista

Utilizamos a função len(), que retorna a quantidade de elementos existentes em uma lista.

Exemplo:
linguagens = ["Python", "Java", "C#", "PHP"]

print(len(linguagens))
10. Strings em Python funcionam como listas de caracteres. Dada a variável palavra = "Tech", como extraímos apenas a primeira letra ("T")

Utilizamos o índice 0 para acessar o primeiro caractere da string.
palavra = "Tech"

print(palavra[0])
11. Qual palavra-chave (keyword) é usada obrigatoriamente para declarar (definir) uma função em Python

A palavra-chave utilizada é def. Ela indica o início da definição de uma função em Python.
12. Crie a estrutura de uma função simples chamada saudar que não recebe parâmetros e apenas imprime "Bem-vindo ao sistema!".

Podemos criar a função utilizando def, seguido do nome da função e parênteses vazios.
def saudar():
    print("Bem-vindo ao sistema!")

saudar()
13. Para que serve a palavra-chave return dentro de uma função Qual a diferença entre return e print()

A palavra-chave return serve para devolver um resultado da função para quem a chamou, permitindo utilizar esse valor em outras partes do programa.

Já o print() serve apenas para exibir informações na tela. Portanto, return devolve um valor, enquanto print() mostra uma informação no console.
14. Escreva uma função chamada calcular_dobro que receba um parâmetro numero, calcule o dobro desse valor e retorne o resultado.

Podemos multiplicar o parâmetro numero por 2 e utilizar return para devolver o resultado.
def calcular_dobro(numero):
    return numero * 2

resultado = calcular_dobro(10)

print(resultado)
15. O que são parâmetros com valores padrão (default) em uma função Python Dê um exemplo simples de código.

Parâmetros com valores padrão são aqueles que já possuem um valor definido na criação da função. Assim, quando chamamos a função sem informar esse parâmetro, o Python utiliza automaticamente o valor padrão.

Exemplo:
def saudar(nome="Visitante"):
    print(f"Bem-vindo ao sistema, {nome}!")

saudar()
saudar("Carlos")
