str = "i am learning information security"

result = ""
key = 15
for i in range(len(str)):
    char = str[i]
    if(str[i] == " "):
        result += str[i]
        continue
    if(char.isupper()):
        result += chr(((ord(char)-65)*key)%26+65)
    else:
        result += chr(((ord(char)-97)*key)%26+97)
print("cipher is: "+result)
decipher = ""
key_inverse = pow(key, -1, 26)
for i in range(len(result)):
    char = result[i]
    if(result[i] == " "):
        decipher += result[i]
        continue
    if(char.isupper()):
        decipher += chr(int((ord(char)-65)*key_inverse)%26+65)
    else:
        decipher += chr(int((ord(char)-97)*key_inverse)%26+97)
print("decipher is: "+decipher)
