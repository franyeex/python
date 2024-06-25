from time import sleep
from colorama import Fore, Style, init
import os 

# Inicializar colorama
init(autoreset=True)

# Diccionario de código Morse a texto
MORSE_TO_TEXT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9', '/': ' '
}

# Diccionario de texto a código Morse
TEXT_TO_MORSE = {v: k for k, v in MORSE_TO_TEXT.items()}

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')

print(f'{Fore.CYAN}[ℹ️] Version 2.0')
sleep(1)
print(f'{Fore.WHITE}[❗] Los mensajes de morse a texto aparecerán en mayúsculas.')
sleep(1)
print(f'{Fore.CYAN}[👤] Tool hecha por cizcow')
sleep(1)
print(f'{Fore.GREEN}[❓] Este script convierte código Morse a texto y viceversa')
sleep(1)
print(f'{Fore.YELLOW}[🎶] Visita mi github!  https://github.com/franyeex')
sleep(1)
print(f'{Fore.RED}[❌] Para salir, escribe "salir"')
sleep(3)
limpiar_pantalla()
print(f'{Fore.CYAN}[ℹ️] Version 2.0 | {Fore.GREEN}Cizcow Translator | {Fore.YELLOW}https://github.com/franyeex')
print(f'{Fore.WHITE}[❗] Los mensajes de morse a texto aparecerán en mayúsculas.')
print(f'{Fore.RED}[❌] Para salir, escribe "salir"')




def morse_a_texto(texto_morse):
    palabras = texto_morse.strip().split(' ')
    mensaje_decodificado = ''.join([MORSE_TO_TEXT.get(code, '') for code in palabras])
    return mensaje_decodificado

def texto_a_morse(texto_plano):
    texto_plano = texto_plano.upper()
    mensaje_codificado = ' '.join([TEXT_TO_MORSE.get(char, '') for char in texto_plano])
    return mensaje_codificado

# Entrada del usuario
while True:
    modo = input(f"{Fore.MAGENTA}[➡️] Elige el modo ('texto a morse' o 'morse a texto'): ").strip().lower()
    if modo == "salir":
        break
    elif modo == "texto a morse":
        texto_plano = input(f"{Fore.MAGENTA}[+] Introduce el texto plano: ")
        if texto_plano.lower() == "salir":
            break
        codigo_morse = texto_a_morse(texto_plano)
        print(f'{Fore.BLUE}[>] Código Morse: {codigo_morse}')
    elif modo == "morse a texto":
        texto_morse = input(f"{Fore.MAGENTA}[+] Introduce el código Morse: ")
        if texto_morse.lower() == "salir":
            break
        texto_decodificado = morse_a_texto(texto_morse)
        print(f'{Fore.BLUE}[>] Texto Decodificado: {texto_decodificado}')
    else:
        print(f"{Fore.RED}[!] Modo no válido. Por favor, elige 'texto a morse' o 'morse a texto'.")
    sleep(1)  # Pausa de 1 segundo antes de la siguiente iteración
