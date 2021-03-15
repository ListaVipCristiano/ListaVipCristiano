#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Por Diogo V. Kerting diogovk@gmail.com
# Sob GNU GPL

from optparse import OptionParser
import sys

usage = "usage: %prog [options] [mensagem]"

# Objeto que manipula a linha de comando
parser = OptionParser()
parser.add_option("-o", "--saida", dest="arquivo_saida", help="Imprime em arquivo",metavar="_default")
parser.add_option("-e", "--encripta", action="store_true", dest="encriptar",default=False,help="Encriptar mensagem",metavar="ENCRIPTA")
parser.add_option("-d", "--decripta", action="store_true", dest="decriptar",default=False,help="Decriptar mensagem",metavar="DECRIPTA")
parser.add_option("-c", "--chave", action="store", dest="chave",type='int',help="Chave utilizada para encriptar ou decriptar a mensagem",metavar="CHAVE")
(options, args) = parser.parse_args()


if options.encriptar and options.decriptar:
    print 'Opções conflitantes -e e -d'
if not options.encriptar and not options.decriptar:
    options.encriptar=True
if options.chave == None:
    print 'É necessaria uma chave para a ação selecionada.\nTente passar uma atraves do parametro -c'
    sys.exit(1)    
if options.chave > 25 or options.chave < 1:
    print 'A chave deve ser de 1 a 25'
    print options.chave
    sys.exit(1)

if args == ['']:
    mensagem=raw_input()
else:
    mensagem=''
    for string in args:
        mensagem+=string+' '

chave=options.chave
mensagem_encriptada=''

if options.encriptar:
    for byte in mensagem:
        if byte.isalpha():
            byte_encriptado=chr(ord(byte)+chave)
            if byte.isupper() and ord(byte_encriptado) > 90:
                byte_encriptado=chr(ord(byte_encriptado)-26)
            if byte.islower() and ord(byte_encriptado) > 122:
                byte_encriptado=chr(ord(byte_encriptado)-26)
        else:
            byte_encriptado=byte
        mensagem_encriptada+=byte_encriptado
else:
    for byte in mensagem:
        if byte.isalpha():
            byte_encriptado=chr(ord(byte)-chave)
            if byte.isupper() and ord(byte_encriptado) < 65:
                byte_encriptado=chr(ord(byte_encriptado)+26)
            if byte.islower() and ord(byte_encriptado) < 97:
                byte_encriptado=chr(ord(byte_encriptado)+26)
        else:
            byte_encriptado=byte
        mensagem_encriptada+=byte_encriptado
        
print mensagem_encriptada
