def readString(i, text):
    string = ""

    for pos in range(i, len(text)):
        if text[pos] == '"':
            return pos+1, string
        string += text[pos]

    raise Exception("Error: String not closed")