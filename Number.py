def readNumber(i, text):
    number = ""
    while i < len(text):
        if text[i].isdigit(): #INTEGER
            number += text[i]
            i += 1

        elif text[i] == ".": #REAL
            number += text[i]
            i += 1
            while i < len(text):
                if text[i].isdigit():
                    number += text[i]
                    i += 1
                elif text[i].lower() == "e":
                    number += text[i]
                    i += 1
                    while i < len(text):
                        if text[i].isdigit():
                            number += text[i]
                            i += 1
                        else:
                            if number[-1].lower() == "e":
                                number += text[i]
                                raise Exception('Error, illegal expression "' + number + '"')
                            else:
                                return "REAL", i, number
                else:
                    return "REAL", i, number

        elif text[i].lower() == "e": #REAL
            number += text[i]
            i += 1
            while i < len(text):
                if text[i].isdigit():
                    number += text[i]
                    i += 1
                elif text[i] == ".":
                    number += text[i]
                    raise Exception('Error, illegal expression "' + number + '"')
                else:
                    if number[-1].lower() == "e":
                        number += text[i]
                        raise Exception('Error, illegal expression "' + number + '"')
                    else:
                        return "REAL", i, number
        
        elif text[i].isalpha(): #SyntaxError
            number += text[i]
            raise Exception('Error, illegal expression "' + number + '"')

        else:
            return "INTEGER", i, number
    
    if number == ".":
        return "TOKEN", i, number
    elif "." in number or "e" in number.lower():
        return "REAL", i, number
    else:
        return "INTEGER", i, number