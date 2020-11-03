reserved = set()

reserved.add("program")
reserved.add("constant")
reserved.add("var")
reserved.add("begin")
reserved.add("end")
reserved.add("integer")
reserved.add("real")
reserved.add("boolean")
reserved.add("string")
reserved.add("assign")
reserved.add("writeln")
reserved.add("readln")
reserved.add("while")
reserved.add("do")
reserved.add("repeat")
reserved.add("until")
reserved.add("for")
reserved.add("to")
reserved.add("downto")
reserved.add("if")
reserved.add("then")
reserved.add("else")
reserved.add("not")
reserved.add("false")
reserved.add("true")
reserved.add("div")
reserved.add("mod")
reserved.add("and")
reserved.add("or")

def readLexeme(i, text):
    lexeme = ""
    while i < len(text):
        if text[i].isdigit() or text[i].isalpha():
            lexeme += text[i]
            i += 1
        else:
            return isReserved(lexeme), i, lexeme
    return isReserved(lexeme), i, lexeme

def isReserved(lexeme):
    if lexeme.lower() in reserved:
        return "LEXEME"
    else:
        return "IDENTIFIER"