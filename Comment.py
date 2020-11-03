def readComment(i, text):
    for pos in range(i, len(text)):
        if pos+1 < len(text):
            if ""+text[pos]+text[pos+1] == "*)":
                return pos+2
    
    raise Exception("Error: Comment not closed")