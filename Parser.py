# -*- coding: utf-8 -*-
'''
Oswaldo David García Rodríguez A01206725
Analizador sintáctico
24/10/2020
'''

import Project as project
import numpy as np
import pandas as pd
from collections import deque

#Read grammar
source = open("grammar.txt", 'r')
grammar = []
for line in source:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    grammar.append(line_list)
source.close()

#Scan LR (1) table from a csv
try:
    table = pd.read_csv("Table.csv", header=[1], index_col=[0])
except IOError:
    raise Exception("Error: File 'Table.csv' doesn't exist")
    exit()

stack = deque()
stack.append(0)
input_ = project.q

print("Compiling", project.sys.argv[1])

def action():
    #print(stack)
    #print(input_[0].getToken(), input_[0].getCat(), input_[0].getVal())
    state = stack[-1]
    token = newToken()

    action = table[token][state]
    #Check is a valid action
    if pd.isnull(action):
        print("Fatal: Syntax error, unexpected '" + str(input_[0].getVal()) + "' found")
        print("Fatal: Compliation aborted")
        exit()
    
    #Check if input was accepted
    elif action == 'acc':
        print('Compiled succesfully')

    #Check for shift action
    elif action[0] == 's':
        shift(int(action[1:]), token)
    
    #Check for redue action
    elif action[0] == 'r':
        reduce(int(action[1:]))

def newToken():
    if input_[0].getToken().lower() == 'word':
        if input_[0].getCat().lower() == 'lexeme':
            if input_[0].getVal().lower() == 'false' or input_[0].getCat().lower() == 'true':
                token = 'boolean'
            else:
                token = input_[0].getVal().lower()
        else: #We assume it's an id
            token = 'identifier'
    elif input_[0].getToken().lower() == 'token':
        token = input_[0].getVal()
    else: #We assume it's an integer, real or $
        token = input_[0].getToken().lower()
    return token

def shift(new_state, token):
    state = stack[-1]
    input_.pop(0) #Remove token
    #Add token and state to stack
    stack.append(token)
    stack.append(new_state)
    action()
    
def reduce(grammar_rule):
    i = 1
    #print(grammar[grammar_rule])
    #print(stack)
    while(True):
        if not grammar[grammar_rule][-i] == "''":
            if grammar[grammar_rule][-i] == '->':
                stack.append(grammar[grammar_rule][0])
                break
            elif not grammar[grammar_rule][-i] == stack[-2]:
                print("Fatal: Syntax error,", grammar[grammar_rule][-i], "expected but", stack[-2], "found")
                exit()
            else:
                stack.pop()
                stack.pop()
        i += 1
    goto(stack[-1], stack[-2])

def goto(goto, state):
    new_state = int(table[goto][state])
    stack.append(new_state)
    action()

action()