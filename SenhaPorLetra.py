from random import randint

senha = input("Digite a senha que você quer encontrar: ")

letras = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
    '[', ']', '{', '}', '\\', '|', ';', ':', "'", '"', ',', '.', '/', '<', '>', '?', '`', '~', ' '
]

# Inicializa a variável que vai armazenar o valor gerado
acho = ""

while (acho != senha):
    acho = ""  # Reseta a variável
    for letra in senha:
        # Gera uma letra aleatória da lista 'letras'
        AchoLetra = letras[randint(0, len(letras) - 1)]
        acho += AchoLetra  # Adiciona a letra gerada à variável 'acho'
    print(acho)

print(f"Senha encontrada: {acho}")
