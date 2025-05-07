import re

# Step 1: Tokenizer (Lexer)
token_specification = [
    ('NUMBER',   r'\d+'),       # Integer
    ('PLUS',     r'\+'),        # Addition
    ('TIMES',    r'\*'),        # Multiplication
    ('LPAREN',   r'\('),        # Left Parenthesis
    ('RPAREN',   r'\)'),        # Right Parenthesis
    ('SKIP',     r'[ \t\n]+'),  # Skip spaces, tabs, newlines
    ('MISMATCH', r'.'),         # Any other character
]

# Create a regex for the token types
tok_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
get_token = re.compile(tok_regex).match

# Step 2: Lexer - Convert input string to tokens
def lexer(code):
    line_num = 1
    line_start = 0
    position = 0
    tokens = []
    
    while position < len(code):
        match = get_token(code, position)
        if match:
            type_ = match.lastgroup
            value = match.group(type_)
            if type_ == 'SKIP':
                pass
            elif type_ == 'MISMATCH':
                raise RuntimeError(f'Unexpected character {value!r} at position {position}')
            else:
                tokens.append((type_, value))
            position = match.end()
        else:
            raise RuntimeError(f'Unexpected character {code[position]!r} at position {position}')
    
    return tokens

# Step 3: Parser - Convert tokens into an abstract syntax tree (AST)
class ASTNode:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def __repr__(self):
        return f'{self.value}'

def parse_expression(tokens):
    # Parse the expression: term ((PLUS | TIMES) term)*
    def parse_term(tokens):
        token = tokens.pop(0)
        if token[0] == 'NUMBER':
            return ASTNode(int(token[1]))
        elif token[0] == 'LPAREN':
            expr = parse_expr(tokens)
            if tokens.pop(0)[0] != 'RPAREN':
                raise SyntaxError("Expected ')'")
            return expr
        else:
            raise SyntaxError(f'Unexpected token: {token}')
    
    def parse_factor(tokens):
        # Here we would expand for multiplication or division
        left = parse_term(tokens)
        while tokens and tokens[0][0] in ('TIMES'):
            token = tokens.pop(0)
            right = parse_term(tokens)
            new_node = ASTNode(token[1])
            new_node.children.extend([left, right])
            left = new_node
        return left
    
    def parse_expr(tokens):
        # Expression is factors and terms joined by addition or subtraction
        left = parse_factor(tokens)
        while tokens and tokens[0][0] in ('PLUS'):
            token = tokens.pop(0)
            right = parse_factor(tokens)
            new_node = ASTNode(token[1])
            new_node.children.extend([left, right])
            left = new_node
        return left
    
    return parse_expr(tokens)

# Step 4: Evaluation of the AST
def evaluate_ast(ast):
    if ast.value == '+':
        return evaluate_ast(ast.children[0]) + evaluate_ast(ast.children[1])
    elif ast.value == '*':
        return evaluate_ast(ast.children[0]) * evaluate_ast(ast.children[1])
    else:  # It is a number node
        return ast.value

# Step 5: Putting everything together
def compile_and_run(code):
    tokens = lexer(code)
    ast = parse_expression(tokens)
    result = evaluate_ast(ast)
    return result

# Example Usage
source_code = "3 + 4 * 2"
result = compile_and_run(source_code)
print(f"Result: {result}")
