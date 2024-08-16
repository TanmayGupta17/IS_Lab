
         
def generateTable(list1,word):
    key_table = []
    for i in word:
        if i not in key_table:
            key_table.append(i)
        
    compElements = []
    for i in key_table:
        if i not in compElements:
            compElements.append(i)
    for i in list1:
        if i not in compElements:
            compElements.append(i)
    matrix = []
    while compElements != []:
        matrix.append(compElements[:5])
        compElements = compElements[5:]
    return matrix

def encypt_row_rule(matrix,e1r,e1c,e2r,e2c):
    char1 = ''
    if(e1c==4):
        char1 = matrix[e1r][0]
    else:
        char1 = matrix[e1r][e1c+1]
    
    char2 = ''
    if(e2c == 4):
        char2 = matrix[e2r][0]
    else:
        char2 = matrix[e2r][e2c+1]
    
    return char1,char2

def encrypt_col_rule(matrix,e1r,e1c,e2r,e2c):
    char1 = ''
    if(e1r == 4):
        char1 = matrix[0][e1c]
    else:
        char1 = matrix[e1r][e1c]
    char2 = ''
    if(e2r == 4):
        char2 = matrix[0][e2c]
    else:
        char2 = matrix[e2r][e2c]
    
    return char1,char2
    
def search(mat, element):
    for i in range(5):
        for j in range(5):
            if(mat[i][j] == element):
                return i, j
                
def encrypt_rectangle_rule(matrix,e1r,e1c,e2r,e2c):
    char1 = ''
    char1 = matrix[e1r][e2c]
    char2 = ''
    char2 = matrix[e2r][e1c]
    
    return char1,char2

def PlayfairCipher(matrix,subStrings):
    ciphertext = []
    for i in range(len(subStrings)):
        c1=0
        c2=0
        e1r,e1c=search(matrix,subStrings[i][0])
        e2r,e2c=search(matrix,subStrings[i][1])
        
        if e1r == e2r:
            c1,c2=encrypt_row_rule(matrix,e1r,e1c,e2r,e2c)
        elif e2c == e1c:
            c1,c2=encrypt_col_rule(matrix,e1r,e1c,e2r,e2c)
        else:
            c1,c2=encrypt_rectangle_rule(matrix,e1r,e1c,e2r,e2c)
        
        cipher = c1+c2
        ciphertext.append(cipher)
    return ciphertext


#main function
    
str = "the key is hidden under the doorpad"
secretKey = "guidance"
newStr = str.replace(" ","")
print(newStr)
matrix = [[0 for x in range(5)] for y in range(5)]
myset = {}

i = 0
while i < len(newStr) - 1:
    if newStr[i] == newStr[i+1]:
        incremented_char = chr(ord(newStr[i]) + 1)
        newStr = newStr[:i+1] + incremented_char + newStr[i+1:]
        i += 2
    else:
        i += 1
i = 0
substrings = []  # Initialize a list with a different name
while i < len(newStr):
    substring = newStr[i:i+2]
    substrings.append(substring)  # Use append() to add to the list
    i += 2
if len(newStr) % 2 != 0:
    # Increment the last character of the last substring
    last_char = newStr[-1]
    incremented_char = chr(ord(last_char) + 1)
    # Add the incremented character to the last substring
    if substrings:
        substrings[-1] += incremented_char
    else:
        substrings.append(incremented_char)

print(substrings)

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
matrix = generateTable(list1,secretKey)
cipherlist = PlayfairCipher(matrix,substrings)

ciphertext = ""
for i in cipherlist:
    ciphertext += i
print("Encrypted Text:"+ciphertext)
