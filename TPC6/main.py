import ply.lex as lexer


tokens = (
    'NUM',
    'VAR',
    'TYPE',
    'SIMB',
    'SIMBC',
    'ARRAY',
    'CONJNUM',
    'FUNCTION',
    'WHILE',
    'FOR',
    'IF',
    'PRINT',
    'PROGRAM',
    'OPENCHAV',
    'CLOSECHAV',
    'OPENPARC',
    'CLOSEPARC',
    'OPENPARR',
    'CLOSEPARR',
    'EQUALS',
    'SEP',
    'IN',
    'CONJ',
    'COMMENT',
    'ARRAYVAR'
)

# Regular expression rules for simple tokens
t_ARRAY = r'\w+\[\d+\]'
t_ARRAYVAR = r'\w+\[\w+\]'
t_COMMENT = r'[\/\*|\-\-|\*\/|\/\/]'
t_CONJ = r'\[\d+\.\.\d+\]'
t_CONJNUM = r'\{[\d,]+\}'
t_OPENPARR    = r'\['
t_CLOSEPARR   = r'\]'
t_OPENPARC    = r'\('
t_CLOSEPARC   = r'\)'
t_OPENCHAV    = r'\{'
t_CLOSECHAV   = r'\}'
t_SEP   = r','
t_TYPE = r'int|double|string|float'
t_SIMB = r'[\+\-\*\/\%]'
t_SIMBC = r'[\>\<(\<\=)(\>\=)(\=\=)(\!\=)]'
t_EQUALS = r'\='
t_FUNCTION = r'function'
t_PROGRAM = r'program'
t_IF = r'if '
t_WHILE = r'while'
t_FOR = r'for'
t_IN = r'\bin\b'
t_PRINT = r'print'
t_VAR = r'\w+'

# A regular expression rule with some action code
def t_NUM(t):
    r'[+\-]\d+'
    t.value = int(t.value)    
    return t

# Ignorar espaços em branco e tabulações
t_ignore = ' \t\n;.:'

# Tratamento de erros
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lexer.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lexer.lex()
# lexer.input(data)

flag = False
with open("factorial.p", "r") as f:
    for line in f:
        if flag==False and line != "\n":
            lexer.input(line)
            lexer.variables = list()
            while tok := lexer.token():
                if tok.type == 'COMMENT':
                    flag=True
                if flag==False:
                    print(tok.type, end=" ")
            if flag==False:
                print(" ")
        flag = False
