class Token:
    def __init__(self, token, cat, val, start, index):
        self.token = token
        self.cat = cat
        self.val = val
        self.coords = index[start]
    
    def getToken(self):
        return self.token
    
    def getCat(self):
        return self.cat
    
    def getVal(self):
        return self.val
    
    def getCoords(self):
        return self.coords

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