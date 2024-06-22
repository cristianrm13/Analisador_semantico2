import ply.yacc as yacc
from lexer import tokens, lexer

defined_variables = {}
initial_values = {}
loop_variables = set()  

def p_program(p):
    '''program : declarations statements'''
    validate_variables()
    p[0] = "La estructura del código es correcta."

def p_declarations(p):
    '''declarations : declarations declaration
                    | declaration'''

def p_declaration(p):
    '''declaration : INT ID ASSIGN NUMBER SEMICOLON
                   | INT ID ASSIGN NUMBER_2 SEMICOLON
                   | INT ID ASSIGN NUMBER_3 SEMICOLON'''
    defined_variables[p[2]] = p[1]
    initial_values[p[2]] = p[4]
def p_statements(p):
    '''statements : statements statement
                  | statement'''

def p_statement(p):
    '''statement : if_loop
                 | while_loop
                 | for_loop
                 | input_statement
                 | increment_statement
                 | assignment_statement'''

def p_if_loop(p):
    '''if_loop : DO statements ENDDO'''

def p_condition(p):
    '''condition : expression AND expression
                 | expression'''
    p[0] = p[1]

def p_expression(p):
    '''expression : simple_expression comparison_operator simple_expression
                  | simple_expression
                  | simple_expression ASSIGN simple_expression comparison_operator simple_expression SEMICOLON'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = (p[2], p[1], p[3])

def p_simple_expression(p):
    '''simple_expression : ID
                         | NUMBER
                         | NUMBER_2
                         | NUMBER_3'''
    if isinstance(p[1], str) and p.slice[1].type == 'ID':
        validate_variable_definition(p[1])
    p[0] = p[1]

def p_comparison_operator(p):
    '''comparison_operator : EQ
                           | GT
                           | GE
                           | LT
                           | LE
                           | PLUS
                           | TIMES
                           | NE'''
    p[0] = p[1]

def p_while_loop(p):
    '''while_loop : WHILE LPAREN condition RPAREN LBRACE statements RBRACE'''

def p_for_loop(p):
    '''for_loop : WHILE LPAREN INT ID comparison_operator NUMBER RPAREN ENDWHILE'''
    loop_variables.add(p[3])
    validate_variable_definition(p[3])
    p[0] = f"For loop con variable {p[3]} en rango ({p[6]}, {p[8]})"

def p_input_statement(p):
    '''input_statement : INPUT LPAREN simple_expression RPAREN SEMICOLON'''
    if not isinstance(p[3], str):
        raise ValueError(f"Error semántico: La función input debe recibir una cadena, encontrado {p[3]}.")

def p_increment_statement(p):
    '''increment_statement : ID PLUS PLUS SEMICOLON'''
    validate_variable_definition(p[1])

def p_assignment_statement(p):
    '''assignment_statement : ID ASSIGN expression SEMICOLON'''
    validate_variable_definition(p[1])
    if p[1] == 'B':
        if p[3] != initial_values['B']:
            raise ValueError(f"Error semántico en línea {p.lineno(1)}: Variable 'B' debe mantener el valor {initial_values['B']}.")

def validate_variable_definition(variable):
    if variable not in defined_variables and variable not in loop_variables:
        raise ValueError(f"Error semántico: Variable '{variable}' no definida correctamente.")

def validate_variables():
    pass

def p_error(p):
    if p:
        error_message = f"Línea {p.lineno}.- Error de sintaxis en '{p.value}'"
        raise SyntaxError(error_message)
    else:
        raise SyntaxError(f"Error de sintaxis al final del archivo en la línea {lexer.lineno}. Falta una llave de cierre o punto y coma.")

parser = yacc.yacc()

def parse_semantic(code):
    global defined_variables, loop_variables, initial_values
    defined_variables = {}
    loop_variables = set()
    initial_values = {}
    lexer.lineno = 1
    try:
        result = parser.parse(code, lexer=lexer)
        return result if result else 'La estructura del código es correcta'
    except (SyntaxError, ValueError) as e:
        raise e

def parse_code(code):
    global defined_variables, loop_variables, initial_values
    defined_variables = {}
    loop_variables = set()
    initial_values = {}
    lexer.lineno = 1
    try:
        result = parser.parse(code, lexer=lexer)
        return result if result else "La estructura del código es correcta."
    except (SyntaxError, ValueError) as e:
        raise e
