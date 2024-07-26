str = "I am learning information security"

result = ""
s = 20
for i in range(len(str)):
        char = str[i]
        
        if(str[i] == " "):
            result += str[i]
            continue

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

print("cipher is:" + result);
decipher = ""
for i in range(len(result)):
    char = result[i]
    if(str[i] == " "):
        decipher += result[i]
        continue
    if(char.isupper()):
        decipher += chr((ord(char)-s-65)%26 +65)
    else:
        decipher += chr((ord(char) - s - 97) % 26 +97)
    
print("decipher is:"+decipher)
