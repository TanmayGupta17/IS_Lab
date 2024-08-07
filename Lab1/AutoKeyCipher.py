str = "the house is being sold tonight"

key = "g"

res = []
shifted = []
count1 = 0
count2 = 0

for i in str:
    if i.isalpha():
        if count1<len(key):
            res.append(key[count1])
            count1 += 1
            shifted.append(i)
        elif count2 < len(str):
            res.append(shifted[count2])
            count2 += 1
            shifted.append(i)
    else:
        res.append(i)
print("newKey: "+"".join(res))
print("Plaintext: "+str)

cipher = ""

for i in range(len(str)):
    c1 = str[i]
    c2 = res[i]
    if(c1.isalpha()):
        char = chr((ord(c1)-ord('a')+ord(c2)-ord('a'))%26+ord('a'))
        cipher += char
    else:
        cipher += c1
print("Encrypted: "+cipher)


decrypted_text = ""
key_for_decryption = key  # Start with the keyword

i=0
j=0
while i < len(cipher):
    c1 = cipher[i]
    if c1.isalpha():
        c2 = key_for_decryption[j]
        char = chr((ord(c1)-ord('a') - (ord(c2)-(ord('a')))+26) % 26 + ord('a'))
        decrypted_text += char
        key_for_decryption += char
        j += 1
    else:
        decrypted_text += c1
    i+=1

print("Decryption:", decrypted_text)
