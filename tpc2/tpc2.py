sup=100
inf=0
x=0
n=0
pergunta=str()
acertou= str("acertou")
while pergunta!=str(acertou):
    n=n+1
    x=int((sup+inf)/2)
    pergunta=input(f"o seu número é {x}?")
    if pergunta == "maior":
        inf=x
    else:
        sup=x
print(f"O computador advinhou o número em {n} tentativas")


modo = int( input("Escolha a forma como pretende jogar?\n 0-Advinha o numero do computador \n1-O computador advinha o teu número"))
sup = 100
inf = 0
x = 0
n = 0
t = 1
if modo == 0:
    import random
    r = random.randrange(1,100)
    x = int(input("Diga um número"))
    while r!=x:
        t = t + 1
        if r>x:
            print("maior")
        else:
            print("menor")
        x =  int(input("Diga um número"))
    print("Acertou em " + str(t) +  "tentativas!")
elif modo == 1:
    pergunta = str()
    acertou = "acertou"
    while pergunta!= acertou:
        n = n + 1
        x = int((sup + inf) / 2)
        pergunta = input("O seu número é "+ str(x) + "?")
        if pergunta == "maior":
            inf = x
        else:
            sup = x
    print("O computador advinhou o número em " + str(n) + " tentativas")