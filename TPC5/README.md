# Relatório do TPC5
## Data: 07/10/2024
## Autor: Inês Fernandes Freitas

## Resumo do que foi feito:
O TPC5 consistia na realização de uma aplicação para a gestão de um cinema do centro comericial. Tendo utilizado o modelo sugerido no enunciado para a sua concretização. Assim, segue-se o modelo:
Cinema = [Sala];
Sala = [nlugares, vendidos, filme];
nlugares = Int;
filme = String;
vendidos = [Int]. 
Assim para a realização desta aplicação procedi aos seguintes passos:
* Defini as funções essenciais para o funcionamento desta aplicação, entre as quais a criação de uma sala, inserir a sala no cinema, listar o cinema (a qual possibilitava a vizualização dos filmes em exibição e a lotação máxima das respetivas salas), listar a disponibilidade (a qual possibilitava a vizualização dos filmes e os lugares disponiveís para o mesmo), a venda do bilhete (acrecentava à lista dos vendidos do respetivo filme o lugar comprado, ficando assim indisponível) e a verificação de disponibilidade (dava-nos um resultado True caso o lugar estivesse disponível ou False se o lugar estivesse ocupado);
* Posteriormente, defini a função menu que apresenta todas as funções a cima descritas;
* Por último, crontruí a aplicação em si com um menu de interfaces para as diferentes operações. 

