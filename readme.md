# Projeto: Rede de Colaboração Acadêmica Utilizando Union-Find

### Tema:
O projeto tem como ideia criar uma **Rede de Colaboração Acadêmica** que facilita na formação de grupos de estudo entre os alunos com base nas disciplinas que estão cursando,já cursaram ou que compartilham interesses acadêmicos, ajudando na colaboração e mentorias.

### Cenário de Aplicação:
Na universidade onde os alunos cursam varias cadeiras e tem varios tópicos de interesses diferentes eles têm dificuldades em encontrar colegas para colaborar em disciplinas específicas e projetos. Esse sistema automatiza a criação de grupos de estudo, utilizando o **Union-Find** para agrupar alunos de forma eficiente com base nas disciplinas e interesses, permitindo que alunos se ajudem mutuamente em seus estudos.

## 2. Descrição do Problema

O problema é gerenciar grupos de alunos que compartilham disciplinas em comum, mas sem misturar alunos de disciplinas diferentes em um mesmo grupo. A estrutura de dados **Union-Find** é utilizada para resolver esse problema, facilitando a identificação de alunos que pertencem ao mesmo grupo em uma determinada disciplina, permitindo verificar a conexão entre eles e exibir os alunos conectados.

### Objetivo:
- Agrupar alunos que compartilham disciplinas específicas.
- Permitir verificar se dois alunos estão no mesmo grupo.
- Exibir todos os alunos conectados a um determinado aluno dentro de uma disciplina.

## 3. Implementação

O projeto implementa o **Union-Find** com as otimizações:
- **Compressão de Caminho**: Para tornar as buscas mais rápidas.
- **União por Rank**: Para balancear a estrutura, mantendo sua eficiência.

### Funcionalidades Implementadas:
1. **Adicionar Aluno**: Permite a inserção de novos alunos, associando-os às disciplinas que estão cursando.
2. **Unir Alunos por Disciplina**: Alunos que compartilham uma disciplina são agrupados utilizando a estrutura Union-Find.
3. **Verificar se Alunos Estão no Mesmo Grupo**: Verifica se dois alunos pertencem ao mesmo grupo, verificando as conexões por disciplina.
4. **Exibir Grupo de um Aluno**: Exibe todos os alunos pertencentes ao mesmo grupo de um aluno em uma disciplina específica.

### Estrutura:
- **UnionFind**: Classe que realiza as operações de união e busca entre alunos.
- **GerenciadorDisciplinas**: Gerencia diferentes instâncias de Union-Find, uma para cada disciplina.

### Desafios Resolvidos:
- **Gerenciamento Dinâmico de Alunos**: Alunos podem ser adicionados dinamicamente a disciplinas, e o sistema atualiza as conexões.
- **Eficiência**: Utilização de otimizações como compressão de caminho e união por rank para garantir que as operações sejam rápidas mesmo com um grande número de alunos e disciplinas.

## 4. Visualização e Interação

A interação com o sistema é feita por um **menu de texto** simples, oferecendo as seguintes opções ao usuário:
1. Adicionar alunos e associá-los a disciplinas.
2. Unir alunos de disciplinas específicas.
3. Verificar se dois alunos pertencem ao mesmo grupo.
4. Exibir o grupo de um aluno em uma disciplina.

## Estrutura do Código

### Arquitetura:
O código está dividido em classes que separam a lógica do Union-Find e o gerenciamento de disciplinas, facilitando a manutenção e a extensão do projeto. O projeto também inclui tratamento de erros para casos em que um aluno não existe ou não está associado a uma disciplina.

### Testes e Robustez:
Foram implementados testes básicos para garantir que as operações de união e busca funcionem corretamente, além de tratamento de erros para garantir que o sistema seja robusto em casos de uso inválido ou de dados inconsistentes.

## Considerações Finais

Este projeto proporciona uma solução eficiente para o gerenciamento de grupos de estudo em um ambiente educacional, aplicando algoritmos avançados como o Union-Find para organizar e conectar alunos. O sistema pode ser expandido para incluir mais funcionalidades, como recomendações automáticas de mentores e métricas de desempenho dos grupos.
