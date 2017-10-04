from cipherinterface import *
from playfair import *
from caesar import *
from railfence import *
from vigenere import *
from rowtransposition import *
import os

def errormsg():
    print("USAGE: python main.py <CIPHER> <KEY> <ENC/DEC> <INPUT FILE> <OUTPUT FILE>")
    exit(-1)

if len(sys.argv) != 6:
    errormsg()



if sys.argv[1] == "CES":
    C = Caesar()
    C.setKey(int(sys.argv[2]))
    filein = open(sys.argv[4])
    fileout = open(sys.argv[5], "w")
    if sys.argv[3] == "ENC":
        plaintext = filein.read()
        fileout.write(C.encrypt(plaintext))
        exit(0)
    elif sys.argv[3] == "DEC":
        ciphertext=filein.read()
        fileout.write(C.decrypt(ciphertext))
        exit(0)
    else:
        errormsg()
elif sys.argv[1] == "PLF":
    P = Playfair()
    P.setKey(sys.argv[2])
    filein = open(sys.argv[4])
    fileout = open(sys.argv[5], "w")
    if sys.argv[3] == "ENC":
        plaintext = filein.read()
        fileout.write(P.encrypt(plaintext))
        exit(0)
    elif sys.argv[3] == "DEC":
        ciphertext=filein.read()
        fileout.write(P.decrypt(ciphertext))
        exit(0)
    else:
        errormsg()
elif sys.argv[1] == "RTS":
    R = RowTransposition()
    if not R.setKey(sys.argv[2]):
        errormsg()
    filein = open(sys.argv[4])
    fileout = open(sys.argv[5], 'w')
    if sys.argv[3] == "ENC":
        plaintext = filein.read()
        fileout.write(R.encrypt(plaintext))
        exit(0)
    elif sys.argv[3] == "DEC":
        ciphertext=filein.read()
        fileout.write(R.decrypt(ciphertext))
        exit(0)
    else:
        errormsg()
elif sys.argv[1] == "RFC":
    R = Railfence()
    R.setKey(int(sys.argv[2]))
    filein = open(sys.argv[4])
    fileout = open(sys.argv[5], "w")
    if sys.argv[3] == "ENC":
        plaintext = filein.read()
        fileout.write(R.encrypt(plaintext))
        exit(0)
    elif sys.argv[3] == "DEC":
        ciphertext=filein.read()
        fileout.write(R.decrypt(ciphertext))
        exit(0)
    else:
        errormsg()
elif sys.argv[1] == "VIG":
    V = Vigenere()
    V.setKey(sys.argv[2])
    filein = open(sys.argv[4])
    fileout = open(sys.argv[5], "w")
    if sys.argv[3] == "ENC":
        plaintext = filein.read()
        fileout.write(V.encrypt(plaintext))
        exit(0)
    elif sys.argv[3] == "DEC":
        ciphertext=filein.read()
        fileout.write(V.decrypt(ciphertext))
        exit(0)
    else:
        errormsg()
else:
    errormsg()
