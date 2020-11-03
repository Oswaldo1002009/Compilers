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
    txt = open(sys.argv[1], "r")
    txt2 = open(sys.argv[1], "r")
    text = txt.read()
    lines = txt2.readlines()
except IOError:
    raise Exception("Error: File '" + sys.argv[1] +  "' doesn't exist")
    exit()

#Queue for parser
q = []

#i to row,col
index = []
for row in range(len(lines)):
    for col in range(len(lines[row])):
        index.append((row+1,col+1))
index.append((row+1,col+2)) #Theorical position of EOF

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
        start = i
        i, string = readString(i+1, text)
        #print('STRING - VALUE = "' + string + '"')
        q.append( Token('STRING', 'VALUE', string, start, index) )

    #Number or token .
    elif text[i].isdigit() or text[i] == '.':
        start = i
        numberType, i, number = readNumber(i, text)
        if number == ".":
            #print("TOKEN - VALUE = .")
            q.append( Token('TOKEN', 'VALUE', '.', start, index) )
        elif numberType == "REAL":
            #print(numberType, "VALUE =", float(number))
            q.append( Token(numberType, 'VALUE', number, start, index) )
        else:
            #print(numberType, "VALUE =", int(number))
            q.append( Token(numberType, 'VALUE', number, start, index) )
    
    #Tokens or comments
    elif text[i] in tokens:
        #Comments
        start = i
        if i+1 < len(text):
            if ""+text[i]+text[i+1] == "(*":
                i = readComment(i+2, text)
            else:
                i, token = readToken(i+1, text, text[i])
                #print("TOKEN - VALUE = " + token)
                q.append( Token('TOKEN', 'VALUE', token, start, index) )
        else:
            i, token = readToken(i+1, text, text[i])
            #print("TOKEN - VALUE = " + token)
            q.append( Token('TOKEN', 'VALUE', token, start, index) )
    
    #Lexeme
    elif text[i].isalpha():
        start = i
        lexemeType, i, lexeme = readLexeme(i, text)
        #print("WORD -", lexemeType, "=", lexeme)
        q.append( Token('WORD', lexemeType, lexeme, start, index) )

    else:
        i += 1

q.append( Token('$', 'VALUE', 'EOF', i, index) )

#Print results
'''while q:
    e = q.pop(0)
    print(e.getToken(), '-', e.getCat(), '=', e.getVal())
print("EOF")'''