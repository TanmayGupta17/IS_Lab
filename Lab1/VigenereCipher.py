# Given strings
plaintext = "the house is being sold tonight"
key = "dollars"

cipher = ""
key = key.upper()
key_index = 0
for char in plaintext:
    if char.isalpha():  # Decrypt only alphabetic characters
            # Determine the shift amount
            shift = ord(key[key_index % len(key)]) - ord('A')
            if char.islower():
                # Decrypt lowercase letters
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                # Decrypt uppercase letters
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            
            # Move to the next character in the key
            key_index += 1
    else:
        new_char = char
    cipher += new_char
print("cipher:"+cipher)
key_index = 0
decipher=""
for char in cipher:
    if char.isalpha():  # Decrypt only alphabetic characters
            # Determine the shift amount
            shift = ord(key[key_index % len(key)]) - ord('A')
            if char.islower():
                # Decrypt lowercase letters
                new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                # Decrypt uppercase letters
                new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            
            # Move to the next character in the key
            key_index += 1
    else:
        new_char = char
    decipher += new_char


print("decipher:", decipher)

