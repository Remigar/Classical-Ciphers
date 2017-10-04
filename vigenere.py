from cipherinterface import *

def generateTableau():
    dimension = 26
    table = [['' for x in range(dimension)] for y in range(dimension)]

    #fill in rows

    for j in range(dimension):
        for i in range(dimension):
            a = j + i
            if a >= 26:
                a -= 26
            table[j][i] = chr(a + 97)

    return table

class Vigenere(CipherInterface):
    def __init__(self):
        self.key = ""
    def setKey(self, key):
        #a valid vigenere key is a string of alphabet characters
        if not key.isalpha():
            return False
        else:
            self.key = key
            return True
    def encrypt(self, plaintext):
        stripped_plaintext = plaintext.replace(" ", "").rstrip()
        table = generateTableau()
        keystring = self.key
        #we must extend the keystring to match the size of the plaintext
        while len(keystring) < len(stripped_plaintext):
            keystring += self.key
        result = ""
        for i in range(0, len(stripped_plaintext)):
            x_coord = (ord(stripped_plaintext[i]) - 96) % 26
            y_coord = (ord(keystring[i]) - 96) % 26
            result += table[x_coord-1][y_coord-1]
        return result
    def decrypt(self, ciphertext):
        stripped_ciphertext = ciphertext.replace(" ", "").rstrip()
        table = generateTableau()
        keystring = self.key
        while len(keystring) < len(stripped_ciphertext):
            keystring += self.key
        result = ""
        #in decryption, key letter describes row
        #position of the ciphertext letter in that row determine the column
        for i in range(0, len(stripped_ciphertext)):
            #search in the key letter row for the ciphertext letter
            row_num = (ord(keystring[i]) - 97) % 26
            col_num = table[row_num].index(stripped_ciphertext[i])
            result += table[0][col_num]
        return result
