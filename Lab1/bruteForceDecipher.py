#affine cipher : ax+b
#plaintext = ab
#encrypt = gl

def decipherText(ciphertext,a,b):
    decipher = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha(): 
            char = chr(((ord(ciphertext[i]) - ord('a') - b) * pow(a, -1, 26)) % 26 + ord('a'))
            print(char, end="")

ciphertext = "XPALASXYFGFUKPXUSOGEUTKCDGEXANMGNVS".lower()
a = 5
b = 6
decipherText(ciphertext,a,b)

