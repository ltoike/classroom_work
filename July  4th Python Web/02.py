my_file = open("pal.txt", encoding="utf-8")
text = my_file.read()
my_file.close()
a = text.split()

def ispalyndrome(word):
    return word == "".join(reversed(word))
result = filter(ispalyndrome, text.split())
#a = ", ".join(result)
print(list(result))


#text = filter(lambda  x: x == x[::-1], text.split())
#text = ", ".join(text)
#print(list(result))

