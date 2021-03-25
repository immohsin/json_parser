from typing import List

def parse_array(tokens: List):
    json_array = []
    if tokens[0] == ']':
        return json_array, tokens[1:]
    
    while len(tokens):
        json, tokens = parse(tokens)
        json_array.append(json)
        t = tokens[0]
        if t == ']':
            return json_array, tokens[1:]
        elif t != ',':
            raise Exception("Expected a comma after a object in an array")
        else:
            tokens = tokens[1:]
    
    raise Exception('Expected end-of-array bracket')

def parse_object(tokens: List):
    json_obj = {}
    t = tokens[0]
    if t == "}":
        return json_obj, tokens[1:]
    while len(tokens):
        json_key = tokens[0]
        if isinstance(json_key, str):
            tokens = tokens[1:]
        else:
            raise Exception("Excepted json key, got: {}".format(json_key))
        
        if tokens[0] == ":":
            tokens = tokens[1:]
        else:
            raise Exception("Excepted colon after key in object, got: {}".format(tokens[0]))
        
        json_val, tokens = parse(tokens)
        json_obj[json_key] = json_val
        try:
            t = tokens[0]
        except:
            raise Exception('Expected end-of-object brace')
        if t == "}":
            return json_obj, tokens[1:]
        elif t != ",":
            raise Exception('Expected comma after pair in object, got: {}'.format(t))
        
        tokens = tokens[1:]
    


def parse(tokens: List):
    t = tokens[0]
    if t == "[":
        return parse_array(tokens[1:])
    elif t == "{":
        return parse_object(tokens[1:])
    else:
        return t, tokens[1:]
