#вводит никнейм, программа преобразует

def game(user_in):
    result =""
    index = 0 #go over each letter in string, find index of a letter; if index can be divided by 2, make it x.upper; else x.lower; #then add to the same string 
    for x in user_in:
        if index % 2:
            result += x.lower()
        else:
            result += x.upper() #ИлОн МаСк
        if x != "" and x != "_":
            index += 1 
    return result

name = "Илон Маск"
nickn = game(name)
print(nickn)