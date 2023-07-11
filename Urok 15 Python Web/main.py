my_file = open("text", encoding="utf-8")
text = my_file.read()
my_file.close()

#1
#a = text.startswith("abc")
#if text.startswith("abc"):
    #text = text.replace("abc", "www.")
#else:
    #text = text[0:4]+".com"+text[4:]

#print(text)
#def shortest(x, y):
    #if len(x) > len(y):
        #return y
    #else:
        #return x
2
#text = text.split(' ')
#smallest = 1
#x = len(text)
#for x in text:
    #text_len = len(x)
    #if text_len < smallest:

#print(smallest)

#3
#text = text.split(' ')
#print(text)
#counter = 0
#for x in text:
    #if x.isdigit() is True:
        #counter += 1
#print(counter)

#4
text = text.split(' ')
passed = {}
duplicates = []

for x in text:
    if x in passed:
        duplicates.append(x)
    else:
        passed[x] = True
print('Найденные дубликаты:', duplicates)



