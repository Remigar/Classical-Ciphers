from cipherinterface import *


def constructMatrix(key):
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    matrix = ''
    for letter in key:
        if letter not in matrix and letter in alphabet:
            matrix += letter
    for letter in alphabet:
        if letter not in matrix:
            matrix += letter
    return matrix

def getDigraphs(text):
    digraphList = []
    l_text = text.lower().replace('j','i').rstrip()

    position = 0

    while position < len(l_text):
        digraph = ''
        if position + 1 == len(l_text):
            digraph = l_text[position] + 'x'
            digraphList.append(digraph)
            break
        elif l_text[position] != l_text[position+1]:
            digraph = l_text[position:position+2]
            digraphList.append(digraph)
            position += 2
        else:
            digraph = l_text[position] + 'x'
            digraphList.append(digraph)
            position += 1

    return digraphList

def enc_digraph(matrix, digraph):
    x = matrix.find(digraph[0])
    y = matrix.find(digraph[1])
    x_coord = [x % 5, x/5]
    y_coord = [y % 5, y/5]
    result = ''

    if x_coord[0] == y_coord[0]:#both letters in the same column
        result = matrix[(((x_coord[1] + 1)%5)*5)+ x_coord[0]]
        result += matrix[(((y_coord[1] + 1)%5)*5) + y_coord[0]]
    elif x_coord[1] == y_coord[1]:#both letters in the same row
        result = matrix[(x_coord[1] * 5) + ((x_coord[0]+1)%5)]
        result += matrix[(y_coord[1] * 5) + ((y_coord[0]+1)%5)]
    else:
        result = matrix[(x_coord[1] * 5) + y_coord[0]]
        result += matrix[(y_coord[1] * 5) + x_coord[0]]

    return result

def dec_digraph(matrix, digraph):
    x = matrix.find(digraph[0])
    y = matrix.find(digraph[1])
    x_coord = [x % 5, x/5]
    y_coord = [y % 5, y/5]
    result = ''

    if x_coord[0] == y_coord[0]:#both letters in the same column
        result = matrix[(((x_coord[1] - 1)%5)*5)+ x_coord[0]]
        result += matrix[(((y_coord[1] - 1)%5)*5) + y_coord[0]]
    elif x_coord[1] == y_coord[1]:#both letters in the same row
        result = matrix[(x_coord[1] * 5) + ((x_coord[0]-1)%5)]
        result += matrix[(y_coord[1] * 5) + ((y_coord[0]-1)%5)]
    else:
        result = matrix[(x_coord[1] * 5) + y_coord[0]]
        result += matrix[(y_coord[1] * 5) + x_coord[0]]

    return result

class Playfair(CipherInterface):
    def __init__(self):
        self.key = ""
    def setKey(self, key):
        #a valid Playfair key is 25 or fewer characters and is entirely alphabet characters
        if len(key) > 25:
            return False
        elif not key.isalpha():
            return False
        else:
            self.key = key
            return True
    def encrypt(self, plaintext):
        result = ""
        matrix = constructMatrix(self.key)
        digraphList = getDigraphs(plaintext)
        for digraph in digraphList:
            result += enc_digraph(matrix, digraph)

        print result
        return result

    def decrypt(self, ciphertext):
        result = ""
        matrix = constructMatrix(self.key)
        digraphList = getDigraphs(ciphertext)
        for digraph in digraphList:
            result += dec_digraph(matrix, digraph)
        return result
