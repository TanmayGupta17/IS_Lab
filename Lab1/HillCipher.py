def hillCipher(msg, keyMatrix):
    # Remove spaces and convert message to lowercase
    msg = msg.replace(" ", "").lower()
    n = len(msg)
    
    # Ensure the message length is even
    if n % 2 != 0:
        msg += 'x'  # Padding with 'x' if the length is odd

    encrypted_msg = ""
    
    for i in range(0, len(msg), 2):
        msgMatrix = [[0], [0]]
        for j in range(2):
            msgMatrix[j][0] = ord(msg[i + j]) - ord('a')
        
        # Perform matrix multiplication
        encryptedMatrix = matrixMultiplication(keyMatrix, msgMatrix)
        
        # Convert back to characters and append to result
        for k in range(2):
            encrypted_msg += chr(encryptedMatrix[k][0] + ord('a'))
    
    return encrypted_msg

def matrixMultiplication(keyMatrix, msgMatrix):
    res = [[0], [0]]
    for i in range(2):
        for j in range(2):
            res[i][0] += keyMatrix[i][j] * msgMatrix[j][0]
        res[i][0] = res[i][0] % 26
    return res

# Example usage
msg = "we live in an insecure world"
keyMatrix = [
    [3, 3],
    [2, 7]
]

encrypted_msg = hillCipher(msg, keyMatrix)
print("Encrypted Message:", encrypted_msg)
