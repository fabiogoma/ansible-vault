#!/bin/python

from Crypto.PublicKey import RSA
import os
import ast

private_key_string = open(os.environ['HOME'] + "/.ssh/id_rsa","r").read()
private_key = RSA.importKey(private_key_string)

f = open(os.environ['HOME'] + "/secret.txt", "r")
encrypted_string = str(f.read())

decrypted = private_key.decrypt(ast.literal_eval(encrypted_string))
f.close()

print decrypted
