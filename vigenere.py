alphabet = 'AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ'
ALPHABET_SIZE = 31

def validare_text(text):
    text = text.replace(" ", "").upper()
    for char in text:
        if char not in alphabet:
            print(f"Caracter invalid '{char}'! Folositi litere de la A-Z, Ă, Â, Î, Ș, Ț.")
            return None
    return text

def validare_cheie(key):
    key = key.replace(" ", "").upper()
    if len(key) < 7:
        print("Cheia trebuie sa aiba cel putin 7 caractere!")
        return None
    for char in key:
        if char not in alphabet:
            print(f"Caracter invalid '{char}' in cheie! Folositi litere de la A-Z, Ă, Â, Î, Ș, Ț.")
            return None
    return key

def vigenere_criptare(plaintext, key):
    print(f"Criptare: {plaintext} cu cheia: {key}")
    plaintext = plaintext.replace(" ", "").upper()
    key = key.replace(" ", "").upper()
    result = ""
    key_length = len(key)
    
    for i, char in enumerate(plaintext):
        if char in alphabet:
            # Get positions in alphabet
            plain_pos = alphabet.index(char)
            key_char = key[i % key_length]
            key_pos = alphabet.index(key_char)
            # Encryption: C = (P + K) mod 31
            new_pos = (plain_pos + key_pos) % ALPHABET_SIZE
            result += alphabet[new_pos]
    
    print(f"Criptograma: {result}")
    return result

def vigenere_decriptare(ciphertext, key):
    print(f"Decriptare: {ciphertext} cu cheia: {key}")
    ciphertext = ciphertext.replace(" ", "").upper()
    key = key.replace(" ", "").upper()
    result = ""
    key_length = len(key)
    
    for i, char in enumerate(ciphertext):
        if char in alphabet:
            # Get positions in alphabet
            cipher_pos = alphabet.index(char)
            key_char = key[i % key_length]
            key_pos = alphabet.index(key_char)
            # Decryption: P = (C - K) mod 31
            new_pos = (cipher_pos - key_pos) % ALPHABET_SIZE
            result += alphabet[new_pos]
    
    print(f"Decriptat: {result}")
    return result

# Main program with user input
if __name__ == "__main__":
    # Get user choice for operation
    action = input("Criptati sau decriptare? (e/d): ").lower()
    
    if action not in ['e', 'd']:
        print("Invalid action! Use 'e' or 'd'.")
    else:
        # Get text and key input
        text = input("Enter text to process: ")
        key = input("Enter key (at least 7 characters): ")
        
        # Validate inputs
        validated_text = validare_text(text)
        validated_key = validare_cheie(key)
        
        if validated_text and validated_key:
            if action == "e":
                vigenere_criptare(validated_text, validated_key)
            else:
                vigenere_decriptare(validated_text, validated_key)