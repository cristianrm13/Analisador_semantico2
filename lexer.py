import ply.lex as lex

reserved = {
    'VAR': 'VAR',
    'FOR': 'FOR',
    'CONSOLE': 'CONSOLE',
    'LOG': 'LOG',
    'GLOBAL': 'GLOBAL',
    'INT': 'INT',
    'OUT': 'OUT',
    'PRINTLN': 'PRINTLN',
    'SYSTEM': 'SYSTEM',
    'IF': 'IF',
    'DO': 'DO',
    'ENDDO': 'ENDDO',
    'WHILE': 'WHILE',
    'ENDWHILE': 'ENDWHILE',
    'FLOAT': 'FLOAT',
    'STRING': 'STRING',
    'INPUT': 'INPUT',
    'AND': 'AND',
    'IN': 'IN',
    'RANGE': 'RANGE'
}

tokens = [
    'ID', 'NUMBER', 'NUMBER_2', 'NUMBER_3', 'FLOAT_LITERAL', 'STRING_LITERAL', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGN',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMICOLON', 'COMMA', 'LT', 'LE',
    'GT', 'GE', 'EQ', 'NE', 'DOT', 'SINGLE_QUOTE'
] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_COMMA = r','
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='
t_DOT = r'\.'
t_SINGLE_QUOTE = r"\'"

def t_FLOAT_LITERAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_STRING_LITERAL(t):
    r'"[^"]*"'
    t.value = t.value.strip('"')
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value.upper(), 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NUMBER_2(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NUMBER_3(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print(f"Línea {t.lineno}.- Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
