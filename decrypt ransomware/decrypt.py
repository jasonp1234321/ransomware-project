import os
from cryptography.fernet import Fernet

files = []
#list named file which will store the files that will be encrypted

for file in os.listdir():
    #for each file in this file's current directory
    if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py":
        continue
        #prevents file from encrypting itself and the key it's saving
    if os.path.isfile(file):
        files.append(file)
        #prevents it from trying to add directory

with open("thekey.key", "rb")as key:
    secretkey = key.read()
    #reads the files so that it can decrypt it
for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fertnet(secretkey).decrypt(contents)
        #decrypts all the data in the file
        with open(file,"wb")as thefile:
            thefile.write(contents_decrypted)
        #encrypts the files with the key and puts them back