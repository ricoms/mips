import sys
sys.path.insert(0,"../")
import ply.lex as lex


 # Reserved words
reserved = (
    'INT','STRING','BOOL','VOID','ELSE','IF','WHILE','RETURN','WRITE','READ',
    'TRUE','FALSE','FOR','BREAK'
    )
tokens = reserved + (
    # Operators(=,+,-,*,/,%,<,>,<=,>=,==,!=)
    'ASSIGN','PLUS','MINUS','TIMES','DIV','MOD','LT','GT','NGT','NLT','EQ','NEQ',
    # Operators(||,&&,!,+=,-=,*=,/=,%=)
    'OR','AND','NOT','SIGN','PLUSASG','MINUSASG','TIMESASG','DIVASG','MODASG',
    # Special characters((,),{,},[,],,,;,?,:)
    'LPAREN','RPAREN','LBRACE','RBRACE','LBRACKET','RBRACKET','COMMA','SEMI','TERNARYIF', 'TERNARYIFNOT',
    # Complex tokens
    'ID','NUM','CHAIN'
    #
    )

# Regular expressions rules for simple tokens
## Operators
t_ASSIGN    = r'='
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIV       = r'/'
t_MOD       = r'%'
t_LT        = r'<'
t_GT        = r'>'
t_NGT       = r'<='
t_NLT       = r'>='
t_EQ        = r'=='
t_NEQ       = r'!='
t_OR        = r'\|\|'
t_AND       = r'&&'
t_NOT       = r'!'
t_SIGN      = r'-'
t_PLUSASG   = r'\+='
t_MINUSASG  = r'-='
t_TIMESASG  = r'\*='
t_DIVASG    = r'/='
t_MODASG    = r'%='

## Special characters
t_LPAREN       = r'\('
t_RPAREN       = r'\)'
t_LBRACE       = r'\{'
t_RBRACE       = r'\}'
t_LBRACKET     = r'\['
t_RBRACKET     = r'\]'
t_COMMA        = r','
t_SEMI         = r';'
t_TERNARYIF    = r'\?'
t_TERNARYIFNOT = r':'
t_CHAIN        = r'\"(\n|.)*?\"'

# ignore whitepace,newline,comments
def t_WHITESPACE(t):
    r'[ \t]+'

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_COMMENT(t):
    r' /\*(.|\n)*?\*/'
    t.lineno += t.value.count('\n')

def t_COMMENT_MULTILINE(t):
    r'((//.*)|(/\*(.|\n)*\*/))'
    # No return value. Token discarded
    t.lineno += t.value.count('\n')

# Identifiers and reserved words
reserved_map = { }
for r in reserved:
    reserved_map[r.lower()] = r

def t_ID(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved_map.get(t.value,"ID")
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

# error handle
def t_error(t):
    print("Illegal character %s" % repr(t.value[0]))
    t.lexer.skip(1)


def run_lexer():
    """A debugging function that prints out a list of tokens."""
    if (len(sys.argv)==2):
      with open(sys.argv[1]) as file:
        strings = file.read()
    else:
      print("Usage: lexer.py <file>")
      sys.exit(1)

    lex.input(strings)
    while 1:
        token = lex.token()
        if not token: break
        print("(%s,'%s',%d)" % (token.type, token.value, token.lineno))

lex.lex()

if __name__ == '__main__':
    run_lexer()

