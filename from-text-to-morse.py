from time import sleep
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

# Diccionario de texto a código Morse
TEXT_A_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}
print(f'{Fore.CYAN}[ℹ️] Version 1.0')
sleep(1)
print(f'{Fore.CYAN}[👤] Tool hecha por cizcow')
sleep(1)
print(f'{Fore.GREEN}[❓] Este script convierte código Morse a texto')
sleep(1)
print(f'{Fore.YELLOW}[🎶] Visita mi github!  https://github.com/franyeex')
sleep(1)
print(f'{Fore.RED}[❌] Para salir, escribe "salir"')
sleep(1)

def texto_a_morse(texto_plano):
    texto_plano = texto_plano.upper()
    mensaje_codificado = ' '.join([TEXT_A_MORSE.get(char, '') for char in texto_plano])
    return mensaje_codificado

# Entrada del usuario
while True:
    texto_plano = input(f"{Fore.MAGENTA}[+] Introduce el texto que quieras pasar a morse: ")
    if texto_plano.lower() == "salir":
        break
    codigo_morse = texto_a_morse(texto_plano)
    print(f'{Fore.BLUE}[>] Código Morse: {codigo_morse}')
    sleep(1)  # Pausa de 1 segundo antes de la siguiente iteración
