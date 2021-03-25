JSON_QUOTE = '"'
JSON_SYNTAX = ['{', '}', ",","]", "[", ":", JSON_QUOTE]
JSON_WHITESPACE = ['\n', '\t', ' ', '\b', '\r']

FALSE_LEN = len("false")
TRUE_LEN = len("true")
NULL_LEN = len("null")

def lex_string(string):
    j_string = ''
    if string[0] == JSON_QUOTE:
        string = string[1:]
    else:
        return None, string
    
    for c in string:
        if c in JSON_QUOTE:
            return j_string, string[len(j_string)+1:]
        else:
            j_string += c
    raise Exception('Expected end-of-string quote')

def lex_bool(string):
    string_len = len(string)
    if string_len > TRUE_LEN and string[:TRUE_LEN] == "true":
        return True, string[TRUE_LEN:]
    elif string_len > FALSE_LEN and string[:FALSE_LEN] == "false":
        return False, string[FALSE_LEN:]
    
    return None, string
            

def lex_null(string):
    string_len = len(string)
    if string_len > NULL_LEN and string[:NULL_LEN] == "null":
        return True, string[NULL_LEN:]
    return None, string

def lex_int(string):
    j_num = ''
    num_char = list(map(str, [0,1,2,3,4,5,6,7,8,9,'-','.', 'e']))
    for n in string:
        if n in num_char:
            j_num += n
        else:
            break
    
    if not len(j_num):
        return None, string
    
    rest = string[len(j_num):]
    if '.' in j_num:
        return float(j_num), rest

    return int(j_num), rest

def lex(j_string: str):
    tokens = []

    while len(j_string):
        json_string, j_string = lex_string(j_string)
        # print(json_string)
        if json_string is not None:
            tokens.append(json_string)
            continue
        
        json_bool, j_string = lex_bool(j_string)
        if json_bool is not None:
            tokens.append(json_bool)
            continue
        
        json_null, j_string = lex_null(j_string)
        if json_null is not None:
            tokens.append(json_null)
            continue
        
        json_int, j_string = lex_int(j_string)
        if json_int is not None:
            tokens.append(json_int)
            continue
        
        if j_string[0] in JSON_WHITESPACE:
            j_string = j_string[1:]
        elif j_string[0] in JSON_SYNTAX:
            tokens.append(j_string[0])
            j_string = j_string[1:]
        else:
            raise Exception("Unexpected character: {}".format(j_string[0]))
    
    return tokens
            


if __name__ == "__main__":
    print(lex('{"name": false}'))