#вводит никнейм, программа преобразует

def game(user_in):
    result =""
    size = len(user_in)
    index = 0 #go over each letter in string, find index of a letter; if index can be divided by 2, make it x.upper; else x.lower; #then add to the same string 
    for i in range(size):
        if i % 2:
            result += user_in[i].upper()
        else:
            result += user_in[i].lower()
    return(result)

name = "lt0025"
nickn = game(name)
nickn2 = game("city_that_never_sleeps")
print(nickn)
print(nickn2)