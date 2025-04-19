# micro: Teclas de atalho padrão

Abaixo estão tabelas simples das teclas de atalho padrão e suas funções. Para mais informações sobre vincular teclas de atalho personalizadas ou alterar as ligações padrão, por favor execute `> help keybindings`

Lembre-se de que *todas* as teclas de atalho aqui podem ser associadas a novas funções! Se você não gosta de alguma delas, você pode alterá-la!

## Usuário avançado

| Tecla de atalho | Descrição da função                                                                                                 |
| --------------- | ------------------------------------------------------------------------------------------------------------------- |
| Ctrl-e          | Abre um prompt de comando para executar comandos (Veja `> help commands` para obter uma lista de comandos válidos). |
| Tab             | No prompt de comando, ele irá completar, se possível.                                                               |
| Ctrl-b          | Execute um comando do shell (Isso fechará `micro` enquanto seu comando é executado).                                |

## Navegação

| Tecla de atalho                | Descrição da função                                                                        |
| ------------------------------ | ------------------------------------------------------------------------------------------ |
| Setas direcionais              | Move o cursor                                                                              |
| Shift-setas direcionais        | Move o cursor e seleciona texto                                                            |
| Alt-SetaEsquerda               | Move o cursor para o início da linha atual                                                 |
| Alt-SetaDireita                | Move para o final da linha atual                                                           |
| Home                           | Move o cursor para o início do texto na linha atual                                        |
| End                            | Move o cursor para o final da linha atual                                                  |
| Ctrl-SetaEsquerda              | Move o cursor uma palavra à esquerda                                                       |
| Ctrl-SetaDireita               | Move o cursor uma palavra à direita                                                        |
| Alt-{                          | Move o cursor para a linha vazia anterior ou o início do documento                         |
| Alt-}                          | Move o cursor para a próxima linha vazia ou final do documento                             |
| PageUp                         | Move o cursor para cima em uma página                                                      |
| PageDown                       | Move o cursor para baixo em uma página                                                     |
| Ctrl-Home ou Ctrl-SetaParaCima | Move o cursor para início do documento                                                     |
| Ctrl-End ou Ctrl-SetaParaBaixo | Move o cursor para o fim do documento                                                      |
| Ctrl-l                         | Pule para uma linha do arquivo (Pede o número da linha no prompt)                          |
| Ctrl-w                         | Alterna entre as divisões na guia atual (Use `> vsplit` ou `> hsplit` para fazer divisões) |

## Abas

| Tecla de atalho | Descrição da função |
| --------------- | ------------------- |
| Ctrl-t          | Abre uma nova guia  |
| Alt-,           | Guia anterior       |
| Alt-.           | Próxima guia        |

## Operações de busca

| Tecla de atalho | Descrição da função                             |
| --------------- | ----------------------------------------------- |
| Ctrl-f          | Busca o termo (Abre o prompt)                   |
| Ctrl-n          | Procura a próxima ocorrência da pesquisa atual  |
| Ctrl-p          | Procura a ocorrência anterior da pesquisa atual |

Nota: `Ctrl-n` e `Ctrl-p` devem ser usados ​​no *buffer* principal, não dentro do *prompt* de pesquisa. Depois de `Ctrl-f`, pressione `Enter` para concluir a pesquisa e, em seguida, você pode usar o `Ctrl-n` e `Ctrl-p` para percorrer as correspondências.

## Operações de arquivo

| Tecla de atalho | Descrição da função                                                        |
| --------------- | -------------------------------------------------------------------------- |
| Ctrl-q          | Fecha o arquivo atual (Sai do `micro` se este for o último arquivo aberto) |
| Ctrl-o          | Abre um arquivo (Solicita o nome do arquivo no *prompt*)                   |
| Ctrl-s          | Salva o arquivo atual                                                      |

## Operações de texto

| Tecla de atalho             | Descrição da função                                     |
| --------------------------- | ------------------------------------------------------- |
| Ctrl-Shift-SetaDireita      | Seleciona uma palavra à direita                         |
| Ctrl-Shift-SetaEsquerda     | Seleciona uma palavra à esquerda                        |
| Alt-Shift-SetaEsquerda      | Seleciona até o início da linha atual                   |
| Alt-Shift-SetaDireita       | Seleciona até o fim da linha atual                      |
| Shift-Home                  | Seleciona até o início do arquivo atual                 |
| Shift-End                   | Seleciona até o fim da linha atual                      |
| Ctrl-Shift-SetaParaCima     | Seleciona até o início do arquivo atual                 |
| Ctrl-Shift-SetaParaBaixo    | Seleciona até o fim do arquivo                          |
| Ctrl-x                      | Recorta o texto selecionado                             |
| Ctrl-c                      | Copia o texto selecionado                               |
| Ctrl-v                      | Cola                                                    |
| Ctrl-k                      | Recorta a linha atual                                   |
| Ctrl-d                      | Duplica a linha atual                                   |
| Ctrl-z                      | Desfaz                                                  |
| Ctrl-y                      | Refaz                                                   |
| Alt-SetaParaCima            | Move para cima a linha atual ou as linhas selecionadas  |
| Alt-SetaParaBaixo           | Move para baixo a linha atual ou as linhas selecionadas |
| Alt-Backspace or Alt-Ctrl-h | Apaga uma palavra à esquerda                            |
| Ctrl-a                      | Seleciona todo o texto                                  |
| Tab                         | Endenta o texto selecionado (Aumenta o recuo)           |
| Shift-Tab                   | Desendenta o texto selecionado (Diminui o recuo)        |

## Macros

| Tecla de atalho | Descrição da função                                                                                  |
| --------------- | ---------------------------------------------------------------------------------------------------- |
| Ctrl-u          | Alterna para o modo de gravação de macro (Pressione Ctrl-u para iniciar e para finalizar a gravação) |
| Ctrl-j          | Execute a macro mais recente gravada                                                                 |

## Múltiplos cursores

| Tecla de atalho | Descrição da função                                                                                           |
| --------------- | ------------------------------------------------------------------------------------------------------------- |
| Alt-n           | Cria múltiplos cursores a partir da seleção (Selecionará a palavra atual se não houver nenhuma seleção atual) |
| Alt-Shift-Cima  | Acrescenta um novo cursor na linha acima da atual                                                             |
| Alt-Shift-Baixo | Acrescenta um novo cursor na linha abaixo da atual                                                            |
| Alt-p           | Remove o último cursores múltiplos                                                                            |
| Alt-c           | Remove todos os múltiplos cursores (Cancela)                                                                  |
| Alt-x           | Pula a seleção de múltiplos cursores                                                                          |
| Alt-m           | Gera um novo cursor no início de todas as linhas da seleção atual                                             |
| Ctrl-MouseEsq   | Coloca um cursor múltiplo em qualquer local                                                                   |

## Outras

| Tecla de atalho | Descrição da função                                                                         |
| --------------- | ------------------------------------------------------------------------------------------- |
| Ctrl-g          | Abre o arquivo de ajuda                                                                     |
| Ctrl-h          | Backspace (Terminais antigos não suportam a tecla *Backspace* e usam `Ctrl+H` em vez disso) |
| Ctrl-r          | Exibir ou esconder o número das linhas                                                      |

## Ações ao estilo do Emacs

| Tecla de atalho | Descrição da função         |
| --------------- | --------------------------- |
| Alt-f           | Próxima palavra             |
| Alt-b           | Palavra anterior            |
| Alt-a           | Move para o início da linha |
| Alt-e           | Mover para o final da linha |

## Teclas de função

Aviso! As teclas de função podem não funcionar em todos os terminais!

| Tecla de atalho | Descrição da função |
| --------------- | ------------------- |
| F1              | Ajuda               |
| F2              | Salvar              |
| F3              | Pesquisar           |
| F4              | Sair                |
| F7              | Pesquisar           |
| F10             | Sair                |
