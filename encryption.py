# -*- coding: utf-8 -*-
"""
Created on Sat May 22 21:40:21 2021

@author: athar
"""
import pyAesCrypt
from os import stat, remove
# encryption/decryption buffer size - 64K
# with stream-oriented functions, setting buffer size is mandatory
bufferSize = 64 * 1024
password = "atharvkaushik"
# get encrypted file size
encFileSize = stat("data.txt.aes").st_size
# decrypt
with open("data.txt.aes", "rb") as fIn:
    try:
        with open("dataout.txt", "wb") as fOut:
            # decrypt file stream
            pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
    except ValueError:
        # remove output file on error
        remove("dataout.txt")
# encrypt
with open("data.txt", "rb") as fIn:
    with open("data.txt.aes", "wb") as fOut:
        pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)



