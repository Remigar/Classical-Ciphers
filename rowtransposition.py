from cipherinterface import *

class RowTransposition(CipherInterface):
    def __init__(self):
        self.key = []
    def setKey(self, key):
        #a valid row transposition key is a list of integers
        if not key.isdigit():
            return False
        else:
            self.key = list(key)
            return True
    def encrypt(self, plaintext):
        stripped_plaintext = plaintext.replace(" ","").rstrip()
        ptext_size = len(stripped_plaintext)
        columns = len(self.key)
        rows = ptext_size / columns

        grid = []
        position = 0
        for i in range(0, rows):
            grid.append(stripped_plaintext[position:position+columns])
            position += columns
        #handle incomplete row(if there is one)
        remainder = ptext_size % columns
        if remainder:
            grid.append(stripped_plaintext[position:remainder+position])


        result = ""
        for i in range(0, columns):
            column_to_read = int(self.key[i]) - 1
            print column_to_read
            if column_to_read > remainder - 1: #the column doesn't have an extra character
                sublist = [item[column_to_read] for item in grid[0:len(grid)-1]]
                result += ''.join(sublist) + '$'

            else:
                sublist = [item[column_to_read] for item in grid]
                result += ''.join(sublist)


        return result
    def decrypt(self, ciphertext):
        stripped_ciphertext = ciphertext.replace(" ", "").rstrip()
        ctext_size = len(stripped_ciphertext)
        columns = len(self.key)
        rows = ctext_size / columns
        #we write the first (row) of ciphertext to the firt column and so on
        grid = ["" for x in range(0,rows)]
        position = 0
        for i in range(0, columns):

            ct_col = stripped_ciphertext[position:position+rows]

            for j in range(0, rows):
                grid[j] += ct_col[j]

            position += rows



        result = ""

        for i in range(0, rows):

            for k in range(0, columns):
                column_to_read = int(self.key.index(str(k+1)))
                result += grid[i][column_to_read]



        return result.replace('$','')
