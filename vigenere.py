alphabet = 'AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ'
ALPHABET_SIZE = 31

def validare_text():
    while True:
        text = input("Introdu mesajul: ").replace(" ", "").upper()
        for char in text:
            if char not in alphabet:
                print(f"Caracter invalid '{char}'! Folositi litere de la A-Z, Ă, Â, Î, Ș, Ț.")
                break
        else:
            return text

def validare_cheie():
    while True:
        key = input("Introdu cheia (cu cel putin 7 caractere): ").replace(" ", "").upper()
        if len(key) < 7:
            print("Cheia trebuie sa aiba cel putin 7 caractere!")
            continue
        for char in key:
            if char not in alphabet:
                print(f"Caracter invalid '{char}' in cheie! Folositi litere de la A-Z, Ă, Â, Î, Ș, Ț.")
                break
        else:
            return key

def vigenere_criptare(plaintext, key):
    criptat = ""
    key_length = len(key)
    
    for i, char in enumerate(plaintext):
        if char in alphabet:
            plain_pos = alphabet.index(char)
            key_char = key[i % key_length]
            key_pos = alphabet.index(key_char)
            new_pos = (plain_pos + key_pos) % ALPHABET_SIZE
            criptat += alphabet[new_pos]
    
    print(f"Criptograma: {criptat}")
    return criptat

def vigenere_decriptare(ciphertext, key):
    print(f"Decriptare: {ciphertext} cu cheia: {key}")
    decriptat = ""
    key_length = len(key)
    
    for i, char in enumerate(ciphertext):
        if char in alphabet:
            cipher_pos = alphabet.index(char)
            key_char = key[i % key_length]
            key_pos = alphabet.index(key_char)
            new_pos = (cipher_pos - key_pos) % ALPHABET_SIZE
            decriptat += alphabet[new_pos]
    
    print(f"Decriptat: {decriptat}")
    return decriptat

alegere = ""
while alegere != "q":
    print("\n----------Alege o optiunne de mai jos----------")
    print(" c - criptarea mesajului")
    print(" d - decriptarea mesajului")
    print(" q - inchidere program")

    alegere = input(">>> ").strip().lower()
    
    if alegere == 'c':
        text = validare_text()
        key = validare_cheie()
        rezultat = vigenere_criptare(text, key)
    elif alegere == 'd':
        text = validare_text()
        key = validare_cheie()
        rezultat = vigenere_decriptare(text, key)
    elif alegere == 'q':
        print("\nOprire program.")
    else:
        print("Optiune invalida")
