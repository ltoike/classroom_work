def get_sequence(text, symbol):
    result = ""
    for x in text:
        if x == symbol:
            result += x
        elif result:
            break
    return result

seq1 = get_sequence("cannon", "n")
seq2 = get_sequence("cannon", "y")

print ("seq1=", seq1)
print ("seq2=", seq2)