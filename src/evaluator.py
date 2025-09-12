def eval_ast(node):
    #Evaluate AST recursively.
    if node[0] == "NUM":
        return node[1]
    elif node[0] == "PLUS":
        return eval_ast(node[1]) + eval_ast(node[2])
    elif node[0] == "MINUS":
        return eval_ast(node[1]) - eval_ast(node[2])
    elif node[0] == "MUL":
        return eval_ast(node[1]) * eval_ast(node[2])
    elif node[0] == "DIV":
        return eval_ast(node[1]) / eval_ast(node[2])
    else:
        raise RuntimeError(f"Unknown node {node}")