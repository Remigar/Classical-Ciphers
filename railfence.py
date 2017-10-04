from cipherinterface import *


class Railfence(CipherInterface):
    def __init__(self):
        self.key = 0
    def setKey(self, key):
        #a valid railfence key a single integer
            self.key = int(key)
            return True
    def encrypt(self, plaintext):
        stripped_plaintext = plaintext.replace(" ", "").rstrip()
        ptext_size = len(stripped_plaintext)

        row_count = 0
        result = []
        #make as many rows as self.key
        for i in range (0, self.key):
            result.append("")
        #read the plaintext into the rows
        for character in stripped_plaintext:
            result[row_count] += character
            row_count += 1
            if row_count == self.key:
                row_count = 0

        return ''.join(result)
    def decrypt(self, ciphertext):
        stripped_ciphertext = ciphertext.replace(" ", "").rstrip()
        ctext_size = len(stripped_ciphertext)
        remainder = ctext_size % self.key #this many rows will have an extra char
        row_count = self.key
        row_size = ctext_size / row_count

        result = []
        for i in range(0, self.key):
            result.append("")
        #first we handle the rows with an extra char
        position = 0
        for i in range(0, remainder):
            result[i] += stripped_ciphertext[position:row_size+1]
            position += row_size + 1

        #the remaining rows are constructed next
        for i in range(remainder, row_count):
            result[i] += stripped_ciphertext[position:row_size+position]
            position += row_size


        actual_result = ""

        col_count = 0
        for i in range (0, ctext_size / self.key):
            for element in result:
                actual_result += element[i]
        for i in range(0, remainder):
            actual_result += result[i][-1]
        return actual_result
