from time import sleep
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

# Diccionario de código Morse
DICCIONARIO_MORSE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9', '/': ' '
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

def morse_a_texto(texto_morse):
    palabras = texto_morse.strip().split(' ')
    mensaje_decodificado = ''.join([DICCIONARIO_MORSE.get(code, '') for code in palabras])
    return mensaje_decodificado

# Entrada del usuario
while True:
    texto_morse = input(f"{Fore.MAGENTA}[+] Introduce el código Morse: ")
    if texto_morse.lower() == "salir":
        break
    texto_decodificado = morse_a_texto(texto_morse)
    print(f'{Fore.BLUE}[>] Texto Decodificado: {texto_decodificado}')
    sleep(1)