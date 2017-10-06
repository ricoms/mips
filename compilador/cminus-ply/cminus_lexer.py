import ply.lex as lex
import sys

# list of tokens
tokens = (
    # Reserve words:
    'ELSE',
    'IF',
    'INT',
    'RETURN',
    'VOID',
    'WHILE',

    # Symbols:
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'EQUAL',
    'NEQUAL',
    'ASSIGN',
    'SEMICOLON',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBRACE',
    'RBRACE',

    # Others:
    'ID',
    'NUMBER',
)

# Regular expressions rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r'='
t_LESS = r'<'
t_GREATER = r'>'
t_SEMICOLON = r';'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'{'
t_RBRACE = r'}'

def t_ELSE(t):
    r'else'
    return t

def t_IF(t):
    r'if'
    return t

def t_INT(t):
    r'int'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_VOID(t):
    r'void'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'\w+(_\d\w)*'
    return t

def t_LESSEQUAL(t):
    r'<='
    return t

def t_GREATEREQUAL(t):
    r'>='
    return t

def t_EQUAL(t):
    r'=='
    return t

def t_NEQUAL(t):
    r'!='
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t\r'

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_comments_C99(t):
    r'//(.)*?\n'
    t.lexer.lineno += 1

def t_error(t):
    print("Lexical eror: " + str(t.value[0]))
    t.lexer.skip(1)

def test(data, lexer):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

lexer = lex.lex()

# test
if __name__ == '__main__':

    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = 'examples/gcd.c'

    f = open(fin, 'r')
    data = f.read()

    # Build lexer and try on
    lexer.input(data)
    test(data, lexer)
