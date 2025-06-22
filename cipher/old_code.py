key_map = {
    'A': '00', 'B': '01', 'C': '02', 'D': '03', 'E': '04',
    'F': '05', 'G': '06', 'H': '07', 'I': '08', 'J': '09',
    'K': '10', 'L': '11', 'M': '12', 'N': '13', 'O': '14',
    'P': '15', 'Q': '16', 'R': '17', 'S': '18', 'T': '19',
    'U': '20', 'V': '21', 'W': '22', 'X': '23', 'Y': '24',
    'Z': '25'
}

reverse_map = {
    '00': 'A', '01': 'B', '02': 'C', '03': 'D', '04': 'E',
    '05': 'F', '06': 'G', '07': 'H', '08': 'I', '09': 'J',
    '10': 'K', '11': 'L', '12': 'M', '13': 'N', '14': 'O',
    '15': 'P', '16': 'Q', '17': 'R', '18': 'S', '19': 'T',
    '20': 'U', '21': 'V', '22': 'W', '23': 'X', '24': 'Y',
    '25': 'Z'
}


def encrypt(text):
    text = text.upper().replace(" ", "")
    encrypted = [key_map.get(char, '??') for char in text]
    return ' '.join(encrypted)

def decrypt(cipher_text):
    codes = cipher_text.strip().split()
    decrypted = [reverse_map.get(code, '?') for code in codes]
    return ''.join(decrypted)

# --- Example Usage ---
if __name__ == "__main__":
    print("Classic 2-Digit Cipher")

    plain_text = input("Enter text to encrypt: ")
    cipher_result = encrypt(plain_text)
    print("Encrypted:", cipher_result)

    cipher_input = input("\nEnter 2-digit codes to decrypt (separated by space): ")
    decrypted_text = decrypt(cipher_input)
    print("Decrypted:", decrypted_text)
