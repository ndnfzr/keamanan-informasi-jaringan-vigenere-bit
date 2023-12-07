def text_to_binary(text):
    binary_result = ""
    for char in text:
        # Konversi karakter ke ASCII, lalu ke biner
        binary_char = format(ord(char), 'b')
        binary_result += binary_char.rjust(8, '0') + " "  # Sesuaikan panjang biner menjadi 8 dengan padding nol di depan
    return binary_result.strip()  # Hapus spasi di akhir

def vigenere_encrypt(message, key):
    encrypted_message = ""
    key_binary = text_to_binary(key)

    # Sesuaikan panjang kunci biner dengan panjang pesan biner
    key_binary = key_binary * (len(message) // len(key_binary)) + key_binary[:len(message) % len(key_binary)]

    message_binary = text_to_binary(message)

    # Pastikan panjang pesan biner dan kunci biner sama
    min_length = min(len(message_binary), len(key_binary))
    message_binary = message_binary[:min_length]
    key_binary = key_binary[:min_length]

    print(f"Pesan ({message}): {text_to_binary(message)}")
    print(f"Kunci ({key}): {text_to_binary(key)}")

    for i in range(len(message_binary)):
        # Lakukan XOR bit ke bit antara pesan dan kunci
        encrypted_bit = str(int(message_binary[i]) ^ int(key_binary[i]))
        encrypted_message += encrypted_bit

    print(f"Hasil Enkripsi (dalam bentuk biner): {encrypted_message}")

    return encrypted_message

def vigenere_decrypt(encrypted_message, key):
    decrypted_message = ""
    key_binary = text_to_binary(key)

    # Sesuaikan panjang kunci biner dengan panjang pesan biner
    key_binary = key_binary * (len(encrypted_message) // len(key_binary)) + key_binary[:len(encrypted_message) % len(key_binary)]

    # Pastikan panjang pesan terenkripsi dan kunci biner sama
    min_length = min(len(encrypted_message), len(key_binary))
    encrypted_message = encrypted_message[:min_length]
    key_binary = key_binary[:min_length]

    print(f"Hasil Enkripsi (dalam bentuk biner): {encrypted_message}")
    print(f"Kunci ({key}): {text_to_binary(key)}")

    for i in range(len(encrypted_message)):
        try:
            # Lakukan XOR bit ke bit antara pesan terenkripsi dan kunci
            decrypted_bit = str(int(encrypted_message[i], 2) ^ int(key_binary[i], 2))
            decrypted_message += decrypted_bit
        except ValueError:
            # Tangani karakter tidak valid
            print(f"Ignored invalid character: {encrypted_message[i]}")

    print(f"Hasil Dekripsi (dalam bentuk biner): {decrypted_message}")

    return decrypted_message

# Input dari pengguna
message = input("Masukkan pesan: ")
key = input("Masukkan kunci: ")

# Enkripsi pesan
encrypted_message = vigenere_encrypt(message, key)

# Dekripsi pesan
decrypted_message = vigenere_decrypt(encrypted_message, key)
