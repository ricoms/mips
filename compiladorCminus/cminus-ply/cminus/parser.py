import sys
sys.path.insert(0,"../")
import ply.yacc as yacc
import ply.lex as lex

from lexer import tokens
from semantic import *


lex.lexer.lineno = 1
VERBOSE = 1
precedence = (
    ('right', 'TERNARYIF'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQ', 'NEQ'),
    ('left', 'GT', 'NLT', 'LT', 'NGT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIV'),
    ('right', 'NOT', 'SIGN'),
)


def p_program(p):
    'program : declaration_seq'
    p[0] = Program(dec_seq=p[1])


def p_declaration_seq(p):
    '''
    declaration_seq : declaration declaration_seq
           | declaration
    '''
    if len(p) == 2:
        p[0] = DecSeq(dec=p[1])
    elif len(p) == 3:
        p[0] = DecSeq(dec=p[1], dec_seq=p[2])


def p_declaration(p):
    '''declaration : var_declaration
        | ID LPAREN param_list RPAREN LBRACE compound_stmt RBRACE
        | type_specifier ID LPAREN param_list RPAREN LBRACE compound_stmt RBRACE'''
    if len(p) == 2:
        p[0] = Dec(var_dec=p[1])
    elif len(p) == 6:
        p[0] = Dec(id_=p[1], param_list=p[3], block=p[6])
    elif len(p) == 7:
        p[0] = Dec(type_=p[1], id_=p[2], param_list=p[4], block=p[8])
    

def p_var_declaration(p):
    '''var_declaration : type_specifier var_spec_seq SEMI'''
    p[0] = VarDec(type_=p[1], var_spec_seq=p[2])





def p_var_specifier(p):
    '''
    var_specifier : ID
            | ID ASSIGN literal
            | ID LBRACKET NUM RBRACKET
            | ID LBRACKET NUM RBRACKET ASSIGN LBRACKET literal_seq RBRACKET
    '''
    if len(p) == 2:
        p[0] = VarSpec(id_=p[1])
    elif len(p) == 4:
        p[0] = VarSpec(id_=p[1], literal=p[3])
    elif len(p) == 5:
        p[0] = VarSpec(id_=p[1], number=p[3])
    elif len(p) == 9:
        p[0] = VarSpec(id_=p[1], number=p[3], literal_seq=p[7])


def p_type_specifier(p):
    '''type_specifier : INT
        | STRING
        | BOOL
        | VOID'''
    p[0] = Type(type_=p[1])


def p_param(p):
    '''param : type_specifier ID
        | type_specifier ID LBRACKET RBRACKET'''
    if len(p) == 3:
        p[0] = Param(type_=p[1], id_=p[2], array=False)
    elif len(p) == 5:
        p[0] = Param(type_=p[1], id_=p[2], array=True)


def p_compound_stmt(p):
    'compound_stmt : var_declaration_list statement_list'
    p[0] = Block(var_dec_list=p[1], stmt_list=p[2])


def p_statement(p):
    '''statement : if_stmt
        | while_stmt
        | for_stmt
        | break_stmt SEMI
        | return_stmt SEMI
        | read_stmt SEMI
        | write_stmt SEMI
        | assign SEMI
        | sub_call SEMI
    '''
    p[0] = Stmt(stmt=p[1])


def p_if_stmt(p):
    '''if_stmt : IF LPAREN expression RPAREN statement
        | IF LPAREN expression RPAREN statement ELSE statement
        | IF LPAREN expression RPAREN LBRACE compound_stmt RBRACE
        | IF LPAREN expression RPAREN LBRACE compound_stmt RBRACE ELSE LBRACE compound_stmt RBRACE'''
    if len(p) == 8:
        p[0] = IfStmt(if_=p[1], exp=p[3], block1=p[6])
    if len(p) == 12:
        p[0] = IfStmt(if_=p[1], exp=p[3], block1=p[6], else_=p[7], block2=p[11])


def p_while_stmt(p):
    ''' while_stmt : WHILE LPAREN expression RPAREN LBRACE compound_stmt RBRACE '''
    p[0] = WhileStmt(while_=p[1], exp=p[3], block=p[7])


def p_for_stmt(p):
    '''for_stmt : FOR LPAREN assign SEMI expression SEMI assign RPAREN LBRACE compound_stmt RBRACE'''
    p[0] = ForStmt(for_=p[1], assign1=p[3], exp=p[5], assign2=p[7], block=p[11])


def p_break_stmt(p):
    '''break_stmt : BREAK'''
    p[0] = BreakStmt(break_=p[1])


def p_read_stmt(p):
    '''read_stmt : READ variable'''
    p[0] = ReadStmt(read=p[1], var=p[2])


def p_write_stmt(p):
    '''write_stmt : WRITE expression_list'''
    p[0] = WriteStmt(write=p[1], exp_list=p[2])


def p_return_stmt(p):
    '''
    return_stmt : RETURN
               | RETURN expression
    '''
    if len(p) == 3:
        p[0] = ReturnStmt(return_=p[1])
    if len(p) == 4:
        p[0] = ReturnStmt(return_=p[1], exp=p[2])


def p_sub_call(p):
    '''sub_call : ID LPAREN expression_list RPAREN'''
    p[0] = SubCall(id_=p[1], exp_list=p[3])


def p_assign(p):
    '''
    assign : variable ASSIGN expression
           | variable PLUSASG expression
           | variable MINUSASG expression
           | variable TIMESASG expression
           | variable DIVASG expression
           | variable MODASG expression
    '''
    p[0] = Assign(op=p[2], left=p[1], right=p[3])


def p_variable(p):
    '''variable : ID
        | ID LBRACKET expression RBRACKET'''
    if len(p) == 2:
        p[0] = Variable(id_=p[1])
    else:
        p[0] = Variable(id_=p[1], exp=p[3])


def p_expression(p):
    '''
    expression : expression PLUS expression
        | expression MINUS expression
        | expression TIMES expression
        | expression DIV expression
        | expression MOD expression
        | expression EQ expression
        | expression NEQ expression
        | expression NGT expression
        | expression NLT expression
        | expression GT expression
        | expression LT expression
        | expression AND expression
        | expression OR expression
        | NOT expression
        | SIGN expression
        | expression TERNARYIF expression TERNARYIFNOT expression
        | sub_call
        | variable
        | literal
        | LPAREN expression RPAREN
        | param
    '''
    if len(p) == 4:
        if p[1] == '(':
            p[0] = Exp(op=p[2])
        else:
            p[0] = Exp(op=p[2], left=p[1], right=p[3])
    elif len(p) == 3:
        p[0] = Exp(op=p[1], right=p[2])
    elif len(p) == 2:
        p[0] = Exp(op=p[1])
    elif len(p) == 6:
        p[0] = Exp(op=p[1], left=p[3], right=p[5])


def p_literal(p):
    '''
    literal : NUM
            | CHAIN
            | TRUE
            | FALSE
    '''
    p[0] = Literal(literal=p[1])   


def p_param_list(p):
    '''param_list : param_seq
        | VOID
        | empty'''
    p[0] = ParamList(param_seq=p[1])


def p_param_seq(p):
    '''
    param_seq : param COMMA param_seq
             | param
    '''
    if len(p) == 4:
        p[0] = ParamSeq(param=p[1], param_seq=p[3])
    elif len(p) == 2:
        p[0] = ParamSeq(param=p[1])


def p_var_declaration_list(p):
    '''
    var_declaration_list : var_declaration var_declaration_list
               | empty
    '''
    if p[1]:
        p[0] = VarDecList(var_dec=p[1], var_dec_list=p[2])


def p_var_spec_seq(p):
    '''
    var_spec_seq : var_specifier COMMA var_spec_seq
               | var_specifier
    '''
    if len(p) == 4:
        p[0] = VarSpecSeq(var_spec=p[1], var_spec_seq=p[3])
    elif len(p) == 2:
        p[0] = VarSpecSeq(var_spec=p[1])


def p_expression_list(p):
    '''
    expression_list : expression_seq
            | empty
    '''
    if p[1]:
        p[0] = ExpList(exp_seq=p[1])


def p_literal_seq(p):
    '''
    literal_seq : literal COMMA literal_seq
               | literal
    '''
    if len(p) == 4:
        p[0] = LiteralSeq(literal=p[1], literal_seq=p[3])
    elif len(p) == 2:
        p[0] = LiteralSeq(literal=p[1])


def p_statement_list(p):
    '''statement_list : statement statement_list
        | empty'''
    if p[1]:
        p[0] = StmtList(stmt=p[1], stmt_list=p[2])


def p_expression_seq(p):
    '''
    expression_seq : expression COMMA expression_seq
           | expression
    '''
    if len(p) == 2:
        p[0] = ExpSeq(exp=p[1])
    elif len(p) == 4:
        p[0] = ExpSeq(exp=p[1], exp_seq=p[3])


def p_empty(p):
    'empty :'
    pass


def p_error(p):
    if VERBOSE:
        if p is not None:
            print("Syntax error at line " + str(p.lexer.lineno) + " Unexpected token " + str(p.value))
        else:
            print("Syntax error at line: " + str(cminus_lexer.lexer.lineno))
    else:
        raise Exception('syntax', 'error')


def run_parser():
    if (len(sys.argv)==2):
      with open(sys.argv[1]) as file:
        strings = file.read()
    else:
      print("Usage: parser.py <file>")
      sys.exit(1)

    parser = yacc.yacc()
    parser.parse(strings, tracking=True)


if __name__ == '__main__':
    run_parser()
