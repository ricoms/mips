# Compiladores
#### aluno: Ricardo Manhães Savii - 92482
------------------


O analisador léxico está contido no arquivo **cminus_lexer.py** para testa-lo basta chamar o comando abaixo substituindo \<arquivo\> pelo endereço do código à ser analisado.

```
python3 cminus_lexer.py <arquivo>
```

Já o analisador sintático está contido no arquivo **cminus_parser.py** onde está a gramática utilizada. A gramática utilizada é diferente à apresentada em aula pois a gramática dada em aula entrava em recursão infinita, acredito que devido à ordem de análise ser diferente.

Para suporte do compilador utilizei a versão python do lex e yacc chamada PLY. PLY é composto pelos arquivos **ply/lex.py** e **ply/yacc.py**. Estes arquivos contém diversas classes que fornecem a funcionalidade bem semelhante aos mesmos pacotes implementados em C, porém percebi que a ordem de análise é diferente.

Dentro da pasta **ply** há outros arquivos que implementam processadores léxicos de outras linguagens, os utilizei junto o manual do ply (http://www.dabeaz.com/ply/) para entender como utilizar o PLY.




