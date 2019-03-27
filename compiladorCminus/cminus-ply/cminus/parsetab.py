
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightTERNARYIFleftORleftANDleftEQNEQleftGTNLTLTNGTleftPLUSMINUSleftTIMESDIVrightNOTSIGNINT STRING BOOL VOID ELSE IF WHILE RETURN WRITE READ TRUE FALSE FOR BREAK ASSIGN PLUS MINUS TIMES DIV MOD LT GT NGT NLT EQ NEQ OR AND NOT SIGN PLUSASG MINUSASG TIMESASG DIVASG MODASG LPAREN RPAREN LBRACE RBRACE LBRACKET RBRACKET COMMA SEMI TERNARYIF TERNARYIFNOT ID NUM CHAINprogram : declaration_seq\n    declaration_seq : declaration declaration_seq\n           | declaration\n    declaration : var_declaration\n        | ID LPAREN param_list RPAREN LBRACE compound_stmt RBRACE\n        | type_specifier ID LPAREN param_list RPAREN LBRACE compound_stmt RBRACEvar_declaration : type_specifier var_spec_seq SEMI\n    var_specifier : ID\n            | ID ASSIGN literal\n            | ID LBRACKET NUM RBRACKET\n            | ID LBRACKET NUM RBRACKET ASSIGN LBRACKET literal_seq RBRACKET\n    type_specifier : INT\n        | STRING\n        | BOOL\n        | VOIDparam : type_specifier ID\n        | type_specifier ID LBRACKET RBRACKETcompound_stmt : var_declaration_list statement_liststatement : if_stmt\n        | while_stmt\n        | for_stmt\n        | break_stmt SEMI\n        | return_stmt SEMI\n        | read_stmt SEMI\n        | write_stmt SEMI\n        | assign SEMI\n        | sub_call SEMI\n    if_stmt : IF LPAREN expression RPAREN statement\n        | IF LPAREN expression RPAREN statement ELSE statement\n        | IF LPAREN expression RPAREN LBRACE compound_stmt RBRACE\n        | IF LPAREN expression RPAREN LBRACE compound_stmt RBRACE ELSE LBRACE compound_stmt RBRACE while_stmt : WHILE LPAREN expression RPAREN LBRACE compound_stmt RBRACE for_stmt : FOR LPAREN assign SEMI expression SEMI assign RPAREN LBRACE compound_stmt RBRACEbreak_stmt : BREAKread_stmt : READ variablewrite_stmt : WRITE expression_list\n    return_stmt : RETURN\n               | RETURN expression\n    sub_call : ID LPAREN expression_list RPAREN\n    assign : variable ASSIGN expression\n           | variable PLUSASG expression\n           | variable MINUSASG expression\n           | variable TIMESASG expression\n           | variable DIVASG expression\n           | variable MODASG expression\n    variable : ID\n        | ID LBRACKET expression RBRACKET\n    expression : expression PLUS expression\n        | expression MINUS expression\n        | expression TIMES expression\n        | expression DIV expression\n        | expression MOD expression\n        | expression EQ expression\n        | expression NEQ expression\n        | expression NGT expression\n        | expression NLT expression\n        | expression GT expression\n        | expression LT expression\n        | expression AND expression\n        | expression OR expression\n        | NOT expression\n        | SIGN expression\n        | expression TERNARYIF expression TERNARYIFNOT expression\n        | sub_call\n        | variable\n        | literal\n        | LPAREN expression RPAREN\n        | param\n    \n    literal : NUM\n            | CHAIN\n            | TRUE\n            | FALSE\n    param_list : param_seq\n        | VOID\n        | empty\n    param_seq : param COMMA param_seq\n             | param\n    \n    var_declaration_list : var_declaration var_declaration_list\n               | empty\n    \n    var_spec_seq : var_specifier COMMA var_spec_seq\n               | var_specifier\n    \n    expression_list : expression_seq\n            | empty\n    \n    literal_seq : literal COMMA literal_seq\n               | literal\n    statement_list : statement statement_list\n        | empty\n    expression_seq : expression COMMA expression_seq\n           | expression\n    empty :'
    
_lr_action_items = {'ID':([0,3,4,6,7,8,9,10,18,21,25,26,39,45,46,47,48,50,52,54,56,57,58,69,70,72,74,78,79,80,81,82,83,84,85,86,88,89,93,97,98,99,100,101,102,107,108,109,115,116,117,118,119,120,121,122,123,124,125,126,127,128,138,143,145,165,166,167,169,170,173,175,176,177,181,182,185,186,],[5,5,-4,13,-12,-13,-14,-15,-15,29,-7,38,-90,73,-90,-79,38,-90,-5,73,-19,-20,-21,73,96,73,-78,-22,-23,-24,-25,-26,-27,73,73,96,73,73,73,73,73,73,73,73,73,73,73,-6,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,-28,-90,-90,73,73,96,-29,-30,-32,-90,-90,-31,-33,]),'INT':([0,3,4,12,22,25,28,39,46,50,52,69,72,84,85,88,89,93,97,98,99,100,101,102,107,108,109,115,116,117,118,119,120,121,122,123,124,125,126,127,128,138,145,166,167,169,181,182,],[7,7,-4,7,7,-7,7,7,7,7,-5,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,-6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'STRING':([0,3,4,12,22,25,28,39,46,50,52,69,72,84,85,88,89,93,97,98,99,100,101,102,107,108,109,115,116,117,118,119,120,121,122,123,124,125,126,127,128,138,145,166,167,169,181,182,],[8,8,-4,8,8,-7,8,8,8,8,-5,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,-6,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'BOOL':([0,3,4,12,22,25,28,39,46,50,52,69,72,84,85,88,89,93,97,98,99,100,101,102,107,108,109,115,116,117,118,119,120,121,122,123,124,125,126,127,128,138,145,166,167,169,181,182,],[9,9,-4,9,9,-7,9,9,9,9,-5,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,-6,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'VOID':([0,3,4,12,22,25,28,39,46,50,52,69,72,84,85,88,89,93,97,98,99,100,101,102,107,108,109,115,116,117,118,119,120,121,122,123,124,125,126,127,128,138,145,166,167,169,181,182,],[10,10,-4,18,18,-7,10,10,10,10,-5,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,-6,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'$end':([1,2,3,4,11,25,52,109,],[0,-1,-3,-4,-2,-7,-5,-6,]),'LPAREN':([5,13,65,66,67,69,72,73,84,85,88,89,93,97,98,99,100,101,102,107,108,115,116,117,118,119,120,121,122,123,124,125,126,127,128,138,145,169,],[12,22,84,85,86,93,93,107,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,]),'RPAREN':([12,16,17,18,19,20,22,29,30,32,33,34,35,40,49,73,90,91,92,94,104,105,106,107,112,113,129,130,131,132,133,134,135,136,137,139,146,147,148,149,150,151,152,153,154,155,156,157,158,160,161,162,163,174,178,],[-90,27,-73,-74,-75,-77,-90,-16,42,-69,-70,-71,-72,-76,-17,-46,-64,-65,-66,-68,-82,-83,-89,-90,143,144,-61,-62,160,-40,-41,-42,-43,-44,-45,162,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-67,-88,-39,-47,-63,180,]),'COMMA':([13,15,20,29,31,32,33,34,35,38,43,49,73,90,91,92,94,106,111,129,130,141,146,147,148,149,150,151,152,153,154,155,156,157,158,160,162,163,174,],[-8,26,28,-16,-9,-69,-70,-71,-72,-8,-10,-17,-46,-64,-65,-66,-68,138,142,-61,-62,-11,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-67,-39,-47,-63,]),'SEMI':([13,14,15,29,31,32,33,34,35,37,38,43,49,59,60,61,62,63,64,68,69,72,73,87,90,91,92,94,95,96,103,104,105,106,114,129,130,132,133,134,135,136,137,141,146,147,148,149,150,151,152,153,154,155,156,157,158,160,161,162,163,168,174,],[-8,25,-81,-16,-9,-69,-70,-71,-72,-80,-8,-10,-17,78,79,80,81,82,83,-34,-37,-90,-46,-38,-64,-65,-66,-68,-35,-46,-36,-82,-83,-89,145,-61,-62,-40,-41,-42,-43,-44,-45,-11,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-67,-88,-39,-47,173,-63,]),'ASSIGN':([13,38,43,71,73,96,163,],[23,23,51,97,-46,-46,-47,]),'LBRACKET':([13,29,38,51,73,96,],[24,41,24,76,108,108,]),'NUM':([23,24,69,72,76,84,85,88,89,93,97,98,99,100,101,102,107,108,115,116,117,118,119,120,121,122,123,124,125,126,127,128,138,142,145,169,],[32,36,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'CHAIN':([23,69,72,76,84,85,88,89,93,97,98,99,100,101,102,107,108,115,116,117,118,119,120,121,122,123,124,125,126,127,128,138,142,145,169,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'TRUE':([23,69,72,76,84,85,88,89,93,97,98,99,100,101,102,107,108,115,116,117,118,119,120,121,122,123,124,125,126,127,128,138,142,145,169,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'FALSE':([23,69,72,76,84,85,88,89,93,97,98,99,100,101,102,107,108,115,116,117,118,119,120,121,122,123,124,125,126,127,128,138,142,145,169,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'IF':([25,39,45,46,47,50,54,56,57,58,74,78,79,80,81,82,83,143,165,166,167,170,175,176,177,181,182,185,186,],[-7,-90,65,-90,-79,-90,65,-19,-20,-21,-78,-22,-23,-24,-25,-26,-27,65,-28,-90,-90,65,-29,-30,-32,-90,-90,-31,-33,]),'WHILE':([25,39,45,46,47,50,54,56,57,58,74,78,79,80,81,82,83,143,165,166,167,170,175,176,177,181,182,185,186,],[-7,-90,66,-90,-79,-90,66,-19,-20,-21,-78,-22,-23,-24,-25,-26,-27,66,-28,-90,-90,66,-29,-30,-32,-90,-90,-31,-33,]),'FOR':([25,39,45,46,47,50,54,56,57,58,74,78,79,80,81,82,83,143,165,166,167,170,175,176,177,181,182,185,186,],[-7,-90,67,-90,-79,-90,67,-19,-20,-21,-78,-22,-23,-24,-25,-26,-27,67,-28,-90,-90,67,-29,-30,-32,-90,-90,-31,-33,]),'BREAK':([25,39,45,46,47,50,54,56,57,58,74,78,79,80,81,82,83,143,165,166,167,170,175,176,177,181,182,185,186,],[-7,-90,68,-90,-79,-90,68,-19,-20,-21,-78,-22,-23,-24,-25,-26,-27,68,-28,-90,-90,68,-29,-30,-32,-90,-90,-31,-33,]),'RETURN':([25,39,45,46,47,50,54,56,57,58,74,78,79,80,81,82,83,143,165,166,167,170,175,176,177,181,182,185,186,],[-7,-90,69,-90,-79,-90,69,-19,-20,-21,-78,-22,-23,-24,-25,-26,-27,69,-28,-90,-90,69,-29,-30,-32,-90,-90,-31,-33,]),'READ':([25,39,45,46,47,50,54,56,57,58,74,78,79,80,81,82,83,143,165,166,167,170,175,176,177,181,182,185,186,],[-7,-90,70,-90,-79,-90,70,-19,-20,-21,-78,-22,-23,-24,-25,-26,-27,70,-28,-90,-90,70,-29,-30,-32,-90,-90,-31,-33,]),'WRITE':([25,39,45,46,47,50,54,56,57,58,74,78,79,80,81,82,83,143,165,166,167,170,175,176,177,181,182,185,186,],[-7,-90,72,-90,-79,-90,72,-19,-20,-21,-78,-22,-23,-24,-25,-26,-27,72,-28,-90,-90,72,-29,-30,-32,-90,-90,-31,-33,]),'RBRACE':([25,39,44,45,46,47,50,53,54,55,56,57,58,74,75,77,78,79,80,81,82,83,165,166,167,171,172,175,176,177,181,182,183,184,185,186,],[-7,-90,52,-90,-90,-79,-90,-18,-90,-87,-19,-20,-21,-78,109,-86,-22,-23,-24,-25,-26,-27,-28,-90,-90,176,177,-29,-30,-32,-90,-90,185,186,-31,-33,]),'LBRACE':([27,42,143,144,179,180,],[39,50,166,167,181,182,]),'PLUS':([29,32,33,34,35,49,73,87,90,91,92,94,106,112,113,129,130,131,132,133,134,135,136,137,140,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,162,163,168,174,],[-16,-69,-70,-71,-72,-17,-46,115,-64,-65,-66,-68,115,115,115,-61,-62,115,115,115,115,115,115,115,115,-48,-49,-50,-51,115,115,115,115,115,115,115,115,115,115,-67,-39,-47,115,115,]),'MINUS':([29,32,33,34,35,49,73,87,90,91,92,94,106,112,113,129,130,131,132,133,134,135,136,137,140,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,162,163,168,174,],[-16,-69,-70,-71,-72,-17,-46,116,-64,-65,-66,-68,116,116,116,-61,-62,116,116,116,116,116,116,116,116,-48,-49,-50,-51,116,116,116,116,116,116,116,116,116,116,-67,-39,-47,116,116,]),'TIMES':([29,32,33,34,35,49,73,87,90,91,92,94,106,112,113,129,130,131,132,133,134,135,136,137,140,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,162,163,168,174,],[-16,-69,-70,-71,-72,-17,-46,117,-64,-65,-66,-68,117,117,117,-61,-62,117,117,117,117,117,117,117,117,117,117,-50,-51,117,117,117,117,117,117,117,117,117,117,-67,-39,-47,117,117,]),'DIV':([29,32,33,34,35,49,73,87,90,91,92,94,106,112,113,129,130,131,132,133,134,135,136,137,140,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,162,163,168,174,],[-16,-69,-70,-71,-72,-17,-46,118,-64,-65,-66,-68,118,118,118,-61,-62,118,118,118,118,118,118,118,118,118,118,-50,-51,118,118,118,118,118,118,118,118,118,118,-67,-39,-47,118,118,]),'MOD':([29,32,33,34,35,49,73,87,90,91,92,94,106,112,113,129,130,131,132,133,134,135,136,137,140,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,162,163,168,174,],[-16,-69,-70,-71,-72,-17,-46,119,-64,-65,-66,-68,119,119,119,-61,-62,119,119,119,119,119,119,119,119,-48,-49,-50,-51,119,-53,-54,-55,-56,-57,-58,-59,-60,119,-67,-39,-47,119,119,]),'EQ':([29,32,33,34,35,49,73,87,90,91,92,94,106,112,113,129,130,131,132,133,134,135,136,137,140,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,162,163,168,174,],[-16,-69,-70,-71,-72,-17,-46,120,-64,-65,-66,-68,120,120,120,-61,-62,120,120,120,120,120,120,120,120,-48,-49,-50,-51,120,-53,-54,-55,-56,-57,-58,120,120,120,-67,-39,-47,120,120,]),'NEQ':([29,32,33,34,35,49,73,87,90,91,92,94,106,112,113,129,130,131,132,133,134,135,136,137,140,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,162,163,168,174,],[-16,-69,-70,-71,-72,-17,-46,121,-64,-65,-66,-68,121,121,121,-61,-62,121,121,121,121,121,121,121,121,-48,-49,-50,-51,121,-53,-54,-55,-56,-57,-58,121,121,121,-67,-39,-47,121,121,]),'NGT':([29,32,33,34,35,49,73,87,90,91,92,94,106,112,113,129,130,131,132,133,134,135,136,137,140,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,162,163,168,174,],[-16,-69,-70,-71,-72,-17,-46,122,-64,-65,-66,-68,122,122,122,-61,-62,122,122,122,122,122,122,122,122,-48,-49,-50,-51,122,122,122,-55,-56,-57,-58,122,122,122,-67,-39,-47,122,122,]),'NLT':([29,32,33,34,35,49,73,87,90,91,92,94,106,112,113,129,130,131,132,133,134,135,136,137,140,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,162,163,168,174,],[-16,-69,-70,-71,-72,-17,-46,123,-64,-65,-66,-68,123,123,123,-61,-62,123,123,123,123,123,123,123,123,-48,-49,-50,-51,123,123,123,-55,-56,-57,-58,123,123,123,-67,-39,-47,123,123,]),'GT':([29,32,33,34,35,49,73,87,90,91,92,94,106,112,113,129,130,131,132,133,134,135,136,137,140,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,162,163,168,174,],[-16,-69,-70,-71,-72,-17,-46,124,-64,-65,-66,-68,124,124,124,-61,-62,124,124,124,124,124,124,124,124,-48,-49,-50,-51,124,124,124,-55,-56,-57,-58,124,124,124,-67,-39,-47,124,124,]),'LT':([29,32,33,34,35,49,73,87,90,91,92,94,106,112,113,129,130,131,132,133,134,135,136,137,140,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,162,163,168,174,],[-16,-69,-70,-71,-72,-17,-46,125,-64,-65,-66,-68,125,125,125,-61,-62,125,125,125,125,125,125,125,125,-48,-49,-50,-51,125,125,125,-55,-56,-57,-58,125,125,125,-67,-39,-47,125,125,]),'AND':([29,32,33,34,35,49,73,87,90,91,92,94,106,112,113,129,130,131,132,133,134,135,136,137,140,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,162,163,168,174,],[-16,-69,-70,-71,-72,-17,-46,126,-64,-65,-66,-68,126,126,126,-61,-62,126,126,126,126,126,126,126,126,-48,-49,-50,-51,126,-53,-54,-55,-56,-57,-58,-59,126,126,-67,-39,-47,126,126,]),'OR':([29,32,33,34,35,49,73,87,90,91,92,94,106,112,113,129,130,131,132,133,134,135,136,137,140,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,162,163,168,174,],[-16,-69,-70,-71,-72,-17,-46,127,-64,-65,-66,-68,127,127,127,-61,-62,127,127,127,127,127,127,127,127,-48,-49,-50,-51,127,-53,-54,-55,-56,-57,-58,-59,-60,127,-67,-39,-47,127,127,]),'TERNARYIF':([29,32,33,34,35,49,73,87,90,91,92,94,106,112,113,129,130,131,132,133,134,135,136,137,140,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,162,163,168,174,],[-16,-69,-70,-71,-72,-17,-46,128,-64,-65,-66,-68,128,128,128,-61,-62,128,128,128,128,128,128,128,128,-48,-49,-50,-51,128,-53,-54,-55,-56,-57,-58,-59,-60,128,-67,-39,-47,128,128,]),'RBRACKET':([29,32,33,34,35,36,41,49,73,90,91,92,94,110,111,129,130,140,146,147,148,149,150,151,152,153,154,155,156,157,158,160,162,163,164,174,],[-16,-69,-70,-71,-72,43,49,-17,-46,-64,-65,-66,-68,141,-85,-61,-62,163,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-67,-39,-47,-84,-63,]),'TERNARYIFNOT':([29,32,33,34,35,49,73,90,91,92,94,129,130,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,162,163,174,],[-16,-69,-70,-71,-72,-17,-46,-64,-65,-66,-68,-61,-62,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,169,-67,-39,-47,-63,]),'ELSE':([56,57,58,78,79,80,81,82,83,165,175,176,177,185,186,],[-19,-20,-21,-22,-23,-24,-25,-26,-27,170,-29,179,-32,-31,-33,]),'NOT':([69,72,84,85,88,89,93,97,98,99,100,101,102,107,108,115,116,117,118,119,120,121,122,123,124,125,126,127,128,138,145,169,],[88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,]),'SIGN':([69,72,84,85,88,89,93,97,98,99,100,101,102,107,108,115,116,117,118,119,120,121,122,123,124,125,126,127,128,138,145,169,],[89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,]),'PLUSASG':([71,73,96,163,],[98,-46,-46,-47,]),'MINUSASG':([71,73,96,163,],[99,-46,-46,-47,]),'TIMESASG':([71,73,96,163,],[100,-46,-46,-47,]),'DIVASG':([71,73,96,163,],[101,-46,-46,-47,]),'MODASG':([71,73,96,163,],[102,-46,-46,-47,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declaration_seq':([0,3,],[2,11,]),'declaration':([0,3,],[3,3,]),'var_declaration':([0,3,39,46,50,166,167,181,182,],[4,4,46,46,46,46,46,46,46,]),'type_specifier':([0,3,12,22,28,39,46,50,69,72,84,85,88,89,93,97,98,99,100,101,102,107,108,115,116,117,118,119,120,121,122,123,124,125,126,127,128,138,145,166,167,169,181,182,],[6,6,21,21,21,48,48,48,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,48,48,21,48,48,]),'var_spec_seq':([6,26,48,],[14,37,14,]),'var_specifier':([6,26,48,],[15,15,15,]),'param_list':([12,22,],[16,30,]),'param_seq':([12,22,28,],[17,17,40,]),'empty':([12,22,39,45,46,50,54,72,107,166,167,181,182,],[19,19,47,55,47,47,55,105,105,47,47,47,47,]),'param':([12,22,28,69,72,84,85,88,89,93,97,98,99,100,101,102,107,108,115,116,117,118,119,120,121,122,123,124,125,126,127,128,138,145,169,],[20,20,20,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,]),'literal':([23,69,72,76,84,85,88,89,93,97,98,99,100,101,102,107,108,115,116,117,118,119,120,121,122,123,124,125,126,127,128,138,142,145,169,],[31,92,92,111,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,111,92,92,]),'compound_stmt':([39,50,166,167,181,182,],[44,75,171,172,183,184,]),'var_declaration_list':([39,46,50,166,167,181,182,],[45,74,45,45,45,45,45,]),'statement_list':([45,54,],[53,77,]),'statement':([45,54,143,170,],[54,54,165,175,]),'if_stmt':([45,54,143,170,],[56,56,56,56,]),'while_stmt':([45,54,143,170,],[57,57,57,57,]),'for_stmt':([45,54,143,170,],[58,58,58,58,]),'break_stmt':([45,54,143,170,],[59,59,59,59,]),'return_stmt':([45,54,143,170,],[60,60,60,60,]),'read_stmt':([45,54,143,170,],[61,61,61,61,]),'write_stmt':([45,54,143,170,],[62,62,62,62,]),'assign':([45,54,86,143,170,173,],[63,63,114,63,63,178,]),'sub_call':([45,54,69,72,84,85,88,89,93,97,98,99,100,101,102,107,108,115,116,117,118,119,120,121,122,123,124,125,126,127,128,138,143,145,169,170,],[64,64,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,64,90,90,64,]),'variable':([45,54,69,70,72,84,85,86,88,89,93,97,98,99,100,101,102,107,108,115,116,117,118,119,120,121,122,123,124,125,126,127,128,138,143,145,169,170,173,],[71,71,91,95,91,91,91,71,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,71,91,91,71,71,]),'expression':([69,72,84,85,88,89,93,97,98,99,100,101,102,107,108,115,116,117,118,119,120,121,122,123,124,125,126,127,128,138,145,169,],[87,106,112,113,129,130,131,132,133,134,135,136,137,106,140,146,147,148,149,150,151,152,153,154,155,156,157,158,159,106,168,174,]),'expression_list':([72,107,],[103,139,]),'expression_seq':([72,107,138,],[104,104,161,]),'literal_seq':([76,142,],[110,164,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declaration_seq','program',1,'p_program','parser.py',25),
  ('declaration_seq -> declaration declaration_seq','declaration_seq',2,'p_declaration_seq','parser.py',31),
  ('declaration_seq -> declaration','declaration_seq',1,'p_declaration_seq','parser.py',32),
  ('declaration -> var_declaration','declaration',1,'p_declaration','parser.py',41),
  ('declaration -> ID LPAREN param_list RPAREN LBRACE compound_stmt RBRACE','declaration',7,'p_declaration','parser.py',42),
  ('declaration -> type_specifier ID LPAREN param_list RPAREN LBRACE compound_stmt RBRACE','declaration',8,'p_declaration','parser.py',43),
  ('var_declaration -> type_specifier var_spec_seq SEMI','var_declaration',3,'p_var_declaration','parser.py',53),
  ('var_specifier -> ID','var_specifier',1,'p_var_specifier','parser.py',62),
  ('var_specifier -> ID ASSIGN literal','var_specifier',3,'p_var_specifier','parser.py',63),
  ('var_specifier -> ID LBRACKET NUM RBRACKET','var_specifier',4,'p_var_specifier','parser.py',64),
  ('var_specifier -> ID LBRACKET NUM RBRACKET ASSIGN LBRACKET literal_seq RBRACKET','var_specifier',8,'p_var_specifier','parser.py',65),
  ('type_specifier -> INT','type_specifier',1,'p_type_specifier','parser.py',78),
  ('type_specifier -> STRING','type_specifier',1,'p_type_specifier','parser.py',79),
  ('type_specifier -> BOOL','type_specifier',1,'p_type_specifier','parser.py',80),
  ('type_specifier -> VOID','type_specifier',1,'p_type_specifier','parser.py',81),
  ('param -> type_specifier ID','param',2,'p_param','parser.py',86),
  ('param -> type_specifier ID LBRACKET RBRACKET','param',4,'p_param','parser.py',87),
  ('compound_stmt -> var_declaration_list statement_list','compound_stmt',2,'p_compound_stmt','parser.py',95),
  ('statement -> if_stmt','statement',1,'p_statement','parser.py',100),
  ('statement -> while_stmt','statement',1,'p_statement','parser.py',101),
  ('statement -> for_stmt','statement',1,'p_statement','parser.py',102),
  ('statement -> break_stmt SEMI','statement',2,'p_statement','parser.py',103),
  ('statement -> return_stmt SEMI','statement',2,'p_statement','parser.py',104),
  ('statement -> read_stmt SEMI','statement',2,'p_statement','parser.py',105),
  ('statement -> write_stmt SEMI','statement',2,'p_statement','parser.py',106),
  ('statement -> assign SEMI','statement',2,'p_statement','parser.py',107),
  ('statement -> sub_call SEMI','statement',2,'p_statement','parser.py',108),
  ('if_stmt -> IF LPAREN expression RPAREN statement','if_stmt',5,'p_if_stmt','parser.py',114),
  ('if_stmt -> IF LPAREN expression RPAREN statement ELSE statement','if_stmt',7,'p_if_stmt','parser.py',115),
  ('if_stmt -> IF LPAREN expression RPAREN LBRACE compound_stmt RBRACE','if_stmt',7,'p_if_stmt','parser.py',116),
  ('if_stmt -> IF LPAREN expression RPAREN LBRACE compound_stmt RBRACE ELSE LBRACE compound_stmt RBRACE','if_stmt',11,'p_if_stmt','parser.py',117),
  ('while_stmt -> WHILE LPAREN expression RPAREN LBRACE compound_stmt RBRACE','while_stmt',7,'p_while_stmt','parser.py',125),
  ('for_stmt -> FOR LPAREN assign SEMI expression SEMI assign RPAREN LBRACE compound_stmt RBRACE','for_stmt',11,'p_for_stmt','parser.py',130),
  ('break_stmt -> BREAK','break_stmt',1,'p_break_stmt','parser.py',135),
  ('read_stmt -> READ variable','read_stmt',2,'p_read_stmt','parser.py',140),
  ('write_stmt -> WRITE expression_list','write_stmt',2,'p_write_stmt','parser.py',145),
  ('return_stmt -> RETURN','return_stmt',1,'p_return_stmt','parser.py',151),
  ('return_stmt -> RETURN expression','return_stmt',2,'p_return_stmt','parser.py',152),
  ('sub_call -> ID LPAREN expression_list RPAREN','sub_call',4,'p_sub_call','parser.py',161),
  ('assign -> variable ASSIGN expression','assign',3,'p_assign','parser.py',167),
  ('assign -> variable PLUSASG expression','assign',3,'p_assign','parser.py',168),
  ('assign -> variable MINUSASG expression','assign',3,'p_assign','parser.py',169),
  ('assign -> variable TIMESASG expression','assign',3,'p_assign','parser.py',170),
  ('assign -> variable DIVASG expression','assign',3,'p_assign','parser.py',171),
  ('assign -> variable MODASG expression','assign',3,'p_assign','parser.py',172),
  ('variable -> ID','variable',1,'p_variable','parser.py',178),
  ('variable -> ID LBRACKET expression RBRACKET','variable',4,'p_variable','parser.py',179),
  ('expression -> expression PLUS expression','expression',3,'p_expression','parser.py',188),
  ('expression -> expression MINUS expression','expression',3,'p_expression','parser.py',189),
  ('expression -> expression TIMES expression','expression',3,'p_expression','parser.py',190),
  ('expression -> expression DIV expression','expression',3,'p_expression','parser.py',191),
  ('expression -> expression MOD expression','expression',3,'p_expression','parser.py',192),
  ('expression -> expression EQ expression','expression',3,'p_expression','parser.py',193),
  ('expression -> expression NEQ expression','expression',3,'p_expression','parser.py',194),
  ('expression -> expression NGT expression','expression',3,'p_expression','parser.py',195),
  ('expression -> expression NLT expression','expression',3,'p_expression','parser.py',196),
  ('expression -> expression GT expression','expression',3,'p_expression','parser.py',197),
  ('expression -> expression LT expression','expression',3,'p_expression','parser.py',198),
  ('expression -> expression AND expression','expression',3,'p_expression','parser.py',199),
  ('expression -> expression OR expression','expression',3,'p_expression','parser.py',200),
  ('expression -> NOT expression','expression',2,'p_expression','parser.py',201),
  ('expression -> SIGN expression','expression',2,'p_expression','parser.py',202),
  ('expression -> expression TERNARYIF expression TERNARYIFNOT expression','expression',5,'p_expression','parser.py',203),
  ('expression -> sub_call','expression',1,'p_expression','parser.py',204),
  ('expression -> variable','expression',1,'p_expression','parser.py',205),
  ('expression -> literal','expression',1,'p_expression','parser.py',206),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression','parser.py',207),
  ('expression -> param','expression',1,'p_expression','parser.py',208),
  ('literal -> NUM','literal',1,'p_literal','parser.py',225),
  ('literal -> CHAIN','literal',1,'p_literal','parser.py',226),
  ('literal -> TRUE','literal',1,'p_literal','parser.py',227),
  ('literal -> FALSE','literal',1,'p_literal','parser.py',228),
  ('param_list -> param_seq','param_list',1,'p_param_list','parser.py',234),
  ('param_list -> VOID','param_list',1,'p_param_list','parser.py',235),
  ('param_list -> empty','param_list',1,'p_param_list','parser.py',236),
  ('param_seq -> param COMMA param_seq','param_seq',3,'p_param_seq','parser.py',242),
  ('param_seq -> param','param_seq',1,'p_param_seq','parser.py',243),
  ('var_declaration_list -> var_declaration var_declaration_list','var_declaration_list',2,'p_var_declaration_list','parser.py',253),
  ('var_declaration_list -> empty','var_declaration_list',1,'p_var_declaration_list','parser.py',254),
  ('var_spec_seq -> var_specifier COMMA var_spec_seq','var_spec_seq',3,'p_var_spec_seq','parser.py',262),
  ('var_spec_seq -> var_specifier','var_spec_seq',1,'p_var_spec_seq','parser.py',263),
  ('expression_list -> expression_seq','expression_list',1,'p_expression_list','parser.py',273),
  ('expression_list -> empty','expression_list',1,'p_expression_list','parser.py',274),
  ('literal_seq -> literal COMMA literal_seq','literal_seq',3,'p_literal_seq','parser.py',282),
  ('literal_seq -> literal','literal_seq',1,'p_literal_seq','parser.py',283),
  ('statement_list -> statement statement_list','statement_list',2,'p_statement_list','parser.py',292),
  ('statement_list -> empty','statement_list',1,'p_statement_list','parser.py',293),
  ('expression_seq -> expression COMMA expression_seq','expression_seq',3,'p_expression_seq','parser.py',300),
  ('expression_seq -> expression','expression_seq',1,'p_expression_seq','parser.py',301),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',310),
]
