import ply.yacc as yacc
from cminus_lexer import tokens
import cminus_lexer
import sys

VERBOSE = 1

def p_program(p):
    'program : declaration_list'
    pass

def p_declaration_list(p):
    '''declaration_list : declaration_list declaration
        | declaration'''
    #p[0] = p[1] + p[2]
    pass

def p_declaration(p):
    '''declaration : var_declaration
        | fun_declaration'''

def p_var_declaration(p):
    '''var_declaration : type_specifier ID SEMICOLON
        | type_specifier ID LBRACKET NUMBER RBRACKET SEMICOLON'''
    pass

def p_type_specifier(p):
    '''type_specifier : INT
        | VOID'''
    pass

def p_fun_declaration(p):
    'fun_declaration : type_specifier ID LPAREN params RPAREN compound_stmt'
    pass

def p_params(p):
    '''params : param_list
        | VOID'''
    pass

def p_param_list(p):
    '''param_list : param_list COMMA param
        | param
        | empty'''
    pass

def p_param(p):
    '''param : type_specifier ID
        | type_specifier ID LBRACKET RBRACKET'''
    pass

def p_compound_stmt(p):
    'compound_stmt : LBRACE local_declarations statement_list RBRACE'
    pass

def p_local_declarations(p):
    '''local_declarations : local_declarations var_declaration
        | empty'''
    pass

def p_statement_list(p):
    '''statement_list : statement_list statement
        | empty'''
    pass

def p_statement(p):
    '''statement : expression_stmt
        | compound_stmt
        | selection_stmt
        | iteration_stmt
        | return_stmt
    '''
    pass

def p_expression_stmt(p):
    '''expression_stmt : expression SEMICOLON
        | SEMICOLON'''
    pass
########
def p_selection_stmt(p):
    '''selection_stmt : IF LPAREN expression RPAREN statement
        | IF LPAREN expression RPAREN statement ELSE statement'''
    pass

def p_iteration_stmt(p):
    'iteration_stmt : WHILE LPAREN expression RPAREN statement'
    pass

def p_return_stmt(p):
    '''return_stmt : RETURN SEMICOLON
        | RETURN expression SEMICOLON'''
    pass

def p_expression(p):
    '''expression : var ASSIGN expression
        | simple_expression'''
    pass

def p_var(p):
    '''var : ID
        | ID LBRACKET expression RBRACKET'''
    pass

def p_simple_expression(p):
    '''simple_expression : additive_expression relop additive_expression
        | additive_expression'''
    pass

def p_relop(p):
    '''relop : LESS
        | LESSEQUAL
        | GREATER
        | GREATEREQUAL
        | EQUAL
        | NEQUAL
    '''
    pass

def p_additive_expression(p):
    '''additive_expression : additive_expression addop term
        | term'''
    pass

def p_addop(p):
    ''' addop : PLUS
        | MINUS
    '''
    pass

def p_term(p):
    '''term : term mulop factor
        | factor'''
    pass

def p_mulop(p):
    ''' mulop : TIMES
        | DIVIDE
    '''
    pass

def p_factor(p):
    '''factor : LPAREN expression RPAREN
        | var
        | call
        | NUMBER'''
    pass

def p_call(p):
    'call : ID LPAREN args RPAREN'
    pass

def p_args(p):
    ''' args : args_list
        | empty
    '''
    pass

def p_args_list(p):
    '''args_list : args_list COMMA expression
        | expression'''
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    #print( str(dir(p)) )
    #print( str(dir(cminus_lexer)) )
    if VERBOSE:
        if p is not None:
            print("Syntax error at line " + str(p.lexer.lineno) + " Unexpected token " + str(p.value))
        else:
            print("Syntax error at line: " + str(cminus_lexer.lexer.lineno))
    else:
        raise Exception('syntax', 'error')

parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'examples/gcd.c'

	f = open(fin, 'r')
	data = f.read()
	print(data)
	parser.parse(data, tracking=True)
