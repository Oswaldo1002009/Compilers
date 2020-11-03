class Token:
    def __init__(self, token, cat, val):
        self.token = token
        self.cat = cat
        self.val = val
    
    def getToken(self):
        return self.token
    
    def getCat(self):
        return self.cat
    
    def getVal(self):
        return self.val

tokens = set()
tokens.add("=")
tokens.add("+")
tokens.add("-")
tokens.add("*")
tokens.add("(")
tokens.add(")")
tokens.add("%")
tokens.add(".")
tokens.add(":")
tokens.add(",")
tokens.add(";")
tokens.add(":=")
tokens.add("<>")
tokens.add(">")
tokens.add("<")
tokens.add(">=")
tokens.add("<=")

def readToken(i, text, token):
    if i < len(text):
        if token+text[i] in tokens:
            return i+1, token+text[i]
    return i, token