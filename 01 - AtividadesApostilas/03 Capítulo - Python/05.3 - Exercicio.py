# Você é um investigador e precisa decifrar uma mensagem secreta escondida em um texto. 
# Cada letra da mensagem foi substituída pela letra do alfabeto que vem imediatamente depois 
# dela. Por exemplo, "a" foi substituída por "b", "b" foi substituída por "c", e assim por 
# diante. A letra "z" foi substituída por "a". Escreva uma função recursiva chamada decifrar_mensagem 
# que aceite a mensagem codificada como uma string e retorne a mensagem decodificada. A regra é que a 
# função deve ser recursiva!

def decifrar_mensagem(mensagem):
    if not mensagem:
        return ""
    
    primeira_letra = mensagem[0]
    
    if 'a' <= primeira_letra <= 'z':
        if primeira_letra == 'a':
            decifrada = 'z'
        else:
            decifrada = chr(ord(primeira_letra) - 1)
    else:
        decifrada = primeira_letra

    return decifrada + decifrar_mensagem(mensagem[1:])

mensagem_codificada = "ifmmp"
mensagem_decifrada = decifrar_mensagem(mensagem_codificada)
print(mensagem_decifrada)
