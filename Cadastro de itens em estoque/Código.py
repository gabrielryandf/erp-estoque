from database import cur, con

def cadastrar_produto():
    print("\n--- Cadastro de Novo Produto ---")

    nome = input("Nome: ")
    categoria = input("Categoria: ")
    unidade = input("Unidade (UN, KG, LT): ").upper()  
    
