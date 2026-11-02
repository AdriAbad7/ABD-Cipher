# Configuración del cifrado
ALPHABET = 'ryñhwzldxopguvcjktasqmneibf'
NUMBERS = '8259130467'

def caesar(text, shift, encrypt=True):

    alphabet = ALPHABET
    numbers = NUMBERS

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift >= len(alphabet):
        return f'Shift must be an integer between 1 and {len(alphabet)-1}.'

    if not encrypt:
        shift = -shift

    # Desplazamiento de letras
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    # Desplazamiento de números
    number_shift = shift % len(numbers)
    shifted_numbers = numbers[number_shift:] + numbers[:number_shift]

    # Tabla de traducción
    translation_table = str.maketrans(
        alphabet + alphabet.upper() + numbers,
        shifted_alphabet + shifted_alphabet.upper() + shifted_numbers
    )

    return text.translate(translation_table)


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)