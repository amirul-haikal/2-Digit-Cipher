import string
import random

# === Collatz Max Function ===
def collatz_max(n):
    max_val = n
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        max_val = max(max_val, n)
    return max_val

# === Generate Rotation 1 using Collatz (%100, unique) ===
def generate_collatz_key():
    cipher_map_array = []
    used_mod_100 = set()
    original_number = 1

    while len(cipher_map_array) < 26:
        max_val = collatz_max(original_number)
        mod_100 = max_val % 100
        if mod_100 not in used_mod_100:
            cipher_map_array.append((original_number, max_val, mod_100))
            used_mod_100.add(mod_100)
        original_number += 1

    rotation1 = {}
    for i, letter in enumerate(string.ascii_uppercase):
        rotation1[letter] = f"{cipher_map_array[i][2]:02}"
    rotation1[' '] = "99"  # Add space mapping
    return rotation1

# === Generate Rotations with +1 and +10 ===
def generate_rotations(base_key, increments):
    rotations = [base_key]
    for inc in increments:
        new_key = {}
        for letter, code in base_key.items():
            new_val = (int(code) + inc) % 100
            new_key[letter] = f"{new_val:02}"
        rotations.append(new_key)
    return rotations

# === Reverse Key ===
def get_reverse_key(key):
    return {v: k for k, v in key.items()}

# === Prime Check ===
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# === Encrypt Function ===
def encrypt_improved(text, keyset):
    text = text.upper()
    encrypted = ""
    dummy_positions = []
    used_codes = set()
    for key in keyset:
        used_codes.update(key.values())

    for i, char in enumerate(text):
        key = keyset[i % len(keyset)]
        encrypted += key.get(char, "??")
        if is_prime(i + 1):
            while True:
                dummy = f"{random.randint(0, 99):02}"
                if dummy not in used_codes:
                    encrypted += dummy
                    dummy_positions.append(len(encrypted) - 2)
                    break
    return encrypted, dummy_positions

# === Decrypt Function ===
def decrypt_improved(ciphertext, keyset):
    decrypted = ""
    i = 0
    j = 0
    while i < len(ciphertext):
        code = ciphertext[i:i + 2]
        key = keyset[j % len(keyset)]
        if code in key.values():
            reverse_key = get_reverse_key(key)
            decrypted += reverse_key.get(code, '?')
            j += 1
        i += 2
    return decrypted

# === Print Key Map ===
def print_key_pattern(keyset):
    print("\n--- Key Pattern (Rotating Keys) ---")
    for idx, key in enumerate(keyset):
        print(f"\nRotation {idx + 1}:")
        count = 0
        for letter in string.ascii_uppercase + " ":
            print(f"{letter} → {key[letter]}", end="    ")
            count += 1
            if count % 4 == 0:
                print()
    print()

# === Print Dummy Positions ===
def print_dummy_positions(dummy_positions):
    print("\n--- Dummy Code Placement ---")
    if dummy_positions:
        print("Dummy codes were inserted at these cipher indexes (starts):")
        print(', '.join(map(str, dummy_positions)))
    else:
        print("No dummy codes were inserted.")
    print()

# === Main Menu ===
def main():
    print("=== Improved 2-Digit Substitution Cipher System (Collatz + Prime Dummy) ===")
    rotation1 = generate_collatz_key()
    keyset = generate_rotations(rotation1, [1, 10])
    last_dummy_positions = []

    while True:
        print("\nMenu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Show Pattern Key Map")
        print("4. Show Dummy Code Positions")
        print("5. Exit")

        choice = input("Select option (1–5): ").strip()

        if choice == "1":
            pt = input("Enter text to encrypt: ")
            encrypted, dummy_positions = encrypt_improved(pt, keyset)
            last_encrypted = encrypted
            last_dummy_positions = dummy_positions
            print("\nEncrypted Cipher:")
            print(encrypted)

        elif choice == "2":
            ct = input("Enter encrypted cipher text (no spaces): ")
            decrypted = decrypt_improved(ct, keyset)
            print("\nDecrypted Text:")
            print(decrypted)

        elif choice == "3":
            print_key_pattern(keyset)

        elif choice == "4":
            print_dummy_positions(last_dummy_positions)

        elif choice == "5":
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1 and 5.")

# === Run ===
if __name__ == "__main__":
    main()
