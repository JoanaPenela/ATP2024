O código que você forneceu implementa um jogo de adivinhação de números, com duas modalidades:

Modo 0: O jogador escolhe um número entre 1 e 100, e o computador tenta adivinhar o número, perguntando se o número do jogador é maior ou menor do que o número sugerido pelo computador.
Modo 1: O computador escolhe um número entre 1 e 100, e o jogador tenta adivinhar o número, recebendo feedback se o número escolhido pelo computador é maior ou menor que o palpite do jogador.
Explicação do código:
Parte 1 - O computador adivinha o número do jogador (Modo 1):
O computador começa com um intervalo de possíveis números entre inf = 0 e sup = 100.
O programa tenta adivinhar o número escolhido pelo jogador usando a estratégia de busca binária: a cada tentativa, ele faz uma pergunta ao jogador se o número adivinhado é o correto. Se o número for maior, o intervalo de busca é ajustado para o intervalo inferior, e se o número for menor, o intervalo é ajustado para o intervalo superior.
O loop continua até o computador adivinhar o número corretamente. O número de tentativas (n) é contado e exibido ao final.
Parte 2 - O jogador adivinha o número do computador (Modo 0):
O computador escolhe aleatoriamente um número entre 1 e 100 usando a função random.randrange(1, 100).
O jogador tenta adivinhar o número escolhido pelo computador. O programa solicita um palpite e dá feedback se o número do computador é maior ou menor do que o palpite do jogador.
O loop continua até o jogador acertar o número, e o número de tentativas (t) é contado e exibido ao final.
Detalhes do código:
Modo 1: O computador adivinha o número
python
Copiar código
sup = 100
inf = 0
x = 0
n = 0
pergunta = str()
acertou = "acertou"

while pergunta != acertou:
    n = n + 1
    x = int((sup + inf) / 2)
    pergunta = input(f"O seu número é {x}?")
    if pergunta == "maior":
        inf = x
    else:
        sup = x

print(f"O computador adivinhou o número em {n} tentativas.")
O código começa com o intervalo de 0 a 100.
O computador faz uma sugestão de número (x), perguntando se o número é o adivinhado. O jogador responde com "maior", "menor" ou "acertou".
Se o número sugerido pelo computador for menor, o intervalo é ajustado (inf = x), e se for maior, o intervalo é ajustado (sup = x).
O loop termina quando o computador adivinhar o número corretamente, e o número de tentativas é exibido.
Modo 0: O jogador adivinha o número
python
Copiar código
import random
r = random.randrange(1, 100)
x = int(input("Diga um número"))
t = 1
while r != x:
    t = t + 1
    if r > x:
        print("maior")
    else:
        print("menor")
    x = int(input("Diga um número"))
print("Acertou em " + str(t) + " tentativas!")
O computador escolhe aleatoriamente um número entre 1 e 100.
O jogador tenta adivinhar o número. O programa dá feedback se o número do computador é maior ou menor que o palpite do jogador.
O loop termina quando o jogador adivinhar corretamente, e o número de tentativas é mostrado.