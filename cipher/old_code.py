key_map = {
    'A': '00', 'B': '01', 'C': '02', 'D': '03', 'E': '04',
    'F': '05', 'G': '06', 'H': '07', 'I': '08', 'J': '09',
    'K': '10', 'L': '11', 'M': '12', 'N': '13', 'O': '14',
    'P': '15', 'Q': '16', 'R': '17', 'S': '18', 'T': '19',
    'U': '20', 'V': '21', 'W': '22', 'X': '23', 'Y': '24',
    'Z': '25'
}

reverse_map = {v: k for k, v in key_map.items()}

def encrypt(text):
    text = text.upper()
    words = text.split()
    encrypted_words = []
    for word in words:
        encrypted_word = ''.join([key_map.get(char, char) for char in word])
        encrypted_words.append(encrypted_word)
    return ' '.join(encrypted_words)

def decrypt(cipher_text):
    words = cipher_text.strip().split()
    decrypted_words = []
    for word in words:
        chars = [word[i:i+2] for i in range(0, len(word), 2)]
        decrypted_word = ''.join([reverse_map.get(code, code) for code in chars])
        decrypted_words.append(decrypted_word)
    return ' '.join(decrypted_words)

# --- Example Usage ---
if __name__ == "__main__":
    print("Classic 2-Digit Cipher")

    plain_text = input("Enter text to encrypt: ")
    cipher_result = encrypt(plain_text)
    print("Encrypted:", cipher_result)

    cipher_input = input("\nEnter 2-digit codes to decrypt (space between words): ")
    decrypted_text = decrypt(cipher_input)
    print("Decrypted:", decrypted_text)
