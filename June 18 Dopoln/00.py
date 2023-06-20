#вводит никнейм, программа преобразует

def game(user_in):
    result =""
    index = 0 #go over each letter in string, find index of a letter; if index can be divided by 2, make it x.upper; else x.lower; #then add to the same string 
    for x in user_in:
        if index % 2:
            result += x.upper()
        else:
            result += x.lower()
        index += 1
    return(result)

name = "lt0025"
nickn = game(name)
nickn2 = game("city_that_never_sleeps")
print(nickn)
print(nickn2)