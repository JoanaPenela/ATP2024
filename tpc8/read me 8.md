
a)
O código a seguir combina os elementos exclusivos de duas listas ao mesmo tempo. A função ncomuns é responsável por criar duas listas:

A primeira lista contém os elementos de lista1 que não estão presentes em lista2.
A segunda lista inclui os elementos de lista2 que não estão presentes em lista1.
A função nao_comuns retorna todos os elementos de ambas as listas (ou seja, lista1 + lista2), mas apenas os que são exclusivos de uma lista, ou seja, que não aparecem nas duas simultaneamente.
Ambas as abordagens retornam os elementos que ocorrem apenas em uma das listas, sem incluir duplicatas.
b)
O código divide um texto usando o método split. Palavras com mais de 3 letras são adicionadas à lista chamada lista.

c)
Recebe as palavras da lista lista e imprime o índice (adicionando 1 ao índice para que não seja 0) e a palavra correspondente.

TPC2
a)
Recebe duas strings, uma string principal e uma substring, e o objetivo é verificar quantas vezes a substring ocorre dentro da string principal.

b)
Recebe uma lista de números e organiza-a em ordem crescente utilizando o método sort. Após isso, calcula o produto dos três menores números da lista e retorna o resultado.

c)
Este código reduz um número inteiro a um único dígito, somando repetidamente os dígitos do número até que reste apenas um único dígito.
Enquanto o número tiver mais de um dígito (ou seja, num >= 10), o processo continua.
Em cada iteração, o código calcula a soma dos dígitos do número e atualiza num com esse valor.

d)
A função myIndexOf(s1, s2) procura a posição de uma substring (s2) dentro de uma string (s1).

Se s2 estiver presente em s1, a função usa o método index para retornar a posição da primeira ocorrência de s2 em s1.
Se s2 não for encontrado em s1, a função retorna -1, indicando que a substring não foi localizada.
TPC3
a)
Verifica quantos posts existem na rede social.

b)
Verifica quantos posts de um autor específico existem na rede social, pesquisando pelo nome do autor.

c)
Adiciona autores de posts que ainda não estão presentes na lista de autores.

d)
A função insPost recebe os seguintes parâmetros:

redeSocial: Uma lista que armazena os posts.
conteudo: O texto do post.
autor: O nome do autor do post.
dataCriacao: A data de criação do post.
comentarios: O número inicial de comentários.
A criação do novo post envolve representar o post como um dicionário com as seguintes chaves:

'id': Um identificador único para o post, no formato 'pX', onde X é o número total de posts, incrementado em 1 (assumindo que a função quantosPost retorna o número de posts atuais).
'conteudo': O texto do post.
'autor': O nome do autor.
'dataCriacao': A data de criação do post (em formato string).
'comentarios': A quantidade inicial de comentários.
O novo post é adicionado à lista redeSocial com o método .append().
A função retorna a lista redeSocial atualizada.

e)
A função recebe os parâmetros:

redeSocial: Uma lista de dicionários, onde cada dicionário representa um post com uma chave 'id'.
id: O identificador ('id') do post a ser removido.
A função percorre a lista redeSocial, compara a chave 'id' de cada post com o valor fornecido de id. Se houver uma correspondência, o post é removido da lista com o método .remove(post).
A função retorna a lista atualizada de posts (redeSocial), agora sem o post removido.

f)
A função recebe o parâmetro redeSocial, uma lista de dicionários, onde cada dicionário representa um post, e inclui a chave 'autor'.
A função cria uma lista vazia chamada lista e percorre cada post na lista redeSocial. Para cada post, a função adiciona à lista lista uma tupla contendo o autor do post (post['autor']) e o próprio post.
A função retorna a lista de tuplas, onde cada tupla tem o formato (autor, post).

g)
A função recebe os parâmetros:

redeSocial: Uma lista de dicionários, onde cada dicionário representa um post e inclui uma lista de comentários na chave 'comentarios'.
autor: O nome do autor dos comentários que você deseja buscar.
A função inicializa uma lista vazia chamada lista e percorre cada post em redeSocial. Para cada post, percorre a lista de comentários (post['comentarios']). Se o autor do comentário (comentario['autor']) corresponde ao autor fornecido, o post é adicionado à lista lista.
A função retorna a lista lista, contendo os posts nos quais o autor especificado fez comentários.

