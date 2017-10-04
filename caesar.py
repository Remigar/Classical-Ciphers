from cipherinterface import *

class Caesar(CipherInterface):
    def __init__(self):
        self.key = 0
    def setKey(self, key):
        #a valid caesar cipher key is a number between 0 and 25
        self.key = int(key) % 26
    def encrypt(self, plaintext):
        result = []
        for character in plaintext:
            if not character.isalpha():
                result.append(character)
                continue
            character_num = ord(character) - 96
            character_num += self.key
            character_num = (character_num % 26) + 96
            if character_num == 96:
                character_num += 26
            result.append(chr(character_num))
        return ''.join(result)

        return result
    def decrypt(self, ciphertext):
        #repeat the same process except subtract the key
        result = []
        for character in ciphertext:
            if not character.isalpha():
                result.append(character)
                continue
            character_num = ord(character) - 96
            character_num -= self.key
            character_num = (character_num % 26) + 96
            if character_num == 96:
                character_num += 26
            result.append(chr(character_num))

        return ''.join(result)
