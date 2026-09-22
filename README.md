# Simulador de Força Bruta - Desafio Python 🔐

Este projeto foi desenvolvido como um desafio prático de programação para compreender os conceitos básicos de segurança da informação, criptografia e análise de algoritmos através de um ataque de força bruta (*brute force*).

## 🚀 Como Funciona?
O script utiliza o módulo nativo `itertools` para gerar combinações sequenciais de caracteres (letras minúsculas e números) até encontrar a senha exata fornecida pelo usuário.

### 💡 Dicas Aplicadas no Desafio:
1. **Escopo reduzido:** Otimizado para senhas de até 3 caracteres para manter o tempo de execução curto.
2. **Uso do `itertools.product`:** Geração eficiente de combinações matemáticas em formato de tuplas.
3. **Manipulação de Strings:** Uso do método `"".join()` para converter rapidamente as tuplas geradas em palavras legíveis.

## 🛠️ Como Executar o Projeto

Certifique-se de ter o Python instalado na sua máquina. Abra o terminal na pasta do projeto e execute:

```bash
python main.py
```
