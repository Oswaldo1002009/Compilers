# -*- coding: utf-8 -*-
'''
Oswaldo David García Rodríguez A01206725
Analizador léxico
05/09/2020
'''

import sys
import queue

#Check for usage
if len(sys.argv) < 2:
    raise Exception("Usage: python AppName file")
    exit()

#Check if file exists by trying to get its text
try:
    text = open(sys.argv[1], "r").read()
except IOError:
    raise Exception("Error: File '" + sys.argv[1] +  "' doesn't exist")
    exit()

#Queue for parser
q = []

#Import py files just if usage is correct and input file exists
from String import *
from Comment import *
from Number import *
from Lexeme import *
from Token import *

#Start scanning 
i = 0
while(i < len(text)):
    #Strings
    if text[i] == '"':
        i, string = readString(i+1, text)
        #print('STRING - VALUE = "' + string + '"')
        q.append( Token('STRING', 'VALUE', string) )

    #Number or token .
    elif text[i].isdigit() or text[i] == '.':
        numberType, i, number = readNumber(i, text)
        if number == ".":
            #print("TOKEN - VALUE = .")
            q.append( Token('TOKEN', 'VALUE', '.') )
        elif numberType == "REAL":
            #print(numberType, "VALUE =", float(number))
            q.append( Token(numberType, 'VALUE', number) )
        else:
            #print(numberType, "VALUE =", int(number))
            q.append( Token(numberType, 'VALUE', number) )
    
    #Tokens or comments
    elif text[i] in tokens:
        #Comments
        if i+1 < len(text):
            if ""+text[i]+text[i+1] == "(*":
                i = readComment(i+2, text)
            else:
                i, token = readToken(i+1, text, text[i])
                #print("TOKEN - VALUE = " + token)
                q.append( Token('TOKEN', 'VALUE', token) )
    
    #Lexeme
    elif text[i].isalpha():
        lexemeType, i, lexeme = readLexeme(i, text)
        #print("WORD -", lexemeType, "=", lexeme)
        q.append( Token('WORD', lexemeType, lexeme) )

    else:
        i += 1

q.append( Token('$', 'VALUE', 'EOF') )

#Print results
'''while q:
    e = q.pop(0)
    print(e.getToken(), '-', e.getCat(), '=', e.getVal())
print("EOF")'''