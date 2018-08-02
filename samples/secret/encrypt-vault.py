#!/bin/python

from Crypto.PublicKey import RSA
import os
import getpass

public_key_string = open(os.environ['HOME'] + "/.ssh/id_rsa.pub","r").read()
public_key = RSA.importKey(public_key_string)

password = getpass.getpass('Password: ')

#Encrypt with public key
encrypted = public_key.encrypt(password, 32)

f = open(os.environ['HOME'] + "/secret.txt", "w")
f.write(str(encrypted))
f.close()
