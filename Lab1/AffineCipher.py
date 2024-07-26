str = "i am learning information security"

a = 15
b = 20

result = ""
for i in range(len(str)):
    char = str[i]
    if(char != " "):
        if(char.isupper()):
            result+=chr((a*(ord(char)-65)+b)%26+65)
        else:
            result+=chr((a*(ord(char)-97)+b)%26+97)
    else:
        result += char
print("Encryption: "+result)
decipher = ""
a_inv = pow(a,-1,26)
for i in range(len(result)):
    char = result[i]
    har = str[i]
    if(char != " "):
        if(char.isupper()):
            decipher+=chr((a_inv*(ord(char)-65-b))%26+65)
        else:
            decipher+=chr((a_inv*(ord(char)-97-b))%26+97)
    else:
        decipher += char
print("Decryption: "+decipher)
    
    
