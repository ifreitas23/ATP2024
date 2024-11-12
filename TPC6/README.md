# Relatório do TPC6
## Data: 14/10/2024
## Autor: Inês Fernandes Freitas

## Resumo do que foi feito:
O TPC6 consistia na realização de uma aplicação para a gestão de alunos, devendo esta apresentar as seguintes características:
* O modelo da turma e do aluno deveria ser o seguite, turma = [aluno] e aluno = (nome, id, [notaTPC, notaProj, notaTeste]), ou seja, a turma uma lista de alunos e o aluno um tuplo com as suas informações: nome, id e lista com as notas dos momentos de avalição; 
* Além disso, a aplicação deveria apresentar este menu:
    - 1) Criar uma turma
    - 2) Inserir um aluno na turma
    - 3) Listar a turma
    - 4) Consultar um aluno por id
    - 5) Guardar a turma em ficheiro
    - 6) Carregar uma turma dum ficheiro
    - 0) Sair

Assim para a realização desta aplicação procedi aos seguintes passos:
* Inicialmente, defini as diferentes funções (criar uma turma, inserir aluno numa turma, listar turma, consultar aluno por id, guardar a turma num ficheiro e carregar a turma dum ficheiro);
* Posteriormente, defini a função menu e uma interface para controlar o programa;
* Por fim, utilizado a aplicação criei uma turma de 5 alunos tendo guardado essa informação num ficheiro (turmabiomed.txt).