O jogo começa com 21 fósforos disponíveis. Dois jogadores (usuário e computador) se alternam para retirar entre 1 e 4 fósforos por jogada. O objetivo é não ser o jogador que remove o último fósforo.

Estrutura do Código:
Função jogar(primeiro_jogador):

Controla o fluxo principal do jogo.
Recebe como parâmetro quem começa (usuário ou computador).
Enquanto ainda houver fósforos:
Mostra quantos fósforos restam.
Se for a vez do usuário:
Pede ao usuário para escolher um número de fósforos entre 1 e 4.
Valida a jogada (não pode retirar mais fósforos do que há disponíveis ou um número fora do intervalo).
Atualiza o número de fósforos restantes e verifica se o usuário perdeu (tirou o último fósforo).
Se for a vez do computador:
O computador decide sua jogada com a função jogada_computador().
Atualiza os fósforos restantes e verifica se o computador perdeu.
Alterna entre o usuário e o computador a cada turno.
Função jogada_computador(fosforos):

Calcula a jogada do computador:
Tenta manter o número de fósforos restantes como múltiplo de 5, para garantir uma vantagem estratégica.
Se não for possível, escolhe aleatoriamente um número válido (entre 1 e 4).
Função main():

Introduz o jogo e permite ao usuário escolher quem começa (usuário ou computador).
Valida a escolha e inicia o jogo chamando jogar().
Execução do programa:

Quando o código é executado (if __name__ == "__main__":), a função main() é chamada, iniciando o jogo.
Resumidamente:
O jogo dos fósforos implementado aqui é interativo e possui uma estratégia para o computador tentar vencer. O jogador e o computador alternam jogadas até que um deles seja forçado a tirar o último fósforo, perdendo o jogo.






