import itertools
import string
import sys
import time

def brute_force(senha_alvo, tamanho_max=3):
    """
    Realiza uma simulação de ataque de força bruta para senhas curtas.
    """
    # Dica 1: Conjunto reduzido de caracteres para execução rápida
    caracteres = string.ascii_lowercase + string.digits
    tentativas = 0
    inicio = time.time()
    
    print(f"\n[+] Iniciando simulação para a senha: '{senha_alvo}'")
    print(f"[+] Caracteres válidos: {caracteres}")
    print(f"[+] Limite configurado: {tamanho_max} caracteres\n")
    
    for tamanho in range(1, tamanho_max + 1):
        # Dica 2: O itertools.product gera combinações em formato de tuplas
        for combinacao in itertools.product(caracteres, repeat=tamanho):
            tentativas += 1
            
            # Dica 3: O método .join() transforma a tupla em uma string única
            palavra_testada = "".join(combinacao)
            
            # Atualiza o progresso na mesma linha do terminal
            sys.stdout.write(f"\r[*] Tentativa #{tentativas} | Testando: {palavra_testada}")
            sys.stdout.flush()
            
            if palavra_testada == senha_alvo:
                tempo_total = time.time() - inicio
                print(f"\n\n[✓] SENHA ENCONTRADA COM SUCESSO!")
                print(f"    -> Senha decifrada: {palavra_testada}")
                print(f"    -> Total de tentativas: {tentativas}")
                print(f"    -> Tempo decorrido: {tempo_total:.2f} segundos")
                return True
                
    print("\n\n[X] Senha não encontrada com as configurações atuais.")
    return False

if __name__ == "__main__":
    print("=" * 45)
    print("     SIMULADOR DE FORÇA BRUTA (PYTHON)     ")
    print("=" * 45)
    
    senha = input("Digite uma senha de até 3 caracteres (ex: a1, 7m, c): ").strip()
    
    if len(senha) > 3 or len(senha) == 0:
        print("\n[Erro] Por favor, digite uma senha que tenha entre 1 e 3 caracteres.")
    else:
        brute_force(senha, tamanho_max=3)
